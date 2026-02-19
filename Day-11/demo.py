"""
demo.py — Demonstrates __name__ behavior
"""

def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"

def main():
    """Main function — only runs when executed directly."""
    print(f"__name__ in this module: {__name__}")
    print(greet("World"))
    print("This is the main function!")

# This block only runs when demo.py is executed directly
# NOT when demo.py is imported as a module
if __name__ == "__main__":
    print("\n--- Running demo.py directly ---")
    main()
