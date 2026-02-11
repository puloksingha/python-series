# Python Functions Comprehensive Guide

Everything you need to know about functions in Python

---

## 1. Defining Functions

### Basic Function Definition

```python
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Function with a Parameter

```python
def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!
```

### Function with Multiple Parameters

```python
def add_numbers(a, b):
    """Adds two numbers together."""
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(5, 3)  # Output: The sum of 5 and 3 is 8
```

---

## 2. Return Values

### Function that Returns a Value

```python
def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

result = multiply(4, 7)
print(f"4 × 7 = {result}")  # Output: 4 × 7 = 28
```

### Function Returning Multiple Values (as a tuple)

```python
def calculate(a, b):
    """Returns sum, difference, product, and quotient of two numbers."""
    return a + b, a - b, a * b, a / b

sum_result, diff, prod, quot = calculate(10, 2)
print(f"Sum: {sum_result}, Difference: {diff}, Product: {prod}, Quotient: {quot}")
```

### Early Return

```python
def check_positive(number):
    """Checks if a number is positive."""
    if number <= 0:
        return False  # Early exit
    return True

print(check_positive(5))   # Output: True
print(check_positive(-3))  # Output: False
```

### Function with No Explicit Return (returns None)

```python
def print_message(msg):
    """Prints a message but doesn't return anything."""
    print(msg)

result = print_message("Testing")  # Prints: Testing
print(f"Return value: {result}")   # Output: Return value: None
```

---

## 3. Parameters - Different Types

### Positional Parameters

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")  # Order matters!
```

### Keyword Arguments

```python
def describe_pet_v2(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet_v2(pet_name="Whiskers", animal_type="cat")  # Order doesn't matter
```

### Default Parameters

```python
def greet_with_time(name, time_of_day="morning"):
    """Greets someone with a time of day."""
    print(f"Good {time_of_day}, {name}!")

greet_with_time("Bob")                    # Output: Good morning, Bob!
greet_with_time("Sarah", "evening")       # Output: Good evening, Sarah!
```

### *args (Variable Positional Arguments)

```python
def sum_all(*numbers):
    """Sums all numbers passed to the function."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # Output: 6
print(sum_all(10, 20, 30, 40))    # Output: 100
```

### **kwargs (Variable Keyword Arguments)

```python
def print_user_info(**user_data):
    """Prints user information from keyword arguments."""
    for key, value in user_data.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

### Combining Different Parameter Types

```python
def complex_function(pos1, pos2, *args, default_param="default", **kwargs):
    """Demonstrates all parameter types together."""
    print(f"Positional 1: {pos1}")
    print(f"Positional 2: {pos2}")
    print(f"Additional positional args: {args}")
    print(f"Default parameter: {default_param}")
    print(f"Keyword arguments: {kwargs}")

complex_function(1, 2, 3, 4, 5, default_param="custom", key1="value1", key2="value2")
```

---

## 4. Scope - Understanding Variable Scope

### Global Scope

```python
global_var = "I'm global"

def access_global():
    """Can access global variables."""
    print(global_var)

access_global()  # Output: I'm global
```

### Local Scope

```python
def local_scope_demo():
    """Variables defined here are local."""
    local_var = "I'm local"
    print(local_var)

local_scope_demo()  # Output: I'm local
# print(local_var)  # This would raise NameError: local_var is not defined
```

### Modifying Global Variables

```python
counter = 0

def increment_counter():
    """Modifies a global variable using the global keyword."""
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_counter()  # Output: Counter: 1
increment_counter()  # Output: Counter: 2
```

### Enclosing Scope (Nested Functions)

```python
def outer_function():
    """Demonstrates enclosing scope."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Nested function can access outer function's variables."""
        print(outer_var)
    
    inner_function()

outer_function()  # Output: I'm in outer function
```

### The nonlocal Keyword

```python
def outer_with_nonlocal():
    """Demonstrates the nonlocal keyword."""
    count = 0
    
    def increment():
        nonlocal count  # Refers to count in outer function
        count += 1
        print(f"Count: {count}")
    
    increment()  # Output: Count: 1
    increment()  # Output: Count: 2
    print(f"Final count: {count}")  # Output: Final count: 2

outer_with_nonlocal()
```

### LEGB Rule (Local, Enclosing, Global, Built-in)

```python
x = "global x"

def test_scope():
    """Demonstrates LEGB rule."""
    x = "local x"
    
    def inner():
        x = "inner x"
        print(f"Inner: {x}")  # Uses local x in inner()
    
    inner()
    print(f"Outer: {x}")  # Uses local x in test_scope()

test_scope()
print(f"Global: {x}")  # Uses global x
```

---

## 5. Lambda Functions (Anonymous Functions)

### Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25
```

### Lambda with Multiple Parameters

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12
```

### Lambda in Sorting

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade using lambda
sorted_students = sorted(students, key=lambda student: student["grade"])
print("Sorted by grade:")
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")
```

### Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")  # Output: [1, 4, 9, 16, 25]
```

### Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4, 6, 8, 10]
```

### Lambda with reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_all}")  # Output: Sum: 15
```

### When NOT to Use Lambda

```python
# BAD: Complex logic in lambda
# complicated = lambda x: x if x > 0 else -x if x < -10 else 0

# GOOD: Use regular function for complex logic
def process_number(x):
    """Better readability for complex logic."""
    if x > 0:
        return x
    elif x < -10:
        return -x
    else:
        return 0
```

---

## 6. Practical Examples

### Example 1: Calculator with Functions

```python
def calculator(operation, a, b):
    """A simple calculator function."""
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    
    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Invalid operation"

print(calculator('add', 10, 5))       # Output: 15
print(calculator('multiply', 4, 7))   # Output: 28
```

### Example 2: Function with Validation

```python
def create_user(username, email, age=None):
    """Creates a user with validation."""
    if not username or len(username) < 3:
        return "Username must be at least 3 characters"
    
    if '@' not in email:
        return "Invalid email address"
    
    if age is not None and age < 0:
        return "Age cannot be negative"
    
    user = {
        'username': username,
        'email': email,
        'age': age
    }
    
    return f"User created: {user}"

print(create_user("john_doe", "john@example.com", 25))
```

### Example 3: Recursive Function

```python
def factorial(n):
    """Calculates factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")  # Output: 120
```

### Example 4: Function Returning Function (Closure)

```python
def make_multiplier(factor):
    """Returns a function that multiplies by a factor."""
    def multiply(number):
        return number * factor
    return multiply

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(times_three(10))  # Output: 30
print(times_five(10))   # Output: 50
```

---

## 7. Best Practices & Tips

### Best Practices

1. **Use descriptive function names (use verbs)**
   - ✓ `calculate_average()`  ✗ `avg()`
   - ✓ `get_user_data()`      ✗ `gud()`

2. **Keep functions small and focused** (do one thing well)

3. **Use docstrings** to document what your function does

4. **Return values instead of printing** when possible (makes functions more reusable)

5. **Use default parameters wisely**

6. **Avoid modifying global variables** (use return values)

7. **Lambda functions should be simple** (one-liners)

8. **Use type hints** for better code clarity (Python 3.5+):
   ```python
   def add(a: int, b: int) -> int:
       return a + b
   ```

9. **Follow DRY principle** (Don't Repeat Yourself)
   - If you're writing similar code multiple times, make it a function

10. **Test your functions** with different inputs

### Example with Type Hints

```python
def greet_typed(name: str, age: int) -> str:
    """Type-hinted function for better code clarity."""
    return f"Hello, {name}! You are {age} years old."

print(greet_typed("Alice", 30))
```

---

## Practice Exercises

1. Write a function that takes a list of numbers and returns the average.

2. Create a function that checks if a string is a palindrome.

3. Write a function that takes a temperature in Celsius and converts it to Fahrenheit.

4. Create a function that accepts any number of arguments and returns the largest one.

5. Write a function that takes a sentence and returns the word count.

6. Create a lambda function that checks if a number is even.

7. Write a function that generates a list of Fibonacci numbers up to n terms.

8. Create a function that takes a list and returns a new list with duplicates removed.

9. Write a recursive function to calculate the sum of digits of a number.

10. Create a higher-order function that takes a function and a list, applying the function to each element.

---

**End of Python Functions Guide**