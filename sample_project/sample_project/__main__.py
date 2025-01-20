"""
This module allows running the package as a script:
python -m sample_project
"""

from .core.models import User
from .utils.helpers import format_date
from .api.endpoints import start_api_server

def main():
    """Main entry point for the application."""
    print(f"Starting Sample Project at {format_date()}")
    
    # Create a sample user
    user = User("Admin", "admin@example.com")
    print(f"Created user: {user}")
    
    # Start the API server
    start_api_server()

if __name__ == "__main__":
    main()
