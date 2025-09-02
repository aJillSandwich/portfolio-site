from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin

# This function is required by Flask-Login. It's used to reload the user object
# from the user ID stored in the session.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    User model for authentication.
    UserMixin provides default implementations for the methods that Flask-Login expects user objects to have.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    
    # Relationships: This links the User model to the Project and Post models.
    # The 'backref' argument adds a 'user' attribute to the Project and Post models,
    # so you can easily access the user who created a project or post.
    # 'lazy=True' means that the data will be loaded from the database as needed.
    projects = db.relationship('Project', backref='author', lazy=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Project(db.Model):
    """
    Project model for portfolio projects.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), nullable=False)
    project_link = db.Column(db.String(200), nullable=True)
    github_link = db.Column(db.String(200), nullable=True)
    
    # Foreign Key: This creates a link to the 'user' table.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Project('{self.title}', '{self.date_posted}')"

class Post(db.Model):
    """
    Post model for the blog.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    # Foreign Key: This creates a link to the 'user' table.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"