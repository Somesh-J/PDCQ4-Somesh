"""
Application entry point
Runs the Flask development server
"""
from app import create_app

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run development server
    app.run(debug=True, host='127.0.0.1', port=5000)
