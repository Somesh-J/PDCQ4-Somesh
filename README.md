# FormulaQ - Python Developer Challenge

A Flask application with Google OAuth authentication and pattern generation feature.

## Project Structure

```
formulaq/
│── app/
│   ├── __init__.py          # Flask app factory
│   ├── auth.py              # Google OAuth logic
│   ├── routes.py            # Main routes
│   ├── utils.py             # Helper utilities
│   ├── config.py            # Configuration
│   └── static/
│       └── styles.css       # Stylesheet
│── templates/
│   ├── login.html           # Login page
│   ├── home.html            # Dashboard
│   └── pattern.html         # Pattern display
│── .env                     # Environment variables
│── requirements.txt         # Python dependencies
│── run.py                   # Application entry point
└── README.md
```

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Google OAuth:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing
   - Enable Google+ API
   - Create OAuth 2.0 credentials
   - Add authorized redirect URI: `http://localhost:5000/auth/callback`
   - Copy Client ID and Client Secret to `.env` file

3. **Update .env file:**
   ```
   GOOGLE_CLIENT_ID=your_actual_client_id
   GOOGLE_CLIENT_SECRET=your_actual_client_secret
   SECRET_KEY=generate_a_random_secret_key
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Access the app:**
   Open browser and go to `http://localhost:5000`

## Features

- ✅ Google OAuth authentication
- ✅ Display user name and email
- ✅ Show current IST time
- ✅ Pattern generation feature (max 100 lines)
- ✅ Secure session management

## Development Status

🚧 **Phase 1 (Skeleton):** Complete
⏳ **Phase 2 (OAuth Logic):** Pending
⏳ **Phase 3 (Pattern Logic):** Pending
