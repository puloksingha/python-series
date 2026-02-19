"""
config.py — Application configuration
"""

# Database settings
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'myapp_db',
    'user': 'admin'
}

# API settings
API_KEY = 'your-api-key-here'
API_TIMEOUT = 30

# Feature flags
FEATURES = {
    'new_ui': True,
    'beta_features': False,
    'debug_mode': False
}

def get_database_url():
    """Build database URL."""
    return f"postgresql://{DATABASE['user']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['name']}"
