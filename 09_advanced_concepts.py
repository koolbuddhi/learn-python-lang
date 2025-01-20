# Advanced Python Concepts
# =====================

from typing import Any, Callable, Generator, Iterator, TypeVar
from functools import wraps
import asyncio
from contextlib import contextmanager
from dataclasses import dataclass, field

# Decorators with Type Hints
# -----------------------
def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds to run")
        return result
    return wrapper

# Context Managers
# -------------
@contextmanager
def file_manager(filename: str, mode: str = 'r') -> Generator[Any, None, None]:
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Generators and Iterators
# ---------------------
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class CustomRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

# Property Decorators
# ----------------
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5/9

# Asynchronous Programming
# ---------------------
async def fetch_data(delay: float) -> str:
    await asyncio.sleep(delay)
    return f"Data fetched after {delay} seconds"

async def process_data() -> None:
    tasks = [
        fetch_data(1.0),
        fetch_data(2.0),
        fetch_data(3.0)
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Metaclasses
# ---------
class Singleton(type):
    _instances: Dict[Any, Any] = {}
    
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> None:
        self.connected = True

# Protocol (Structural Subtyping)
# ---------------------------
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

# Example Usage
@timer
def slow_function() -> None:
    import time
    time.sleep(1)

def main() -> None:
    # Using decorator
    slow_function()

    # Using context manager
    with file_manager("test.txt", 'w') as f:
        f.write("Hello, World!")

    # Using generator
    print("Fibonacci sequence:")
    for num in fibonacci(5):
        print(num)

    # Using iterator
    print("\nCustom range:")
    for num in CustomRange(1, 4):
        print(num)

    # Using properties
    temp = Temperature(25)
    print(f"\nTemperature in Celsius: {temp.celsius}")
    print(f"Temperature in Fahrenheit: {temp.fahrenheit}")
    temp.fahrenheit = 100
    print(f"New temperature in Celsius: {temp.celsius}")

    # Using async/await
    asyncio.run(process_data())

    # Using singleton
    db1 = Database()
    db2 = Database()
    print(f"\nSame database instance: {db1 is db2}")

    # Using protocol
    circle = Circle()
    square = Square()
    draw_shape(circle)
    draw_shape(square)

if __name__ == "__main__":
    main()

# Practice Exercises:
# 1. Create a decorator that caches function results
# 2. Implement a context manager for database connections
# 3. Write a generator that yields prime numbers
# 4. Create a metaclass that logs class instantiation
# 5. Implement an async function that simulates API calls
