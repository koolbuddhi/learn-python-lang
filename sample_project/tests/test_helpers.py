"""Tests for utility functions."""

import pytest
from datetime import datetime
from sample_project.utils.helpers import (
    generate_id,
    format_date,
    validate_email,
    sanitize_string
)

def test_generate_id():
    """Test ID generation."""
    id1 = generate_id()
    id2 = generate_id()
    assert isinstance(id1, str)
    assert len(id1) > 0
    assert id1 != id2  # IDs should be unique

def test_format_date():
    """Test date formatting."""
    date = datetime(2025, 1, 1, 12, 0, 0)
    formatted = format_date(date)
    assert formatted == "2025-01-01 12:00:00"

def test_validate_email():
    """Test email validation."""
    assert validate_email("test@example.com") is True
    assert validate_email("invalid.email") is False
    assert validate_email("test@.com") is False
    assert validate_email("@example.com") is False

def test_sanitize_string():
    """Test string sanitization."""
    assert sanitize_string("Hello, World!") == "Hello World"
    assert sanitize_string("Test@123") == "Test123"
    assert sanitize_string("My-Name_is.John") == "My-Name_is.John"
