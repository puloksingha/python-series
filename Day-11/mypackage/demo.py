"""
mypackage/demo.py — Demonstrates relative imports
"""

# Relative imports
from . import string_utils
from . import number_utils
from .math import geometry

def run_demo():
    """Demonstrate package functionality."""
    print("\n--- Relative Import Demo ---")
    print(f"Reverse 'Python': {string_utils.reverse_string('Python')}")
    print(f"Is 7 prime? {number_utils.is_prime(7)}")
    print(f"Circle area (r=3): {geometry.circle_area(3):.2f}")

if __name__ == "__main__":
    # Won't work if run directly (relative imports fail)
    # But works when imported
    run_demo()
