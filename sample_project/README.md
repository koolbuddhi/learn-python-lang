# Sample Project

This is a sample project demonstrating proper Python project structure and organization.

## Project Structure

```
sample_project/
│
├── setup.py           # Package configuration and dependencies
├── requirements.txt   # Development dependencies
├── README.md         # Project documentation
├── LICENSE           # Project license
│
├── sample_project/   # Main package directory
│   ├── __init__.py   # Package initialization
│   ├── __main__.py   # Entry point for running the package
│   ├── core/         # Core functionality
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── utils/        # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   │
│   └── api/          # API-related code
│       ├── __init__.py
│       └── endpoints.py
│
└── tests/            # Test directory
    ├── __init__.py
    ├── test_models.py
    └── test_helpers.py
```

## Installation

```bash
pip install -e .
```

## Usage

```python
from sample_project.core.models import User
from sample_project.utils.helpers import format_date

# Create a new user
user = User("John Doe", "john@example.com")

# Format current date
formatted_date = format_date()
```

## Development

1. Clone the repository
2. Install development dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Format code: `black .`
5. Type checking: `mypy .`
6. Lint code: `flake8`
