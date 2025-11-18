#!/bin/bash

# Production startup script for FormulaQ Flask app

echo "Starting FormulaQ Flask Application..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Set production environment
export FLASK_ENV=production
export PYTHONUNBUFFERED=1

# Create logs directory
mkdir -p logs

# Start the application with gunicorn
echo "Starting application with Gunicorn..."
gunicorn --config gunicorn.conf.py run:app

echo "Application stopped."