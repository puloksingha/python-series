"""
PYTHON MODULES & PACKAGES COMPREHENSIVE GUIDE
==============================================
Importing · Creating Modules · __name__ == "__main__" · Package Structure
"""

import sys
import os
from pathlib import Path

# ============================================================================
# 1. WHAT ARE MODULES?
# ============================================================================

print("=" * 70)
print("1. WHAT ARE MODULES?")
print("=" * 70)

explanation = """
A MODULE is a Python file (.py) containing functions, classes, and variables.
A PACKAGE is a directory containing modules and a special __init__.py file.

WHY USE MODULES?
  ✓ Code organization — group related functionality
  ✓ Reusability — import code from one file into another
  ✓ Namespace separation — avoid naming conflicts
  ✓ Maintainability — easier to manage large projects

MODULE TYPES:
  1. Built-in modules (part of Python): os, sys, math, random, etc.
  2. Third-party modules (installed via pip): requests, numpy, pandas
  3. Your own modules (custom .py files)
"""

print(explanation)


# ============================================================================
# 2. IMPORTING BUILT-IN MODULES
# ============================================================================

print("=" * 70)
print("2. IMPORTING BUILT-IN MODULES")
print("=" * 70)

# --- Import entire module ---
print("\n2a. Import entire module:")
print("    import math")

import math
print(f"    math.pi = {math.pi}")
print(f"    math.sqrt(16) = {math.sqrt(16)}")


# --- Import specific items ---
print("\n2b. Import specific items:")
print("    from math import sqrt, pi")

from math import sqrt, pi
print(f"    pi = {pi}")
print(f"    sqrt(25) = {sqrt(25)}")


# --- Import with alias ---
print("\n2c. Import with alias:")
print("    import datetime as dt")

import datetime as dt
print(f"    dt.datetime.now() = {dt.datetime.now()}")


# --- Import all (not recommended) ---
print("\n2d. Import all (AVOID in production):")
print("    from math import *")
print("    Imports everything — pollutes namespace!")


# --- Common import patterns ---
print("\n2e. Common patterns:")

patterns = """
    import os                       # Import module
    import os.path                  # Import submodule
    from pathlib import Path        # Import specific class
    from collections import Counter # Import specific class
    import numpy as np              # Common alias convention
    import pandas as pd             # Common alias convention
    from typing import List, Dict   # Type hints
"""
print(patterns)


# ============================================================================
# 3. CREATING YOUR OWN MODULES
# ============================================================================

print("=" * 70)
print("3. CREATING YOUR OWN MODULES")
print("=" * 70)

# Create a simple module
module_content = '''"""
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
'''

Path("math_utils.py").write_text(module_content)
print("\n✓ Created: math_utils.py")

# Now import and use it
print("\n3a. Using our custom module:")
print("    import math_utils")

import math_utils

print(f"    math_utils.PI = {math_utils.PI}")
print(f"    math_utils.add(10, 20) = {math_utils.add(10, 20)}")
print(f"    math_utils.factorial(5) = {math_utils.factorial(5)}")

calc = math_utils.Calculator()
print(f"    Calculator: {calc.add(10)} → {calc.multiply(5)}")


# --- Importing specific items ---
print("\n3b. Import specific items:")
print("    from math_utils import add, PI")

from math_utils import add as add_func, PI as pi_value

print(f"    add_func(15, 25) = {add_func(15, 25)}")
print(f"    pi_value = {pi_value}")


# ============================================================================
# 4. THE __name__ == "__main__" PATTERN
# ============================================================================

print("\n" + "=" * 70)
print("4. UNDERSTANDING __name__ == '__main__'")
print("=" * 70)

explanation_name = """
Every Python module has a special variable: __name__

When a file is run directly:        __name__ = "__main__"
When a file is imported:             __name__ = "module_name"

This allows code to behave differently based on how it's executed.

COMMON PATTERN:
    if __name__ == "__main__":
        # Code here runs only when file is executed directly
        # Not when imported
        main()
"""

print(explanation_name)

# Create a demonstration module
demo_module = '''"""
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
    print("\\n--- Running demo.py directly ---")
    main()
'''

Path("demo.py").write_text(demo_module)
print("\n✓ Created: demo.py")

print("\n4a. When we import demo.py:")
print("    import demo")
import demo

print(f"\n    demo.greet('Alice') = {demo.greet('Alice')}")
print("    (Notice: main() did NOT run automatically)")

print(f"\n4b. Current __name__ in this script:")
print(f"    __name__ = '{__name__}'")


# ============================================================================
# 5. MODULE SEARCH PATH
# ============================================================================

print("\n" + "=" * 70)
print("5. MODULE SEARCH PATH")
print("=" * 70)

print("\nPython searches for modules in this order:")
print("  1. Current directory")
print("  2. PYTHONPATH environment variable directories")
print("  3. Standard library directories")
print("  4. Site-packages (third-party packages)")

print("\n5a. sys.path (module search locations):")
for i, path in enumerate(sys.path[:5], 1):
    print(f"    {i}. {path}")
print("    ...")

print("\n5b. Adding custom paths:")
print("    sys.path.append('/custom/path')")
print("    sys.path.insert(0, '/priority/path')")


# ============================================================================
# 6. CREATING PACKAGES
# ============================================================================

print("\n" + "=" * 70)
print("6. CREATING PACKAGES")
print("=" * 70)

print("\n6a. Package structure:")

structure = """
mypackage/
    __init__.py          # Makes directory a package
    module1.py           # Module in package
    module2.py           # Another module
    subpackage/
        __init__.py      # Subpackage
        module3.py       # Module in subpackage
"""
print(structure)

# Create a package
package_dir = Path("mypackage")
package_dir.mkdir(exist_ok=True)

# Create __init__.py
init_content = '''"""
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
'''

(package_dir / "__init__.py").write_text(init_content)
print("✓ Created: mypackage/__init__.py")

# Create string_utils.py module
string_utils_content = '''"""
string_utils.py — String manipulation utilities
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def count_vowels(text):
    """Count vowels in text."""
    return sum(1 for c in text.lower() if c in 'aeiou')
'''

(package_dir / "string_utils.py").write_text(string_utils_content)
print("✓ Created: mypackage/string_utils.py")

# Create number_utils.py module
number_utils_content = '''"""
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
'''

(package_dir / "number_utils.py").write_text(number_utils_content)
print("✓ Created: mypackage/number_utils.py")


# ============================================================================
# 7. IMPORTING FROM PACKAGES
# ============================================================================

print("\n" + "=" * 70)
print("7. IMPORTING FROM PACKAGES")
print("=" * 70)

print("\n7a. Import entire package:")
print("    import mypackage")

import mypackage

print(f"    mypackage.package_info() = {mypackage.package_info()}")
print(f"    mypackage.__version__ = {mypackage.__version__}")

# Items imported in __init__.py are available
print(f"    mypackage.reverse_string('hello') = {mypackage.reverse_string('hello')}")


print("\n7b. Import specific module:")
print("    from mypackage import string_utils")

from mypackage import string_utils

print(f"    string_utils.capitalize_words('hello world') = {string_utils.capitalize_words('hello world')}")


print("\n7c. Import specific function:")
print("    from mypackage.number_utils import is_prime")

from mypackage.number_utils import is_prime

print(f"    is_prime(17) = {is_prime(17)}")
print(f"    is_prime(20) = {is_prime(20)}")


print("\n7d. Import with alias:")
print("    from mypackage import string_utils as su")

from mypackage import string_utils as su

print(f"    su.count_vowels('programming') = {su.count_vowels('programming')}")


# ============================================================================
# 8. SUBPACKAGES
# ============================================================================

print("\n" + "=" * 70)
print("8. SUBPACKAGES")
print("=" * 70)

# Create a subpackage
subpackage_dir = package_dir / "math"
subpackage_dir.mkdir(exist_ok=True)

# Subpackage __init__.py
(subpackage_dir / "__init__.py").write_text('"""Math utilities subpackage."""\n')

# geometry.py in subpackage
geometry_content = '''"""
geometry.py — Geometric calculations
"""

import math

def circle_area(radius):
    """Calculate area of circle."""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of circle."""
    return 2 * math.pi * radius

def rectangle_area(width, height):
    """Calculate area of rectangle."""
    return width * height
'''

(subpackage_dir / "geometry.py").write_text(geometry_content)
print("✓ Created: mypackage/math/geometry.py")

print("\n8a. Importing from subpackage:")
print("    from mypackage.math import geometry")

from mypackage.math import geometry

print(f"    geometry.circle_area(5) = {geometry.circle_area(5):.2f}")


# ============================================================================
# 9. RELATIVE IMPORTS
# ============================================================================

print("\n" + "=" * 70)
print("9. RELATIVE IMPORTS")
print("=" * 70)

explanation_relative = """
Relative imports use dots (.) to refer to current/parent packages:

    from . import module          # Import from same package
    from .. import module         # Import from parent package
    from .subpkg import module    # Import from subpackage

EXAMPLE inside mypackage/string_utils.py:
    from . import number_utils         # Same level
    from .math import geometry         # Subpackage

RULES:
    ✓ Only work inside packages (not standalone scripts)
    ✓ More maintainable when packages are moved/renamed
    ✗ Cannot be used in scripts run directly (use absolute imports)
"""

print(explanation_relative)

# Demonstrate with a new module that uses relative imports
relative_demo = '''"""
mypackage/demo.py — Demonstrates relative imports
"""

# Relative imports
from . import string_utils
from . import number_utils
from .math import geometry

def run_demo():
    """Demonstrate package functionality."""
    print("\\n--- Relative Import Demo ---")
    print(f"Reverse 'Python': {string_utils.reverse_string('Python')}")
    print(f"Is 7 prime? {number_utils.is_prime(7)}")
    print(f"Circle area (r=3): {geometry.circle_area(3):.2f}")

if __name__ == "__main__":
    # Won't work if run directly (relative imports fail)
    # But works when imported
    run_demo()
'''

(package_dir / "demo.py").write_text(relative_demo)
print("✓ Created: mypackage/demo.py (with relative imports)")

from mypackage.demo import run_demo
run_demo()


# ============================================================================
# 10. __all__ VARIABLE
# ============================================================================

print("\n" + "=" * 70)
print("10. THE __all__ VARIABLE")
print("=" * 70)

explanation_all = """
__all__ defines what gets imported with "from module import *"

Without __all__:
    from module import *    → imports everything (not private)

With __all__:
    __all__ = ['func1', 'func2', 'Class1']
    from module import *    → imports only listed items

EXAMPLE:
    # mymodule.py
    __all__ = ['public_func', 'PublicClass']
    
    def public_func(): pass
    def _private_func(): pass     # Not in __all__
    class PublicClass: pass

Best practice: Always define __all__ in your modules
"""

print(explanation_all)

# Demonstrate
all_demo_module = '''"""
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
'''

Path("limited_module.py").write_text(all_demo_module)
print("✓ Created: limited_module.py")

print("\n10a. Using __all__:")
print("    from limited_module import *")
from limited_module import *

print(f"    greet('Alice') = {greet('Alice')}")
print(f"    Calculator available: {Calculator}")
# print(_helper())  # Would fail - not imported


# ============================================================================
# 11. MODULE ATTRIBUTES
# ============================================================================

print("\n" + "=" * 70)
print("11. MODULE ATTRIBUTES")
print("=" * 70)

print("\n11a. Special module attributes:")

import math_utils as mu

print(f"    __name__:     {mu.__name__}")
print(f"    __file__:     {mu.__file__}")
print(f"    __doc__:      {mu.__doc__[:50]}...")

print("\n11b. dir() — list module contents:")
contents = dir(mu)
print(f"    dir(math_utils): {contents[:8]}...")

print("\n11c. Inspect module functions:")
import inspect

functions = [name for name, obj in inspect.getmembers(mu) if inspect.isfunction(obj)]
print(f"    Functions: {functions}")


# ============================================================================
# 12. RELOADING MODULES
# ============================================================================

print("\n" + "=" * 70)
print("12. RELOADING MODULES")
print("=" * 70)

explanation_reload = """
Modules are cached after first import.
Subsequent imports return the cached version.

To reload a modified module:
    import importlib
    importlib.reload(module)

CAUTION:
    - Rarely needed in production
    - Useful in interactive development (Jupyter, REPL)
    - Existing references aren't updated
"""

print(explanation_reload)

print("\n12a. Demonstration:")
import importlib

# Modify the module
original = Path("math_utils.py").read_text()
modified = original.replace("PI = 3.14159", "PI = 3.14159265359")
Path("math_utils.py").write_text(modified)

# Reload
importlib.reload(math_utils)
print(f"    After reload: math_utils.PI = {math_utils.PI}")

# Restore original
Path("math_utils.py").write_text(original)


# ============================================================================
# 13. PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 70)
print("13. PRACTICAL EXAMPLES")
print("=" * 70)

print("\n13a. Config module pattern:")

config_content = '''"""
config.py — Application configuration
"""

# Database settings
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'myapp_db',
    'user': 'admin'
}

# API settings
API_KEY = 'your-api-key-here'
API_TIMEOUT = 30

# Feature flags
FEATURES = {
    'new_ui': True,
    'beta_features': False,
    'debug_mode': False
}

def get_database_url():
    """Build database URL."""
    return f"postgresql://{DATABASE['user']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['name']}"
'''

Path("config.py").write_text(config_content)
print("✓ Created: config.py")

import config

print(f"    Database host: {config.DATABASE['host']}")
print(f"    DB URL: {config.get_database_url()}")


print("\n13b. Utils module pattern:")

utils_content = '''"""
utils.py — Common utility functions
"""

from datetime import datetime
import json

def current_timestamp():
    """Get current ISO timestamp."""
    return datetime.now().isoformat()

def save_json(data, filepath):
    """Save data as JSON."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filepath):
    """Load JSON data."""
    with open(filepath) as f:
        return json.load(f)

def format_size(bytes):
    """Format bytes as human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"
'''

Path("utils.py").write_text(utils_content)
print("✓ Created: utils.py")

import utils

print(f"    Timestamp: {utils.current_timestamp()}")
print(f"    Size format: {utils.format_size(1536000)}")


# ============================================================================
# 14. BEST PRACTICES
# ============================================================================

print("\n" + "=" * 70)
print("14. BEST PRACTICES")
print("=" * 70)

best_practices = """
MODULE ORGANIZATION:
  ✓ One module per file, focused on single purpose
  ✓ Use meaningful module names (lowercase, underscores)
  ✓ Add docstrings to modules, functions, and classes
  ✓ Group related modules into packages

IMPORTING:
  ✓ Put all imports at the top of file
  ✓ Group imports: stdlib, third-party, local
  ✓ Use absolute imports in applications
  ✓ Use relative imports within packages
  ✓ Avoid "from module import *" (except in __init__.py)
  ✓ Use aliases for long module names

NAMING:
  ✓ Modules: lowercase_with_underscores
  ✓ Packages: lowercase (no underscores)
  ✓ Private items: _leading_underscore
  ✓ Constants: UPPER_CASE

STRUCTURE:
  project/
      README.md
      setup.py
      requirements.txt
      mypackage/
          __init__.py
          module1.py
          module2.py
          tests/
              __init__.py
              test_module1.py
              test_module2.py

IF __name__ == "__main__":
  ✓ Always use this in scripts that can be imported
  ✓ Put test/demo code in this block
  ✓ Makes modules both importable and runnable

__all__:
  ✓ Define in every public module/package
  ✓ Controls "from module import *"
  ✓ Documents public API
"""

print(best_practices)


# ============================================================================
# 15. COMMON PITFALLS
# ============================================================================

print("\n" + "=" * 70)
print("15. COMMON PITFALLS")
print("=" * 70)

pitfalls = """
❌ CIRCULAR IMPORTS:
    # a.py
    import b
    
    # b.py  
    import a    # Circular dependency!
    
    Solution: Refactor to remove circular dependency or use lazy imports

❌ MODIFYING sys.path INCORRECTLY:
    sys.path.append('../..')  # Fragile!
    
    Solution: Use proper package structure or relative imports

❌ SHADOWING BUILT-IN MODULES:
    # Don't name your module 'random.py' or 'string.py'
    
    Solution: Use unique, descriptive names

❌ FORGETTING __init__.py:
    Python 3.3+ allows packages without __init__.py (namespace packages)
    But explicit is better — always include __init__.py

❌ RELATIVE IMPORTS IN SCRIPTS:
    # script.py
    from . import utils  # Fails when running script directly
    
    Solution: Use absolute imports in standalone scripts

❌ NOT USING if __name__ == "__main__":
    # Code at module level runs on import
    
    Solution: Wrap executable code in if __name__ == "__main__":
"""

print(pitfalls)


# ============================================================================
# 16. CLEANUP
# ============================================================================

print("\n" + "=" * 70)
print("16. CLEANUP")
print("=" * 70)

# Clean up created files
import shutil

cleanup_items = [
    "math_utils.py",
    "demo.py",
    "mypackage",
    "limited_module.py",
    "config.py",
    "utils.py",
    "__pycache__"
]

removed = 0
for item in cleanup_items:
    path = Path(item)
    if path.is_dir():
        shutil.rmtree(path)
        removed += 1
    elif path.exists():
        path.unlink()
        removed += 1

print(f"\n✓ Cleaned up {removed} files/directories")

print("\n" + "=" * 70)
print("END OF MODULES & PACKAGES GUIDE")
print("=" * 70)