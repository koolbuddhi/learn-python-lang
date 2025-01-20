"""Helper functions for the application."""

import uuid
from datetime import datetime
from typing import Optional

def generate_id() -> str:
    """Generate a unique identifier."""
    return str(uuid.uuid4())

def format_date(date: Optional[datetime] = None) -> str:
    """Format a date in a consistent way."""
    date = date or datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")

def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def sanitize_string(text: str) -> str:
    """Remove potentially dangerous characters from string."""
    return ''.join(char for char in text if char.isalnum() or char in ' -_.')
