# Day 02 - Data Types in Python

## Introduction to Data Types

In Python, a **data type** is a classification of data that tells the compiler or interpreter how the programmer intends to use the data. Python supports various built-in data types that are essential for writing any program.

The main data types in Python are:
- **int** - Integer numbers
- **float** - Floating-point numbers
- **str** - Strings
- **bool** - Boolean values

---

## Integer (int)

An **integer** is a data type that represents whole numbers without any decimal point. Integers can be positive, negative, or zero.

### Characteristics:
- No decimal point
- Can be positive or negative
- Examples: -5, 0, 42, 1000

### Example:

```python
a = 10
print(a)      # Output: 10
print(type(a)) # Output: <class 'int'>
```

In this example, `a` is assigned the integer value `10`. When we print `a`, it outputs `10`. When we use the `type()` function, it confirms that the data type of `a` is `int`.

### More Examples:

```python
x = -5
y = 0
z = 100

print(x)  # Output: -5
print(y)  # Output: 0
print(z)  # Output: 100
```

---

## Float (float)

A **float** is a data type that represents decimal numbers or numbers with a fractional part. Floats are used when you need precision beyond whole numbers.

### Characteristics:
- Contains a decimal point
- Can represent very large or very small numbers using scientific notation
- Examples: 3.14, -2.5, 0.0, 1.23e-4

### Example:

```python
b = 3.14
print(b)       # Output: 3.14
print(type(b)) # Output: <class 'float'>
```

In this example, `b` is assigned the float value `3.14`. When we print `b`, it outputs `3.14`. When we use the `type()` function, it confirms that the data type of `b` is `float`.

### More Examples:

```python
pi = 3.14159
temperature = -10.5
percentage = 99.9

print(pi)         # Output: 3.14159
print(temperature) # Output: -10.5
print(percentage)  # Output: 99.9
```

### Scientific Notation:

```python
large_number = 1.5e10  # 1.5 × 10^10
small_number = 2.5e-3  # 2.5 × 10^-3

print(large_number)  # Output: 15000000000.0
print(small_number)  # Output: 0.0025
```

---

## String (str)

A **string** is a data type that represents a sequence of characters. Strings are used to store text data and are enclosed in either single quotes (`'`) or double quotes (`"`).

### Characteristics:
- Enclosed in single (`'`) or double (`"`) quotes
- Can contain letters, numbers, spaces, and special characters
- Examples: "Hello", 'World', "123", "Hello, World!"

### Example:

```python
c = "Hello, World!"
print(c)       # Output: Hello, World!
print(type(c)) # Output: <class 'str'>
```

In this example, `c` is assigned the string value `"Hello, World!"`. When we print `c`, it outputs `Hello, World!`. When we use the `type()` function, it confirms that the data type of `c` is `str`.

### More Examples:

```python
name = 'Alice'
message = "Welcome to Python programming"
number_as_string = "12345"

print(name)              # Output: Alice
print(message)           # Output: Welcome to Python programming
print(number_as_string)  # Output: 12345
```

### Single vs Double Quotes:

Both single and double quotes can be used interchangeably for strings. Choose one and be consistent:

```python
greeting1 = 'Hello'
greeting2 = "Hello"

print(greeting1)  # Output: Hello
print(greeting2)  # Output: Hello
```

### String with Quotes:

If your string contains a quote, use the opposite quote type or escape the quote:

```python
quote1 = "It's a beautiful day"
quote2 = 'He said "Hello"'
quote3 = "He said \"Hello\""

print(quote1)  # Output: It's a beautiful day
print(quote2)  # Output: He said "Hello"
print(quote3)  # Output: He said "Hello"
```

---

## Boolean (bool)

A **boolean** is a data type that can hold only two values: `True` or `False`. Booleans are commonly used in conditional statements and logical operations.

### Characteristics:
- Can only be `True` or `False`
- Case-sensitive (must be capitalized)
- Often result from comparison or logical operations
- Examples: `True`, `False`

### Example:

```python
d = True
print(d)       # Output: True
print(type(d)) # Output: <class 'bool'>
```

In this example, `d` is assigned the boolean value `True`. When we print `d`, it outputs `True`. When we use the `type()` function, it confirms that the data type of `d` is `bool`.

### More Examples:

```python
is_student = True
is_raining = False

print(is_student)  # Output: True
print(is_raining)  # Output: False
```

### Boolean from Comparisons:

Booleans are often the result of comparison operations:

```python
x = 10
y = 5

result1 = x > y    # True (10 is greater than 5)
result2 = x == y   # False (10 is not equal to 5)
result3 = x < y    # False (10 is not less than 5)

print(result1)     # Output: True
print(result2)     # Output: False
print(result3)     # Output: False
```

---

## Checking Data Types with type()

The **type()** function is a built-in function in Python that returns the data type of a variable or value. This is useful for understanding what kind of data you're working with.

### Syntax:

```python
type(object)
```

### Examples:

```python
a = 10
print(type(a))  # Output: <class 'int'>

b = 3.14
print(type(b))  # Output: <class 'float'>

c = "Hello, World!"
print(type(c))  # Output: <class 'str'>

d = True
print(type(d))  # Output: <class 'bool'>
```

### Practical Use:

```python
# Checking data types of different values
print(type(42))              # Output: <class 'int'>
print(type(3.14))            # Output: <class 'float'>
print(type("Python"))        # Output: <class 'str'>
print(type(True))            # Output: <class 'bool'>
print(type([1, 2, 3]))       # Output: <class 'list'> (for future reference)
```

---

## Summary of Day 02

Today we covered the four fundamental data types in Python:

| Data Type | Description | Example | type() Output |
|-----------|-------------|---------|----------|
| **int** | Whole numbers | `10`, `-5`, `0` | `<class 'int'>` |
| **float** | Numbers with decimals | `3.14`, `-2.5`, `1.5e10` | `<class 'float'>` |
| **str** | Text/characters | `"Hello"`, `'World'` | `<class 'str'>` |
| **bool** | True or False | `True`, `False` | `<class 'bool'>` |

### Key Takeaways:

1. **Data types** are classifications of data that tell Python how to interpret and use the data
2. **Integers** are whole numbers without decimal points
3. **Floats** are numbers with decimal points and higher precision
4. **Strings** are sequences of characters enclosed in quotes
5. **Booleans** are logical values that are either True or False
6. Use the **type()** function to determine the data type of any variable or value
7. Understanding data types is essential for writing correct and efficient Python programs

---

## Practice

Try creating variables of each data type and check their types:

```python
# Create variables of different types
my_int = 25
my_float = 99.99
my_string = "Learning Python"
my_bool = False

# Check their types
print(type(my_int))
print(type(my_float))
print(type(my_string))
print(type(my_bool))
```

These foundational concepts will be crucial as you progress to more complex Python programming!
