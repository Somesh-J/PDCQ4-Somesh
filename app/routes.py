"""
Main application routes
"""
from flask import Blueprint, render_template, session, redirect, url_for, request
from functools import wraps
from app.utils import get_ist_time, generate_pattern

# Create Blueprint for main routes
main_bp = Blueprint('main', __name__)


def login_required(f):
    """
    Decorator to require login for protected routes
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function


@main_bp.route('/')
def index():
    """
    Landing page - redirects based on authentication status
    """
    # Check if user is authenticated
    if 'user' in session:
        return redirect(url_for('main.home'))
    
    # Show login page if not authenticated
    return render_template('login.html')


@main_bp.route('/home')
@login_required
def home():
    """
    User dashboard after successful login
    """
    # Get user data from session
    user = session.get('user')
    
    # Get current IST time
    ist_time = get_ist_time()
    
    # Render home page with user info and IST time
    return render_template('home.html', user=user, ist_time=ist_time)


@main_bp.route('/pattern', methods=['GET', 'POST'])
@login_required
def pattern():
    """
    Pattern generation page
    Handles both GET (show form) and POST (generate pattern)
    """
    pattern_output = None
    error = None
    num_lines = None
    
    if request.method == 'POST':
        # Get number of lines from form data
        try:
            num_lines = int(request.form.get('num_lines', 0))
            
            # Validate input
            if num_lines < 1:
                error = "Please enter a positive number"
            elif num_lines > 100:
                error = "Maximum number of lines is 100"
            else:
                # Generate pattern
                pattern_output = generate_pattern(num_lines)
        except (ValueError, TypeError):
            error = "Please enter a valid number"
    
    # Get user data and IST time
    user = session.get('user')
    ist_time = get_ist_time()
    
    return render_template('pattern.html', 
                         user=user, 
                         ist_time=ist_time,
                         pattern=pattern_output,
                         error=error,
                         num_lines=num_lines)
