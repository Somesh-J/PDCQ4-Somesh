"""
Authentication module - Google OAuth logic
"""
from flask import Blueprint, redirect, url_for, session, request
from app import oauth

# Create Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login')
def login():
    """
    Initiate Google OAuth login flow
    """
    # Generate redirect URI for OAuth callback
    redirect_uri = url_for('auth.callback', _external=True)
    
    # Redirect user to Google's OAuth authorization page
    return oauth.google.authorize_redirect(redirect_uri)


@auth_bp.route('/callback')
def callback():
    """
    Handle Google OAuth callback
    """
    try:
        # Retrieve access token from Google
        token = oauth.google.authorize_access_token()
        
        # Fetch user information using the token
        user_info = token.get('userinfo')
        
        if user_info:
            # Store user data in Flask session
            session.permanent = True
            session['user'] = {
                'name': user_info.get('name'),
                'email': user_info.get('email'),
                'picture': user_info.get('picture'),
                'sub': user_info.get('sub')  # Google user ID
            }
            
            # Redirect to home page after successful login
            return redirect(url_for('main.home'))
        else:
            # Handle case where user info is not available
            return redirect(url_for('main.index'))
            
    except Exception as e:
        # Handle OAuth errors gracefully
        print(f"OAuth error: {e}")
        return redirect(url_for('main.index'))


@auth_bp.route('/logout')
def logout():
    """
    Logout user and clear session
    """
    # Clear all session data
    session.clear()
    
    # Redirect to login page
    return redirect(url_for('main.index'))
