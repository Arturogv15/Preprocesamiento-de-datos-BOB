from flask import Blueprint, request, jsonify, current_app, send_file
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np
from datetime import datetime
import json
import io

from app import db
from app.models import Dataset, Progress, QuizResult, Pipeline
from app.data_processing import DataProcessor
from app.visualization import VisualizationGenerator

api_bp = Blueprint('api', __name__)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@api_bp.route('/data/upload', methods=['POST'])
@login_required
def upload_dataset():
    """Upload a dataset file"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'File type not allowed'}), 400
    
    try:
        # Secure the filename
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{current_user.id}_{timestamp}_{filename}"
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Save file
        file.save(filepath)
        
        # Read and analyze the file
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(filepath)
        elif filename.endswith('.json'):
            df = pd.read_json(filepath)
        else:
            return jsonify({'success': False, 'error': 'Unsupported file format'}), 400
        
        # Store dataset metadata
        dataset = Dataset(
            user_id=current_user.id,
            filename=unique_filename,
            original_filename=filename,
            file_size=os.path.getsize(filepath),
            rows=len(df),
            columns=len(df.columns)
        )
        db.session.add(dataset)
        db.session.commit()
        
        # Return preview
        preview = df.head(10).to_dict('records')
        
        return jsonify({
            'success': True,
            'dataset_id': dataset.id,
            'filename': filename,
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': df.columns.tolist(),
            'dtypes': df.dtypes.astype(str).to_dict(),
            'preview': preview
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/data/datasets', methods=['GET'])
@login_required
def get_datasets():
    """Get list of available datasets (pre-loaded + user uploads)"""
    # Pre-loaded datasets
    dataset_folder = current_app.config['DATASET_FOLDER']
    preloaded = []
    
    if os.path.exists(dataset_folder):
        for filename in os.listdir(dataset_folder):
            if filename.endswith(('.csv', '.xlsx', '.xls')):
                filepath = os.path.join(dataset_folder, filename)
                preloaded.append({
                    'id': f'preloaded_{filename}',
                    'name': filename,
                    'type': 'preloaded',
                    'size': os.path.getsize(filepath)
                })
    
    # User uploaded datasets
    user_datasets = Dataset.query.filter_by(user_id=current_user.id).all()
    uploaded = [{
        'id': str(d.id),
        'name': d.original_filename,
        'type': 'uploaded',
        'rows': d.rows,
        'columns': d.columns,
        'uploaded_at': d.uploaded_at.isoformat()
    } for d in user_datasets]
    
    return jsonify({
        'success': True,
        'preloaded': preloaded,
        'uploaded': uploaded
    })


@api_bp.route('/data/preview/<dataset_id>', methods=['GET'])
@login_required
def preview_dataset(dataset_id):
    """Get dataset preview and statistics"""
    try:
        # Load dataset
        if dataset_id.startswith('preloaded_'):
            filename = dataset_id.replace('preloaded_', '')
            filepath = os.path.join(current_app.config['DATASET_FOLDER'], filename)
        else:
            dataset = Dataset.query.get_or_404(dataset_id)
            if dataset.user_id != current_user.id:
                return jsonify({'success': False, 'error': 'Unauthorized'}), 403
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], dataset.filename)
        
        # Read file
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif filepath.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(filepath)
        else:
            return jsonify({'success': False, 'error': 'Unsupported format'}), 400
        
        # Replace NaN with None for JSON serialization
        df = df.replace({np.nan: None})
        
        # Generate statistics
        processor = DataProcessor(df)
        stats = processor.get_statistics()
        
        return jsonify({
            'success': True,
            'preview': df.head(100).to_dict('records'),
            'statistics': stats
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/data/clean', methods=['POST'])
@login_required
def clean_data():
    """Apply data cleaning operations"""
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        operation = data.get('operation')
        params = data.get('params', {})
        
        # Load dataset
        df = load_dataset(dataset_id)
        
        # Apply cleaning operation
        processor = DataProcessor(df)
        
        if operation == 'impute_missing':
            result_df, stats = processor.impute_missing(**params)
        elif operation == 'remove_duplicates':
            result_df, stats = processor.remove_duplicates(**params)
        elif operation == 'handle_outliers':
            result_df, stats = processor.handle_outliers(**params)
        else:
            return jsonify({'success': False, 'error': 'Unknown operation'}), 400
        
        return jsonify({
            'success': True,
            'preview': result_df.head(100).to_dict('records'),
            'statistics': stats,
            'rows_affected': stats.get('rows_affected', 0)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/data/transform', methods=['POST'])
@login_required
def transform_data():
    """Apply data transformation operations"""
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        operation = data.get('operation')
        params = data.get('params', {})
        
        # Load dataset
        df = load_dataset(dataset_id)
        
        # Apply transformation
        processor = DataProcessor(df)
        
        if operation == 'scale':
            result_df, stats = processor.scale_features(**params)
        elif operation == 'encode':
            result_df, stats = processor.encode_categorical(**params)
        else:
            return jsonify({'success': False, 'error': 'Unknown operation'}), 400
        
        return jsonify({
            'success': True,
            'preview': result_df.head(100).to_dict('records'),
            'statistics': stats
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/viz/generate', methods=['POST'])
@login_required
def generate_visualization():
    """Generate visualization"""
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        viz_type = data.get('type')
        params = data.get('params', {})
        
        # Load dataset
        df = load_dataset(dataset_id)
        
        # Generate visualization
        viz_gen = VisualizationGenerator(df)
        
        if viz_type == 'boxplot':
            plot_data = viz_gen.boxplot(**params)
        elif viz_type == 'histogram':
            plot_data = viz_gen.histogram(**params)
        elif viz_type == 'scatter':
            plot_data = viz_gen.scatter(**params)
        elif viz_type == 'heatmap':
            plot_data = viz_gen.heatmap(**params)
        elif viz_type == 'pairplot':
            plot_data = viz_gen.pairplot(**params)
        else:
            return jsonify({'success': False, 'error': 'Unknown visualization type'}), 400
        
        return jsonify({
            'success': True,
            'plot_data': plot_data
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/progress/update', methods=['POST'])
@login_required
def update_progress():
    """Update user progress"""
    try:
        data = request.get_json()
        module_name = data.get('module_name')
        module_type = data.get('module_type')
        completed = data.get('completed', False)
        time_spent = data.get('time_spent', 0)
        
        # Silently ignore requests with missing parameters
        # (This can happen from pages that don't track progress)
        if not module_name or not module_type:
            return jsonify({'success': True, 'message': 'No progress to update'})
        
        # Find or create progress record
        progress = Progress.query.filter_by(
            user_id=current_user.id,
            module_name=module_name,
            module_type=module_type
        ).first()
        
        if not progress:
            progress = Progress(
                user_id=current_user.id,
                module_name=module_name,
                module_type=module_type,
                time_spent=0
            )
            db.session.add(progress)
        
        progress.completed = completed
        # Handle None value for time_spent
        progress.time_spent = (progress.time_spent or 0) + time_spent
        progress.last_accessed = datetime.utcnow()
        
        if completed and not progress.completion_date:
            progress.completion_date = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/quiz/submit', methods=['POST'])
@login_required
def submit_quiz():
    """Submit quiz answers"""
    try:
        data = request.get_json()
        module = data.get('module')
        score = data.get('score', 0)
        time_spent = data.get('time_spent', 0)
        answers = data.get('answers', {})
        
        # Convert answers dict to JSON string for storage
        answers_json = json.dumps(answers)
        
        # Calculate total questions from answers
        total_questions = len(answers) if answers else 0
        
        # Store result
        result = QuizResult(
            user_id=current_user.id,
            quiz_id=module,
            score=score,
            total_questions=total_questions,
            time_taken=time_spent,
            answers=answers_json
        )
        db.session.add(result)
        
        # Update progress for this module
        progress = Progress.query.filter_by(
            user_id=current_user.id,
            module_name=module,
            module_type='quiz'
        ).first()
        
        if not progress:
            progress = Progress(
                user_id=current_user.id,
                module_name=module,
                module_type='quiz',
                completed=score >= 70,  # Consider passed if score >= 70%
                time_spent=time_spent
            )
            db.session.add(progress)
        else:
            progress.completed = score >= 70
            progress.time_spent = (progress.time_spent or 0) + time_spent
            progress.last_accessed = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'score': score,
            'total': total_questions,
            'percentage': score
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/pipeline/save', methods=['POST'])
@login_required
def save_pipeline():
    """Save preprocessing pipeline"""
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description', '')
        dataset_name = data.get('dataset_name')
        steps = data.get('steps')
        
        pipeline = Pipeline(
            user_id=current_user.id,
            name=name,
            description=description,
            dataset_name=dataset_name,
            steps=steps
        )
        db.session.add(pipeline)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'pipeline_id': pipeline.id
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


def load_dataset(dataset_id):
    """Helper function to load dataset"""
    if dataset_id.startswith('preloaded_'):
        filename = dataset_id.replace('preloaded_', '')
        filepath = os.path.join(current_app.config['DATASET_FOLDER'], filename)
    else:
        dataset = Dataset.query.get_or_404(dataset_id)
        if dataset.user_id != current_user.id:
            raise PermissionError('Unauthorized access to dataset')
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], dataset.filename)
    
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith(('.xlsx', '.xls')):
        return pd.read_excel(filepath)
    elif filepath.endswith('.json'):
        return pd.read_json(filepath)
    else:
        raise ValueError('Unsupported file format')

# Made with Bob


@api_bp.route('/data/export/<format>', methods=['POST'])
@login_required
def export_data(format):
    """Export processed data in various formats"""
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        
        # Load dataset
        df = load_dataset(dataset_id)
        
        # Create in-memory file
        output = io.BytesIO()
        
        if format == 'csv':
            df.to_csv(output, index=False)
            output.seek(0)
            mimetype = 'text/csv'
            filename = 'processed_data.csv'
            
        elif format == 'excel':
            df.to_excel(output, index=False, engine='openpyxl')
            output.seek(0)
            mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            filename = 'processed_data.xlsx'
            
        elif format == 'json':
            json_str = df.to_json(orient='records', indent=2)
            output.write(json_str.encode('utf-8'))
            output.seek(0)
            mimetype = 'application/json'
            filename = 'processed_data.json'
            
        else:
            return jsonify({'success': False, 'error': 'Unsupported format'}), 400
        
        return send_file(
            output,
            mimetype=mimetype,
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api_bp.route('/data/export/report', methods=['POST'])
@login_required
def export_report():
    """Export comprehensive data analysis report"""
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        
        # Load dataset
        df = load_dataset(dataset_id)
        processor = DataProcessor(df)
        
        # Generate comprehensive statistics
        stats = processor.get_statistics()
        
        # Create report
        report = {
            'dataset_info': {
                'name': data.get('dataset_name', 'Unknown'),
                'rows': len(df),
                'columns': len(df.columns),
                'memory_usage': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
                'generated_at': datetime.now().isoformat()
            },
            'column_info': {
                col: {
                    'dtype': str(df[col].dtype),
                    'missing': int(df[col].isnull().sum()),
                    'unique': int(df[col].nunique()),
                    'sample_values': df[col].dropna().head(5).tolist()
                }
                for col in df.columns
            },
            'statistics': stats,
            'data_quality': {
                'total_missing': int(df.isnull().sum().sum()),
                'duplicate_rows': int(df.duplicated().sum()),
                'columns_with_missing': [col for col in df.columns if df[col].isnull().any()]
            }
        }
        
        # Export as JSON
        output = io.BytesIO()
        json_str = json.dumps(report, indent=2, default=str)
        output.write(json_str.encode('utf-8'))
        output.seek(0)
        
        return send_file(
            output,
            mimetype='application/json',
            as_attachment=True,
            download_name='data_analysis_report.json'
        )
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
