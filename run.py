"""
Application entry point
Runs the Flask server in development or production mode
"""
import os
from app import create_app

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    # Check if running in production
    if os.getenv('FLASK_ENV') == 'production':
        # Production mode - let gunicorn handle this
        # This block won't be reached when using gunicorn
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        # Development mode
        app.run(debug=True, host='127.0.0.1', port=5000)
