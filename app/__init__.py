"""
Flask application factory
"""
from flask import Flask
from authlib.integrations.flask_client import OAuth

# Initialize OAuth globally
oauth = OAuth()


def create_app():
    """
    Application factory pattern for creating Flask app instance
    """
    app = Flask(__name__, template_folder='../templates')
    
    # Load configuration
    from app.config import Config
    app.config.from_object(Config)
    
    # Initialize OAuth with app
    oauth.init_app(app)
    
    # Register Google OAuth provider
    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
        client_kwargs={
            'scope': ' '.join(app.config['GOOGLE_SCOPES'])
        }
    )
    
    # Register blueprints
    from app.auth import auth_bp
    from app.routes import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    return app
