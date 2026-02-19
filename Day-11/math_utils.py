"""
math_utils.py — Custom math utilities module
"""

# Module-level variable
PI = 3.14159

# Module-level function
def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Module-level class
class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
    
    def multiply(self, value):
        self.result *= value
        return self.result
    
    def reset(self):
        self.result = 0
        return self.result

# This runs only when module is executed directly
if __name__ == "__main__":
    print("Testing math_utils module...")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")
    print(f"factorial(5) = {factorial(5)}")
