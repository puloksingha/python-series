"""
utils.py — Common utility functions
"""

from datetime import datetime
import json

def current_timestamp():
    """Get current ISO timestamp."""
    return datetime.now().isoformat()

def save_json(data, filepath):
    """Save data as JSON."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filepath):
    """Load JSON data."""
    with open(filepath) as f:
        return json.load(f)

def format_size(bytes):
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"
