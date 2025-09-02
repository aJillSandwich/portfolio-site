import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login' # The route for the login page
login_manager.login_message_category = 'info'
mail = Mail()

def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Get the absolute path of the project's root directory
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # Load configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    # Use the absolute path for the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- NEW DEBUGGING LINE ---
    print(f"DATABASE PATH IS NOW: {app.config['SQLALCHEMY_DATABASE_URI']}")
    # --------------------------

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

