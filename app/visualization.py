import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import base64
from io import BytesIO
import json


class VisualizationGenerator:
    """Generate various data visualizations"""
    
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        sns.set_style("whitegrid")
    
    def boxplot(self, columns=None, orientation='vertical'):
        """Generate box plot using Plotly"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        if not columns:
            return {'error': 'No numerical columns found'}
        
        # Create box plot
        fig = go.Figure()
        
        for col in columns[:10]:  # Limit to 10 columns
            fig.add_trace(go.Box(
                y=self.df[col] if orientation == 'vertical' else None,
                x=self.df[col] if orientation == 'horizontal' else None,
                name=col,
                boxmean='sd'
            ))
        
        fig.update_layout(
            title='Box Plot - Outlier Detection',
            xaxis_title='Variables' if orientation == 'vertical' else 'Values',
            yaxis_title='Values' if orientation == 'vertical' else 'Variables',
            showlegend=True,
            height=500
        )
        
        return fig.to_json()
    
    def histogram(self, column, bins=30, kde=True):
        """Generate histogram with optional KDE"""
        if column not in self.df.columns:
            return {'error': f'Column {column} not found'}
        
        # Create histogram with Plotly
        fig = px.histogram(
            self.df,
            x=column,
            nbins=bins,
            title=f'Distribution of {column}',
            marginal='box' if not kde else 'violin'
        )
        
        fig.update_layout(
            xaxis_title=column,
            yaxis_title='Frequency',
            showlegend=False,
            height=500
        )
        
        return fig.to_json()
    
    def scatter(self, x_column, y_column, hue=None, size=None):
        """Generate scatter plot"""
        if x_column not in self.df.columns or y_column not in self.df.columns:
            return {'error': 'Column not found'}
        
        # Create scatter plot
        fig = px.scatter(
            self.df,
            x=x_column,
            y=y_column,
            color=hue if hue and hue in self.df.columns else None,
            size=size if size and size in self.df.columns else None,
            title=f'{y_column} vs {x_column}',
            trendline='ols'
        )
        
        fig.update_layout(
            xaxis_title=x_column,
            yaxis_title=y_column,
            height=500
        )
        
        return fig.to_json()
    
    def heatmap(self, method='pearson', columns=None):
        """Generate correlation heatmap"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(columns) < 2:
            return {'error': 'Need at least 2 numerical columns'}
        
        # Calculate correlation matrix
        corr_matrix = self.df[columns].corr(method=method)
        
        # Create heatmap with Plotly
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0,
            text=corr_matrix.values.round(2),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            title=f'Correlation Heatmap ({method.capitalize()})',
            xaxis_title='Features',
            yaxis_title='Features',
            height=600,
            width=700
        )
        
        return fig.to_json()
    
    def pairplot(self, columns=None, hue=None):
        """Generate pair plot (scatter matrix)"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()[:5]
        
        if len(columns) < 2:
            return {'error': 'Need at least 2 columns'}
        
        # Create scatter matrix
        fig = px.scatter_matrix(
            self.df,
            dimensions=columns,
            color=hue if hue and hue in self.df.columns else None,
            title='Pair Plot - Feature Relationships'
        )
        
        fig.update_layout(
            height=800,
            width=800
        )
        
        return fig.to_json()
    
    def missing_data_heatmap(self):
        """Visualize missing data patterns"""
        # Create binary matrix (1 = missing, 0 = present)
        missing_matrix = self.df.isnull().astype(int)
        
        fig = go.Figure(data=go.Heatmap(
            z=missing_matrix.T.values,
            x=missing_matrix.index,
            y=missing_matrix.columns,
            colorscale=[[0, 'lightblue'], [1, 'red']],
            showscale=True,
            colorbar=dict(
                title="Missing",
                tickvals=[0, 1],
                ticktext=['Present', 'Missing']
            )
        ))
        
        fig.update_layout(
            title='Missing Data Pattern',
            xaxis_title='Row Index',
            yaxis_title='Columns',
            height=500
        )
        
        return fig.to_json()
    
    def distribution_plot(self, column):
        """Generate distribution plot with statistics"""
        if column not in self.df.columns:
            return {'error': f'Column {column} not found'}
        
        data = self.df[column].dropna()
        
        # Create figure with subplots
        fig = go.Figure()
        
        # Add histogram
        fig.add_trace(go.Histogram(
            x=data,
            name='Histogram',
            nbinsx=30,
            opacity=0.7
        ))
        
        # Add KDE (approximation using histogram with many bins)
        fig.update_layout(
            title=f'Distribution of {column}',
            xaxis_title=column,
            yaxis_title='Frequency',
            showlegend=True,
            height=500,
            annotations=[
                dict(
                    text=f"Mean: {data.mean():.2f}<br>Median: {data.median():.2f}<br>Std: {data.std():.2f}",
                    xref="paper", yref="paper",
                    x=0.95, y=0.95,
                    showarrow=False,
                    bgcolor="white",
                    bordercolor="black",
                    borderwidth=1
                )
            ]
        )
        
        return fig.to_json()
    
    def outlier_visualization(self, column, method='iqr'):
        """Visualize outliers in a column"""
        if column not in self.df.columns:
            return {'error': f'Column {column} not found'}
        
        data = self.df[column].dropna()
        
        # Detect outliers
        if method == 'iqr':
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data < lower_bound) | (data > upper_bound)]
        else:  # zscore
            z_scores = np.abs((data - data.mean()) / data.std())
            outliers = data[z_scores > 3]
        
        # Create box plot with outliers highlighted
        fig = go.Figure()
        
        fig.add_trace(go.Box(
            y=data,
            name=column,
            boxpoints='outliers',
            marker=dict(
                color='red',
                size=8
            )
        ))
        
        fig.update_layout(
            title=f'Outlier Detection - {column} ({method.upper()})',
            yaxis_title='Values',
            showlegend=False,
            height=500,
            annotations=[
                dict(
                    text=f"Outliers detected: {len(outliers)}<br>({len(outliers)/len(data)*100:.1f}% of data)",
                    xref="paper", yref="paper",
                    x=0.95, y=0.95,
                    showarrow=False,
                    bgcolor="white",
                    bordercolor="black",
                    borderwidth=1
                )
            ]
        )
        
        return fig.to_json()
    
    def feature_importance_plot(self, feature_names, importance_scores):
        """Visualize feature importance"""
        # Sort by importance
        sorted_idx = np.argsort(importance_scores)[::-1][:20]  # Top 20
        sorted_features = [feature_names[i] for i in sorted_idx]
        sorted_scores = [importance_scores[i] for i in sorted_idx]
        
        fig = go.Figure(go.Bar(
            x=sorted_scores,
            y=sorted_features,
            orientation='h',
            marker=dict(
                color=sorted_scores,
                colorscale='Viridis'
            )
        ))
        
        fig.update_layout(
            title='Feature Importance',
            xaxis_title='Importance Score',
            yaxis_title='Features',
            height=600,
            yaxis=dict(autorange="reversed")
        )
        
        return fig.to_json()
    
    def pca_variance_plot(self, explained_variance):
        """Plot PCA explained variance"""
        n_components = len(explained_variance)
        cumulative_variance = np.cumsum(explained_variance)
        
        fig = go.Figure()
        
        # Individual variance
        fig.add_trace(go.Bar(
            x=list(range(1, n_components + 1)),
            y=explained_variance,
            name='Individual',
            marker_color='lightblue'
        ))
        
        # Cumulative variance
        fig.add_trace(go.Scatter(
            x=list(range(1, n_components + 1)),
            y=cumulative_variance,
            name='Cumulative',
            mode='lines+markers',
            marker=dict(size=10, color='red'),
            line=dict(width=2, color='red')
        ))
        
        fig.update_layout(
            title='PCA Explained Variance',
            xaxis_title='Principal Component',
            yaxis_title='Explained Variance Ratio',
            showlegend=True,
            height=500
        )
        
        return fig.to_json()
    
    def categorical_distribution(self, column, top_n=10):
        """Visualize categorical variable distribution"""
        if column not in self.df.columns:
            return {'error': f'Column {column} not found'}
        
        # Get value counts
        value_counts = self.df[column].value_counts().head(top_n)
        
        fig = go.Figure(go.Bar(
            x=value_counts.index.astype(str),
            y=value_counts.values,
            marker=dict(
                color=value_counts.values,
                colorscale='Blues'
            ),
            text=value_counts.values,
            textposition='auto'
        ))
        
        fig.update_layout(
            title=f'Distribution of {column} (Top {top_n})',
            xaxis_title=column,
            yaxis_title='Count',
            height=500
        )
        
        return fig.to_json()
    
    @staticmethod
    def matplotlib_to_base64(fig):
        """Convert matplotlib figure to base64 string"""
        buffer = BytesIO()
        fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close(fig)
        return f"data:image/png;base64,{image_base64}"

# Made with Bob
