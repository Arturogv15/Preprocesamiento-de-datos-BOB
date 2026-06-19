<<<<<<< HEAD
import os
from app import create_app, db
from app.models import User, Progress, QuizResult, Pipeline, Dataset

# Create Flask application
app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell"""
    return {
        'db': db,
        'User': User,
        'Progress': Progress,
        'QuizResult': QuizResult,
        'Pipeline': Pipeline,
        'Dataset': Dataset
    }


@app.cli.command()
def init_db():
    """Initialize the database"""
    db.create_all()
    print('Database initialized successfully!')


@app.cli.command()
def create_admin():
    """Create an admin user"""
    from app import bcrypt
    
    username = input('Enter admin username: ')
    email = input('Enter admin email: ')
    password = input('Enter admin password: ')
    
    # Check if user exists
    if User.query.filter_by(username=username).first():
        print('User already exists!')
        return
    
    # Create admin user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    admin = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )
    
    db.session.add(admin)
    db.session.commit()
    
    print(f'Admin user {username} created successfully!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
=======
import os
from app import create_app, db
from app.models import User, Progress, QuizResult, Pipeline, Dataset

# Create Flask application
app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell"""
    return {
        'db': db,
        'User': User,
        'Progress': Progress,
        'QuizResult': QuizResult,
        'Pipeline': Pipeline,
        'Dataset': Dataset
    }


@app.cli.command()
def init_db():
    """Initialize the database"""
    db.create_all()
    print('Database initialized successfully!')


@app.cli.command()
def create_admin():
    """Create an admin user"""
    from app import bcrypt
    
    username = input('Enter admin username: ')
    email = input('Enter admin email: ')
    password = input('Enter admin password: ')
    
    # Check if user exists
    if User.query.filter_by(username=username).first():
        print('User already exists!')
        return
    
    # Create admin user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    admin = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )
    
    db.session.add(admin)
    db.session.commit()
    
    print(f'Admin user {username} created successfully!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
