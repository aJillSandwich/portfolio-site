from app import create_app

# Create an instance of the Flask application
app = create_app()

# This block ensures the server only runs when the script is executed directly
# (and not when it's imported by another script)
if __name__ == '__main__':
    # app.run() starts the Flask development server.
    # debug=True enables debug mode, which will auto-reload the server
    # when you save changes and provide helpful error pages.
    app.run(debug=True)