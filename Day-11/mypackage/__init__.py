"""
mypackage — A demonstration package

This __init__.py file makes mypackage a package.
You can also use it to control what gets imported.
"""

# Package version
__version__ = "1.0.0"

# Import commonly used items to package level
from .string_utils import reverse_string, capitalize_words
from .number_utils import is_even, is_prime

# Define __all__ for "from mypackage import *"
__all__ = ['reverse_string', 'capitalize_words', 'is_even', 'is_prime']

# Package-level variable
PACKAGE_NAME = "mypackage"

def package_info():
    """Get package information."""
    return f"{PACKAGE_NAME} v{__version__}"
