# Package initialization file
# This file marks the directory as a Python package

"""
Sample Project
=============

A demonstration of proper Python project structure and organization.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import commonly used items for easier access
from .core.models import User, Product
from .utils.helpers import format_date, generate_id

# Define what should be imported with "from sample_project import *"
__all__ = ['User', 'Product', 'format_date', 'generate_id']

# Package-level configuration
DEBUG = False
API_VERSION = 'v1'

# You can also run initialization code here
def _initialize():
    """Initialize package settings and resources."""
    import logging
    logging.basicConfig(level=logging.INFO)

_initialize()
