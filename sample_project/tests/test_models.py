"""Tests for the core models."""

import pytest
from sample_project.core.models import User, Product

def test_user_creation():
    """Test creating a new user."""
    user = User("Test User", "test@example.com")
    assert user.name == "Test User"
    assert user.email == "test@example.com"
    assert user.user_id is not None
    assert user.created_at is not None

def test_product_creation():
    """Test creating a new product."""
    product = Product("Test Product", 99.99, "A test product")
    assert product.name == "Test Product"
    assert product.price == 99.99
    assert product.description == "A test product"
    assert product.product_id is not None
    assert product.created_at is not None

def test_user_string_representation():
    """Test the string representation of a user."""
    user = User("Test User", "test@example.com")
    assert str(user) == "User(name=Test User, email=test@example.com)"

def test_product_string_representation():
    """Test the string representation of a product."""
    product = Product("Test Product", 99.99)
    assert str(product) == "Product(name=Test Product, price=$99.99)"
