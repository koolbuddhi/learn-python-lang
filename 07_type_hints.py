# Python Type Hints
# ===============

from typing import List, Dict, Tuple, Optional, Union, Any, Callable
from dataclasses import dataclass

# Basic Type Hints
# --------------
def greet(name: str) -> str:
    return f"Hello, {name}!"

age: int = 25
price: float = 19.99
is_active: bool = True

# Type hints with collections
# ------------------------
def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_user_info() -> Dict[str, Union[str, int]]:
    return {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

# Optional types
# ------------
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union types (multiple possible types)
# ---------------------------------
def process_data(data: Union[str, int, float]) -> str:
    return str(data)

# Type aliases
# ----------
Vector = List[float]
Matrix = List[Vector]

def scale_vector(vector: Vector, factor: float) -> Vector:
    return [x * factor for x in vector]

# Function type hints
# ----------------
CallbackFunc = Callable[[int, int], int]

def apply_operation(x: int, y: int, operation: CallbackFunc) -> int:
    return operation(x, y)

# Example callback functions
def add(x: int, y: int) -> int:
    return x + y

def multiply(x: int, y: int) -> int:
    return x * y

# Type hints with classes
# --------------------
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

# DataClasses with type hints
# ------------------------
@dataclass
class Person:
    name: str
    age: int
    email: Optional[str] = None

# Generic Types
# -----------
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        return self.items.pop() if self.items else None

# Example usage
def main() -> None:
    # Basic type hints
    message: str = greet("Alice")
    print(message)

    # List operations
    numbers: List[int] = [1, 2, 3, 4, 5]
    total: int = process_numbers(numbers)
    print(f"Sum: {total}")

    # Dictionary with type hints
    user_info: Dict[str, Union[str, int]] = get_user_info()
    print(f"User info: {user_info}")

    # Optional types
    user: Optional[str] = find_user(1)
    print(f"Found user: {user}")

    # Union types
    result: str = process_data(42)
    print(f"Processed data: {result}")

    # Function types
    result_add: int = apply_operation(5, 3, add)
    result_mult: int = apply_operation(5, 3, multiply)
    print(f"5 + 3 = {result_add}")
    print(f"5 * 3 = {result_mult}")

    # Classes with type hints
    point: Point = Point(3.0, 4.0)
    distance: float = point.distance_from_origin()
    print(f"Distance: {distance}")

    # DataClass
    person: Person = Person("John", 30, "john@example.com")
    print(f"Person: {person}")

    # Generic Stack
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")

if __name__ == "__main__":
    main()

# Practice Exercises:
# 1. Create a generic Queue class with type hints
# 2. Write a function that takes a Union of different collection types
# 3. Create a dataclass for a Book with appropriate type hints
# 4. Write a function that uses Callable with different type parameters
