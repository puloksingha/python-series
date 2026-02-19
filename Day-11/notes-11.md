# Day 11: Python Modules & Packages

## 📚 Table of Contents
1. [What are Modules?](#what-are-modules)
2. [Importing Built-in Modules](#importing-built-in-modules)
3. [Creating Your Own Modules](#creating-your-own-modules)
4. [The `__name__ == "__main__"` Pattern](#the-__name__--__main__-pattern)
5. [Module Search Path](#module-search-path)
6. [Creating Packages](#creating-packages)
7. [Importing from Packages](#importing-from-packages)
8. [Subpackages](#subpackages)
9. [Relative Imports](#relative-imports)
10. [The `__all__` Variable](#the-__all__-variable)
11. [Module Attributes](#module-attributes)
12. [Reloading Modules](#reloading-modules)
13. [Best Practices](#best-practices)
14. [Common Pitfalls](#common-pitfalls)

---

## What are Modules?

### Definition
- **Module**: A Python file (.py) containing functions, classes, and variables
- **Package**: A directory containing modules and a special `__init__.py` file

### Why Use Modules?
✓ **Code organization** — group related functionality  
✓ **Reusability** — import code from one file into another  
✓ **Namespace separation** — avoid naming conflicts  
✓ **Maintainability** — easier to manage large projects  

### Module Types
1. **Built-in modules** (part of Python): `os`, `sys`, `math`, `random`, etc.
2. **Third-party modules** (installed via pip): `requests`, `numpy`, `pandas`
3. **Your own modules** (custom .py files)

---

## Importing Built-in Modules

### Import Patterns

#### 1. Import Entire Module
```python
import math
print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
```

#### 2. Import Specific Items
```python
from math import sqrt, pi
print(pi)       # 3.141592653589793
print(sqrt(25)) # 5.0
```

#### 3. Import with Alias
```python
import datetime as dt
print(dt.datetime.now())

import numpy as np  # Common convention
import pandas as pd # Common convention
```

#### 4. Import All (⚠️ Not Recommended)
```python
from math import *
# Imports everything — pollutes namespace!
```

### Common Import Patterns
```python
import os                       # Import module
import os.path                  # Import submodule
from pathlib import Path        # Import specific class
from collections import Counter # Import specific class
from typing import List, Dict   # Type hints
```

---

## Creating Your Own Modules

### Example: math_utils.py
```python
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

# Module-level class
class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
```

### Using Your Module
```python
import math_utils

print(math_utils.PI)              # 3.14159
print(math_utils.add(10, 20))     # 30

calc = math_utils.Calculator()
calc.add(10)                       # 10
calc.multiply(5)                   # 50
```

---

## The `__name__ == "__main__"` Pattern

### Understanding `__name__`

Every Python module has a special variable: `__name__`

- When a file is **run directly**: `__name__ = "__main__"`
- When a file is **imported**: `__name__ = "module_name"`

### Common Pattern
```python
"""
script.py
"""

def greet(name):
    return f"Hello, {name}!"

def main():
    """Main function — only runs when executed directly."""
    print(greet("World"))
    print("Running main program!")

# This block only runs when script.py is executed directly
# NOT when script.py is imported as a module
if __name__ == "__main__":
    main()
```

### Why Use This Pattern?
✓ Makes your module both **importable** and **runnable**  
✓ Keeps test/demo code separate from reusable functions  
✓ Prevents code from running on import  

---

## Module Search Path

### Search Order
Python searches for modules in this order:
1. **Current directory**
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (third-party packages)

### Viewing Search Path
```python
import sys
print(sys.path)
```

### Adding Custom Paths
```python
import sys
sys.path.append('/custom/path')      # Add to end
sys.path.insert(0, '/priority/path') # Add to beginning
```

---

## Creating Packages

### Package Structure
```
mypackage/
    __init__.py          # Makes directory a package
    module1.py           # Module in package
    module2.py           # Another module
    subpackage/
        __init__.py      # Subpackage
        module3.py       # Module in subpackage
```

### Example: mypackage/__init__.py
```python
"""
mypackage — A demonstration package
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
```

### Example: mypackage/string_utils.py
```python
"""
string_utils.py — String manipulation utilities
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())
```

---

## Importing from Packages

### Import Patterns

#### 1. Import Entire Package
```python
import mypackage
print(mypackage.package_info())
print(mypackage.reverse_string('hello'))  # olleh
```

#### 2. Import Specific Module
```python
from mypackage import string_utils
print(string_utils.capitalize_words('hello world'))  # Hello World
```

#### 3. Import Specific Function
```python
from mypackage.number_utils import is_prime
print(is_prime(17))  # True
print(is_prime(20))  # False
```

#### 4. Import with Alias
```python
from mypackage import string_utils as su
print(su.reverse_string('Python'))  # nohtyP
```

---

## Subpackages

### Structure
```
mypackage/
    __init__.py
    string_utils.py
    number_utils.py
    math/                    # Subpackage
        __init__.py
        geometry.py
        algebra.py
```

### Example: mypackage/math/geometry.py
```python
"""
geometry.py — Geometric calculations
"""

import math

def circle_area(radius):
    """Calculate area of circle."""
    return math.pi * radius ** 2

def rectangle_area(width, height):
    """Calculate area of rectangle."""
    return width * height
```

### Importing from Subpackage
```python
from mypackage.math import geometry
print(geometry.circle_area(5))  # 78.54
```

---

## Relative Imports

### Syntax
Relative imports use dots (`.`) to refer to current/parent packages:

```python
from . import module          # Import from same package
from .. import module         # Import from parent package
from .subpkg import module    # Import from subpackage
```

### Example Inside mypackage/module.py
```python
"""
mypackage/module.py
"""

# Relative imports
from . import string_utils         # Same level
from . import number_utils         # Same level
from .math import geometry         # Subpackage

def demo():
    print(string_utils.reverse_string('Python'))
    print(number_utils.is_prime(7))
    print(geometry.circle_area(3))
```

### Rules
✓ Only work inside packages (not standalone scripts)  
✓ More maintainable when packages are moved/renamed  
✗ Cannot be used in scripts run directly  

---

## The `__all__` Variable

### Purpose
Defines what gets imported with `from module import *`

### Without `__all__`
```python
from module import *  # Imports everything (except private items)
```

### With `__all__`
```python
# mymodule.py
__all__ = ['public_func', 'PublicClass']

def public_func():
    """Will be imported with *"""
    pass

def _private_func():
    """Won't be imported with *"""
    pass

class PublicClass:
    """Will be imported with *"""
    pass
```

### Usage
```python
from mymodule import *
print(public_func())   # ✓ Available
print(PublicClass)     # ✓ Available
# print(_private_func()) # ✗ Not imported
```

### Best Practice
✓ Always define `__all__` in your modules  
✓ Documents your public API  
✓ Controls what users can import with `*`  

---

## Module Attributes

### Special Attributes

```python
import math_utils

print(math_utils.__name__)    # 'math_utils'
print(math_utils.__file__)    # '/path/to/math_utils.py'
print(math_utils.__doc__)     # Module docstring
```

### Inspecting Modules

#### Using `dir()`
```python
import math
print(dir(math))  # List all attributes and functions
```

#### Using `inspect` Module
```python
import inspect
import math_utils

# Get all functions
functions = [name for name, obj in inspect.getmembers(math_utils) 
             if inspect.isfunction(obj)]
print(functions)

# Get all classes
classes = [name for name, obj in inspect.getmembers(math_utils) 
           if inspect.isclass(obj)]
print(classes)
```

---

## Reloading Modules

### The Problem
Modules are cached after first import. Subsequent imports return the cached version.

### Solution: importlib.reload()
```python
import importlib
import mymodule

# Module is modified externally...

# Reload to get latest version
importlib.reload(mymodule)
```

### Caution
⚠️ Rarely needed in production  
⚠️ Useful in interactive development (Jupyter, REPL)  
⚠️ Existing references aren't updated automatically  

---

## Best Practices

### Module Organization
✓ One module per file, focused on single purpose  
✓ Use meaningful module names (`lowercase_with_underscores`)  
✓ Add docstrings to modules, functions, and classes  
✓ Group related modules into packages  

### Importing
✓ Put all imports at the top of file  
✓ Group imports: stdlib → third-party → local  
✓ Use absolute imports in applications  
✓ Use relative imports within packages  
✓ Avoid `from module import *` (except in `__init__.py`)  
✓ Use aliases for long module names  

### Import Grouping Example
```python
# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import numpy as np
import pandas as pd
import requests

# Local application imports
from mypackage import utils
from mypackage.models import User
```

### Naming Conventions
- **Modules**: `lowercase_with_underscores.py`
- **Packages**: `lowercase` (no underscores)
- **Private items**: `_leading_underscore`
- **Constants**: `UPPER_CASE`

### Project Structure
```
project/
    README.md
    setup.py
    requirements.txt
    mypackage/
        __init__.py
        module1.py
        module2.py
        subpackage/
            __init__.py
            module3.py
        tests/
            __init__.py
            test_module1.py
            test_module2.py
```

### Using `if __name__ == "__main__"`
✓ Always use this in scripts that can be imported  
✓ Put test/demo code in this block  
✓ Makes modules both importable and runnable  

### Defining `__all__`
✓ Define in every public module/package  
✓ Controls `from module import *`  
✓ Documents public API  

---

## Common Pitfalls

### ❌ Circular Imports
```python
# a.py
import b

# b.py  
import a  # ⚠️ Circular dependency!
```
**Solution**: Refactor to remove circular dependency or use lazy imports

### ❌ Modifying `sys.path` Incorrectly
```python
sys.path.append('../..')  # ⚠️ Fragile!
```
**Solution**: Use proper package structure or relative imports

### ❌ Shadowing Built-in Modules
```python
# ⚠️ Don't name your module 'random.py' or 'string.py'
```
**Solution**: Use unique, descriptive names

### ❌ Forgetting `__init__.py`
Python 3.3+ allows packages without `__init__.py`, but explicit is better.  
**Solution**: Always include `__init__.py` for clarity

### ❌ Relative Imports in Scripts
```python
# script.py
from . import utils  # ⚠️ Fails when running script directly
```
**Solution**: Use absolute imports in standalone scripts

### ❌ Not Using `if __name__ == "__main__"`
```python
# Code at module level runs on import
print("This runs every import!")  # ⚠️ Bad practice
```
**Solution**: Wrap executable code in `if __name__ == "__main__":`

---

## Practical Examples

### Configuration Module Pattern
```python
# config.py
"""Application configuration"""

DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'myapp_db',
    'user': 'admin'
}

API_KEY = 'your-api-key-here'
API_TIMEOUT = 30

FEATURES = {
    'new_ui': True,
    'beta_features': False,
    'debug_mode': False
}

def get_database_url():
    """Build database URL."""
    db = DATABASE
    return f"postgresql://{db['user']}@{db['host']}:{db['port']}/{db['name']}"
```

### Utilities Module Pattern
```python
# utils.py
"""Common utility functions"""

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
```

---

## Summary

### Key Takeaways
1. **Modules** organize code into reusable files
2. **Packages** organize modules into directories
3. Use `__name__ == "__main__"` to make scripts importable
4. Use `__init__.py` to define package behavior
5. Use `__all__` to control public API
6. Follow import conventions and grouping
7. Avoid circular imports and namespace pollution
8. Use relative imports within packages, absolute elsewhere

### Quick Reference

| Task | Syntax |
|------|--------|
| Import module | `import module` |
| Import with alias | `import module as alias` |
| Import specific item | `from module import item` |
| Import from package | `from package.module import item` |
| Relative import (same level) | `from . import module` |
| Relative import (parent) | `from .. import module` |
| Check if main script | `if __name__ == "__main__":` |
| Define public API | `__all__ = ['item1', 'item2']` |
| Reload module | `importlib.reload(module)` |

---

## Additional Resources

- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Packages Documentation](https://docs.python.org/3/tutorial/modules.html#packages)
- [PEP 8 – Import Conventions](https://pep8.org/#imports)
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/)

---

**Day 11 Complete!** 🎉

Next: Explore file handling, error handling, or advanced topics like decorators and context managers.
