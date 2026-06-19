from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """User model for authentication and tracking"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    progress = db.relationship('Progress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    quiz_results = db.relationship('QuizResult', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    pipelines = db.relationship('Pipeline', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'


class Progress(db.Model):
    """Track user progress through modules"""
    __tablename__ = 'progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    module_name = db.Column(db.String(100), nullable=False)
    module_type = db.Column(db.String(50), nullable=False)  # 'theory', 'quiz', 'exercise'
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime)
    time_spent = db.Column(db.Integer, default=0)  # in seconds
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        db.UniqueConstraint('user_id', 'module_name', 'module_type', name='unique_user_module'),
    )
    
    def __repr__(self):
        return f'<Progress {self.user_id}:{self.module_name}>'


class QuizResult(db.Model):
    """Store quiz results"""
    __tablename__ = 'quiz_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Integer)  # in seconds
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    answers = db.Column(db.JSON)  # Store user answers
    
    def __repr__(self):
        return f'<QuizResult {self.user_id}:{self.quiz_id}:{self.score}>'


class Pipeline(db.Model):
    """Save preprocessing pipelines"""
    __tablename__ = 'pipelines'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    dataset_name = db.Column(db.String(200))
    steps = db.Column(db.JSON, nullable=False)  # Store pipeline steps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Pipeline {self.name}>'


class Dataset(db.Model):
    """Track uploaded datasets"""
    __tablename__ = 'datasets'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.Integer)  # in bytes
    rows = db.Column(db.Integer)
    columns = db.Column(db.Integer)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_temporary = db.Column(db.Boolean, default=True)
    
    user = db.relationship('User', backref='datasets')
    
    def __repr__(self):
        return f'<Dataset {self.original_filename}>'

# Made with Bob
