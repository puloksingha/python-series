# Day 03 - Variables and Operators in Python

## What are Variables?

A **variable** is a container that holds a value in memory. Think of it as a labeled box where you can store data that you want to use later in your program. Variables allow you to store, modify, and retrieve data throughout your code.

### Key Characteristics:
- Variables are created when you assign a value to them
- Variable names are case-sensitive (e.g., `name` and `Name` are different)
- Python is dynamically typed, so you don't need to declare the data type explicitly
- Variables can hold different types of data: integers, floats, strings, booleans, lists, tuples, etc.

### Variable Assignment

Variables are assigned values using the **assignment operator** (`=`). The variable name goes on the left, and the value goes on the right.

---

## Variable Naming Rules and Conventions

When creating variables in Python, you must follow certain rules:

### Rules (Must Follow):
1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
2. The rest of the name can contain letters, numbers, or underscores
3. Variable names are case-sensitive
4. Cannot use Python keywords (e.g., `if`, `for`, `while`, `class`, etc.)
5. Cannot contain spaces or special characters like !, @, #, $, %, etc.

### Conventions (Best Practices):
1. Use descriptive names that indicate the variable's purpose
2. Use lowercase letters with underscores for variable names (snake_case)
3. Avoid single-letter names except for counters or temporary variables
4. Constants should be in uppercase (e.g., `PI = 3.14159`)

### Examples:

```python
# Valid variable names
age = 25
first_name = "Alice"
total_count = 100
_private_var = "hidden"
user1 = "John"

# Invalid variable names
# 1st_name = "Bob"      # Cannot start with a number
# user-name = "Charlie" # Cannot contain hyphens
# for = 10              # Cannot use Python keywords
```

---

## Working with Variables

Variables can store different types of data and can be used to perform operations.

### Basic Variable Assignment:

```python
x = 10
y = 20
z = x + y
print(z)  # Output: 30
```

In this example:
- `x` is assigned the value `10`
- `y` is assigned the value `20`
- `z` is assigned the result of adding `x` and `y` (which is `30`)
- The `print()` function displays the value of `z`

### Variables with Different Data Types:

```python
name = "John"
age = 30
is_student = True

print(name)        # Output: John
print(age)         # Output: 30
print(is_student)  # Output: True
```

In this example:
- `name` is a **string** (text data)
- `age` is an **integer** (whole number)
- `is_student` is a **boolean** (True/False value)

---

## Collection Variables

Python allows you to store multiple values in a single variable using collections like **lists** and **tuples**.

### Lists

A **list** is an ordered, mutable (changeable) collection of items enclosed in square brackets `[]`.

```python
fruits = ["apple", "banana", "orange"]
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

### Tuples

A **tuple** is an ordered, immutable (unchangeable) collection of items enclosed in parentheses `()`.

```python
colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')
```

### Key Differences:
- **Lists** are mutable - you can change, add, or remove items after creation
- **Tuples** are immutable - once created, they cannot be modified

---

## Understanding Operators

**Operators** are special symbols that perform operations on variables and values. Python supports various types of operators that allow you to manipulate data and make decisions in your programs.

---

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

### List of Arithmetic Operators:

| Operator | Name           | Example | Result |
|----------|----------------|---------|--------|
| `+`      | Addition       | 5 + 3   | 8      |
| `-`      | Subtraction    | 5 - 3   | 2      |
| `*`      | Multiplication | 5 * 3   | 15     |
| `/`      | Division       | 5 / 2   | 2.5    |
| `%`      | Modulus        | 5 % 2   | 1      |
| `**`     | Exponentiation | 5 ** 2  | 25     |
| `//`     | Floor Division | 5 // 2  | 2      |

### Examples:

```python
a = 10
b = 5

print(a + b)   # Output: 15     (Addition)
print(a - b)   # Output: 5      (Subtraction)
print(a * b)   # Output: 50     (Multiplication)
print(a / b)   # Output: 2.0    (Division - always returns float)
print(a % b)   # Output: 0      (Modulus - remainder of division)
print(a ** b)  # Output: 100000 (Exponentiation - 10 to the power of 5)
```

### Special Notes:

**Division (`/`)**: Always returns a float, even if the result is a whole number.

```python
print(10 / 5)   # Output: 2.0 (not 2)
```

**Floor Division (`//`)**: Returns the quotient without the remainder (rounds down to nearest integer).

```python
print(7 // 2)   # Output: 3
print(7 / 2)    # Output: 3.5
```

**Modulus (`%`)**: Returns the remainder of the division.

```python
print(7 % 2)    # Output: 1 (7 divided by 2 has remainder 1)
print(10 % 3)   # Output: 1 (10 divided by 3 has remainder 1)
```

**Exponentiation (`**`)**: Raises the first number to the power of the second.

```python
print(2 ** 3)   # Output: 8  (2 × 2 × 2)
print(5 ** 2)   # Output: 25 (5 × 5)
```

---

## Comparison Operators

Comparison operators are used to compare two values. They return a **boolean** value (`True` or `False`).

### List of Comparison Operators:

| Operator | Name                     | Example | Result |
|----------|--------------------------|---------|--------|
| `==`     | Equal to                 | 5 == 5  | True   |
| `!=`     | Not equal to             | 5 != 3  | True   |
| `>`      | Greater than             | 5 > 3   | True   |
| `<`      | Less than                | 5 < 3   | False  |
| `>=`     | Greater than or equal to | 5 >= 5  | True   |
| `<=`     | Less than or equal to    | 5 <= 3  | False  |

### Examples:

```python
a = 10
b = 5

print(a == b)  # Output: False (10 is not equal to 5)
print(a != b)  # Output: True  (10 is not equal to 5)
print(a > b)   # Output: True  (10 is greater than 5)
print(a < b)   # Output: False (10 is not less than 5)
print(a >= b)  # Output: True  (10 is greater than or equal to 5)
print(a <= b)  # Output: False (10 is not less than or equal to 5)
```

### Important Notes:

- **`==`** checks for equality (value comparison)
- **`=`** is for assignment, not comparison
- Comparison operators are commonly used in conditional statements (if/else)

---

## Logical Operators

Logical operators are used to combine conditional statements and return boolean values.

### List of Logical Operators:

| Operator | Description                                      | Example        |
|----------|--------------------------------------------------|----------------|
| `and`    | Returns True if both statements are True         | x and y        |
| `or`     | Returns True if at least one statement is True   | x or y         |
| `not`    | Reverses the boolean value                       | not x          |

### Examples:

```python
x = True
y = False

print(x and y)  # Output: False (both must be True)
print(x or y)   # Output: True  (at least one is True)
print(not x)    # Output: False (reverses True to False)
print(not y)    # Output: True  (reverses False to True)
```

### Truth Tables:

**AND Operator (`and`)**:
- `True and True` = `True`
- `True and False` = `False`
- `False and True` = `False`
- `False and False` = `False`

**OR Operator (`or`)**:
- `True or True` = `True`
- `True or False` = `True`
- `False or True` = `True`
- `False or False` = `False`

**NOT Operator (`not`)**:
- `not True` = `False`
- `not False` = `True`

### Practical Examples:

```python
age = 25
has_license = True

# Check if person can drive (must be 18+ AND have license)
can_drive = age >= 18 and has_license
print(can_drive)  # Output: True

# Check if person is eligible for discount (senior OR student)
is_senior = age >= 65
is_student = True
gets_discount = is_senior or is_student
print(gets_discount)  # Output: True
```

---

## Assignment Operators

Assignment operators are used to assign values to variables. In addition to the basic assignment operator (`=`), Python provides compound assignment operators that combine arithmetic operations with assignment.

### List of Assignment Operators:

| Operator | Example   | Equivalent to |
|----------|-----------|---------------|
| `=`      | x = 5     | x = 5         |
| `+=`     | x += 3    | x = x + 3     |
| `-=`     | x -= 3    | x = x - 3     |
| `*=`     | x *= 3    | x = x * 3     |
| `/=`     | x /= 3    | x = x / 3     |
| `%=`     | x %= 3    | x = x % 3     |
| `**=`    | x **= 3   | x = x ** 3    |
| `//=`    | x //= 3   | x = x // 3    |

### Examples:

```python
x = 10

x += 5    # Same as: x = x + 5
print(x)  # Output: 15

x -= 3    # Same as: x = x - 3
print(x)  # Output: 12

x *= 2    # Same as: x = x * 2
print(x)  # Output: 24

x /= 4    # Same as: x = x / 4
print(x)  # Output: 6.0
```

---

## Summary

In this lesson, you learned about:

1. **Variables**: Containers that store data values
   - Naming rules and conventions
   - Dynamic typing in Python
   - Different types: int, float, str, bool, list, tuple

2. **Arithmetic Operators**: Perform mathematical operations
   - `+`, `-`, `*`, `/`, `%`, `**`, `//`

3. **Comparison Operators**: Compare values and return boolean results
   - `==`, `!=`, `>`, `<`, `>=`, `<=`

4. **Logical Operators**: Combine conditional statements
   - `and`, `or`, `not`

5. **Assignment Operators**: Assign and update variable values
   - `=`, `+=`, `-=`, `*=`, `/=`, etc.

Understanding variables and operators is fundamental to programming in Python, as they form the building blocks for more complex operations and logic in your programs.

---

## Practice Exercises

Try these exercises to reinforce your understanding:

1. Create variables to store your name, age, and favorite programming language. Print them out.

2. Calculate the area of a rectangle with length 15 and width 8 using variables and operators.

3. Write a program that calculates the remainder when 17 is divided by 5.

4. Use comparison operators to check if 25 is greater than or equal to 20.

5. Use logical operators to check if a number is between 10 and 20 (inclusive).

Happy coding! 🚀
