from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Progress, QuizResult, Pipeline

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Landing page"""
    return render_template('index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    # Get user progress statistics
    total_modules = 16  # 4 theory + 4 quizzes + 4 practice modules + 4 advanced
    completed_modules = Progress.query.filter_by(
        user_id=current_user.id,
        completed=True
    ).count()
    
    # Get quiz statistics
    quiz_results = QuizResult.query.filter_by(user_id=current_user.id).all()
    total_quizzes = len(quiz_results)
    avg_score = sum(r.score for r in quiz_results) / total_quizzes if total_quizzes > 0 else 0
    
    # Get saved pipelines
    pipelines = Pipeline.query.filter_by(user_id=current_user.id).order_by(
        Pipeline.updated_at.desc()
    ).limit(5).all()
    
    # Calculate progress percentage
    progress_percentage = (completed_modules / total_modules * 100) if total_modules > 0 else 0
    
    return render_template('dashboard.html',
                         completed_modules=completed_modules,
                         total_modules=total_modules,
                         progress_percentage=progress_percentage,
                         total_quizzes=total_quizzes,
                         avg_score=avg_score,
                         pipelines=pipelines)


@main_bp.route('/theory')
@login_required
def theory():
    """Theory modules overview"""
    modules = [
        {
            'id': 'data_cleaning',
            'title': 'Limpieza de Datos',
            'description': 'Aprende a manejar valores faltantes, duplicados y outliers',
            'icon': 'fa-broom'
        },
        {
            'id': 'data_transformation',
            'title': 'Transformación de Datos',
            'description': 'Normalización, estandarización y codificación de variables',
            'icon': 'fa-exchange-alt'
        },
        {
            'id': 'data_integration',
            'title': 'Integración de Datos',
            'description': 'Combina datasets usando diferentes tipos de joins',
            'icon': 'fa-link'
        },
        {
            'id': 'dimensionality_reduction',
            'title': 'Reducción de Dimensionalidad',
            'description': 'PCA y selección de características importantes',
            'icon': 'fa-compress'
        }
    ]
    
    # Check completion status for each module
    for module in modules:
        progress = Progress.query.filter_by(
            user_id=current_user.id,
            module_name=module['id'],
            module_type='theory'
        ).first()
        module['completed'] = progress.completed if progress else False
    
    return render_template('theory/index.html', modules=modules)


@main_bp.route('/theory/<module_id>')
@login_required
def theory_module(module_id):
    """Individual theory module"""
    valid_modules = ['data_cleaning', 'data_transformation', 
                    'data_integration', 'dimensionality_reduction']
    
    if module_id not in valid_modules:
        return redirect(url_for('main.theory'))
    
    return render_template(f'theory/{module_id}.html', module_id=module_id)


@main_bp.route('/practice')
@login_required
def practice():
    """Practice lab"""
    return render_template('practice/lab.html')


@main_bp.route('/quiz')
@login_required
def quiz_list():
    """List of available quizzes"""
    quizzes = [
        {
            'id': 'data_cleaning_quiz',
            'title': 'Quiz: Limpieza de Datos',
            'questions': 10,
            'time_limit': 15,
            'difficulty': 'Intermedio'
        },
        {
            'id': 'data_transformation_quiz',
            'title': 'Quiz: Transformación de Datos',
            'questions': 10,
            'time_limit': 15,
            'difficulty': 'Intermedio'
        },
        {
            'id': 'data_integration_quiz',
            'title': 'Quiz: Integración de Datos',
            'questions': 8,
            'time_limit': 12,
            'difficulty': 'Básico'
        },
        {
            'id': 'dimensionality_reduction_quiz',
            'title': 'Quiz: Reducción de Dimensionalidad',
            'questions': 12,
            'time_limit': 18,
            'difficulty': 'Avanzado'
        }
    ]
    
    # Check if user has taken each quiz
    for quiz in quizzes:
        result = QuizResult.query.filter_by(
            user_id=current_user.id,
            quiz_id=quiz['id']
        ).order_by(QuizResult.completed_at.desc()).first()
        
        quiz['taken'] = result is not None
        quiz['best_score'] = result.score if result else 0
    
    return render_template('quiz/list.html', quizzes=quizzes)


@main_bp.route('/quiz/<quiz_id>')
@login_required
def quiz(quiz_id):
    """Take a quiz"""
    # Map quiz_id to module name
    quiz_names = {
        'data_cleaning_quiz': 'Limpieza de Datos',
        'data_transformation_quiz': 'Transformación de Datos',
        'data_integration_quiz': 'Integración de Datos',
        'dimensionality_reduction_quiz': 'Reducción de Dimensionalidad'
    }
    
    # Extract module from quiz_id (remove _quiz suffix)
    module = quiz_id.replace('_quiz', '')
    module_name = quiz_names.get(quiz_id, 'Quiz')
    
    return render_template('quiz/quiz.html',
                         quiz_id=quiz_id,
                         module=module,
                         module_name=module_name)


@main_bp.route('/progress')
@login_required
def progress():
    """User progress page"""
    # Get all progress records
    progress_records = Progress.query.filter_by(user_id=current_user.id).all()
    
    # Get all quiz results
    quiz_results = QuizResult.query.filter_by(
        user_id=current_user.id
    ).order_by(QuizResult.completed_at.desc()).all()
    
    # Get all pipelines
    pipelines = Pipeline.query.filter_by(
        user_id=current_user.id
    ).order_by(Pipeline.updated_at.desc()).all()
    
    return render_template('progress.html',
                         progress_records=progress_records,
                         quiz_results=quiz_results,
                         pipelines=pipelines)

# Made with Bob
