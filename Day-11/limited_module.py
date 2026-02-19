"""
limited_module.py — Demonstrates __all__
"""

__all__ = ['greet', 'Calculator']  # Only these are exported

def greet(name):
    """Public function."""
    return f"Hello, {name}!"

def _helper():
    """Private helper (not in __all__)."""
    return "This is private"

class Calculator:
    """Public class."""
    def add(self, a, b):
        return a + b

class _InternalHelper:
    """Private class (not in __all__)."""
    pass
