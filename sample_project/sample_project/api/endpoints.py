"""API endpoints and server configuration."""

from dataclasses import dataclass
from typing import Optional
from ..core.models import User, Product

@dataclass
class APIConfig:
    """Configuration for the API server."""
    host: str = "localhost"
    port: int = 8000
    debug: bool = False
    api_key: Optional[str] = None

def start_api_server(config: Optional[APIConfig] = None) -> None:
    """Start the API server with the given configuration."""
    config = config or APIConfig()
    print(f"Starting API server on {config.host}:{config.port}")
    # In a real application, this would start an actual server
    
class UserAPI:
    """User-related API endpoints."""
    
    @staticmethod
    def create_user(name: str, email: str) -> User:
        """Create a new user."""
        user = User(name=name, email=email)
        # In a real application, save to database
        return user
    
    @staticmethod
    def get_user(user_id: str) -> Optional[User]:
        """Get user by ID."""
        # In a real application, fetch from database
        return None

class ProductAPI:
    """Product-related API endpoints."""
    
    @staticmethod
    def create_product(name: str, price: float, description: Optional[str] = None) -> Product:
        """Create a new product."""
        product = Product(name=name, price=price, description=description)
        # In a real application, save to database
        return product
    
    @staticmethod
    def get_product(product_id: str) -> Optional[Product]:
        """Get product by ID."""
        # In a real application, fetch from database
        return None
