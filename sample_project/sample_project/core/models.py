"""Data models for the application."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from ..utils.helpers import generate_id

@dataclass
class User:
    """Represents a user in the system."""
    name: str
    email: str
    user_id: str = None
    created_at: datetime = None
    
    def __post_init__(self):
        """Initialize computed fields after instance creation."""
        self.user_id = self.user_id or generate_id()
        self.created_at = self.created_at or datetime.now()
    
    def __str__(self) -> str:
        return f"User(name={self.name}, email={self.email})"

@dataclass
class Product:
    """Represents a product in the system."""
    name: str
    price: float
    description: Optional[str] = None
    product_id: str = None
    created_at: datetime = None
    
    def __post_init__(self):
        """Initialize computed fields after instance creation."""
        self.product_id = self.product_id or generate_id()
        self.created_at = self.created_at or datetime.now()
    
    def __str__(self) -> str:
        return f"Product(name={self.name}, price=${self.price})"
