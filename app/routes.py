from flask import Blueprint, render_template

# A Blueprint is a way to organize a group of related views and other code.
# Rather than registering views and other code directly with an application,
# they are registered with a blueprint. Then the blueprint is registered with
# the application when it is available in a factory function.
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    """Renders the home page."""
    # We will create the home.html template later.
    return "<h1>Welcome to the Home Page!</h1>"

@main.route('/projects')
def projects():
    """Renders the projects page."""
    return "<h1>Projects will be listed here.</h1>"

@main.route('/blog')
def blog():
    """Renders the blog page."""
    return "<h1>Blog posts will be listed here.</h1>"
