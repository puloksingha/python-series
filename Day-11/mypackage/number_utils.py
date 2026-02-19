"""
number_utils.py — Number manipulation utilities
"""

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if number is odd."""
    return n % 2 != 0

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
