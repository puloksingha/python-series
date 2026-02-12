# Day-07
# Python Data Structures



Comprehensive guide to Lists, Tuples, Dictionaries, and Sets

---

## 1. Lists

### Overview
- **Ordered**: Elements maintain their insertion order
- **Mutable**: Can be modified after creation
- **Allow Duplicates**: Can contain duplicate values
- **Syntax**: `[]` or `list()`

### Creating Lists

```python
# Empty list
empty_list = []
empty_list_alt = list()

# List with values
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]  # Different types allowed
```

### Accessing Elements

```python
fruits = ["apple", "banana", "cherry"]

fruits[0]      # "apple" (first element)
fruits[-1]     # "cherry" (last element)
fruits[1:3]    # ["banana", "cherry"] (slicing)
```

### Common List Methods

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add item to end | `fruits.append("date")` |
| `insert(i, x)` | Insert at index | `fruits.insert(1, "avocado")` |
| `extend(list)` | Add multiple items | `fruits.extend(["fig", "grape"])` |
| `remove(x)` | Remove first occurrence | `fruits.remove("banana")` |
| `pop(i)` | Remove and return item | `fruits.pop()` or `fruits.pop(1)` |
| `sort()` | Sort in place | `numbers.sort()` |
| `reverse()` | Reverse in place | `fruits.reverse()` |
| `index(x)` | Find index of value | `fruits.index("apple")` |
| `count(x)` | Count occurrences | `numbers.count(2)` |
| `clear()` | Remove all items | `fruits.clear()` |

### List Comprehensions

```python
# Basic comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Transform strings
uppercase = [word.upper() for word in ["hello", "world"]]

# Nested comprehension
flattened = [num for row in matrix for num in row]
```

### When to Use Lists
✓ Need ordered collection  
✓ Need to modify elements  
✓ Need to allow duplicates  
✓ Need indexing and slicing  
✓ Order matters  

✗ Need fast membership testing (use set)  
✗ Need to prevent modification (use tuple)  

---

## 2. Tuples

### Overview
- **Ordered**: Elements maintain their order
- **Immutable**: Cannot be modified after creation
- **Allow Duplicates**: Can contain duplicate values
- **Syntax**: `()` or `tuple()`

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()

# Tuple with values
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Single element tuple (comma required!)
single = (42,)
not_a_tuple = (42)  # This is just an int
```

### Tuple Packing and Unpacking

```python
# Packing
person = "Alice", 25, "Engineer"

# Unpacking
name, age, profession = person

# Swap variables
a, b = 10, 20
a, b = b, a  # Now a=20, b=10

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

### Tuple Methods

| Method | Description | Example |
|--------|-------------|---------|
| `count(x)` | Count occurrences | `numbers.count(2)` |
| `index(x)` | Find index of value | `colors.index("red")` |

### When to Use Tuples
✓ Data should not change (immutable)  
✓ Returning multiple values from function  
✓ Dictionary keys (tuples are hashable)  
✓ Slightly faster than lists  
✓ Protect data from modification  

✗ Need to modify contents (use list)  

---

## 3. Dictionaries

### Overview
- **Key-Value Pairs**: Store data as key-value associations
- **Ordered**: Maintain insertion order (Python 3.7+)
- **Mutable**: Can be modified
- **No Duplicate Keys**: Keys must be unique
- **Syntax**: `{}` or `dict()`

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}

# Dictionary with values
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "CS"]
}

# Using dict() constructor
person = dict(name="Bob", age=25, city="New York")
```

### Accessing and Modifying

```python
# Access values
student["name"]              # "Alice"
student.get("grade")         # "A"
student.get("gpa", 0.0)      # 0.0 (default if key doesn't exist)

# Add/modify values
student["gpa"] = 3.8         # Add new key-value
student["age"] = 21          # Modify existing

# Update multiple values
student.update({"semester": 3, "major": "CS"})
```

### Common Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `get(key, default)` | Get value with default | `d.get("age", 0)` |
| `keys()` | Get all keys | `student.keys()` |
| `values()` | Get all values | `student.values()` |
| `items()` | Get key-value pairs | `student.items()` |
| `pop(key)` | Remove and return value | `student.pop("age")` |
| `popitem()` | Remove last item | `student.popitem()` |
| `update(dict)` | Update with another dict | `d.update({...})` |
| `clear()` | Remove all items | `student.clear()` |

### Dictionary Comprehensions

```python
# Create from list
squares = {x: x**2 for x in range(5)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Transform existing dict
prices = {"apple": 0.5, "banana": 0.3}
discounted = {item: price * 0.9 for item, price in prices.items()}
```

### Iterating Through Dictionaries

```python
car = {"brand": "Toyota", "model": "Camry", "year": 2022}

# Iterate over keys
for key in car:
    print(key)

# Iterate over values
for value in car.values():
    print(value)

# Iterate over key-value pairs
for key, value in car.items():
    print(f"{key}: {value}")
```

### When to Use Dictionaries
✓ Need key-value associations  
✓ Need fast lookups by key  
✓ Keys are meaningful labels  
✓ Storing configuration settings  
✓ JSON-like data structures  

✗ Need ordered sequence (use list)  
✗ Need duplicate keys (not possible)  

---

## 4. Sets

### Overview
- **Unordered**: No guaranteed order
- **Mutable**: Can add/remove elements
- **No Duplicates**: Automatically removes duplicates
- **Syntax**: `{}` or `set()`

### Creating Sets

```python
# Empty set (must use set(), not {})
empty_set = set()  # {} creates empty dict!

# Set with values
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From list (removes duplicates)
unique = set([1, 2, 2, 3, 3, 3, 4])  # {1, 2, 3, 4}
```

### Common Set Methods

| Method | Description | Example |
|--------|-------------|---------|
| `add(x)` | Add single element | `colors.add("yellow")` |
| `update(iterable)` | Add multiple elements | `colors.update(["red", "blue"])` |
| `remove(x)` | Remove (raises error if missing) | `colors.remove("red")` |
| `discard(x)` | Remove (no error if missing) | `colors.discard("black")` |
| `pop()` | Remove random element | `colors.pop()` |
| `clear()` | Remove all elements | `colors.clear()` |

### Set Operations (Mathematical)

```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (all elements from both)
union = set_a | set_b              # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (common elements)
intersection = set_a & set_b        # {4, 5}

# Difference (in A but not B)
difference = set_a - set_b          # {1, 2, 3}

# Symmetric difference (in A or B but not both)
sym_diff = set_a ^ set_b            # {1, 2, 3, 6, 7, 8}

# Subset/superset checks
{1, 2}.issubset(set_a)              # True
set_a.issuperset({1, 2})            # True
set_a.isdisjoint({10, 11})          # True
```

### Set Comprehensions

```python
# Basic comprehension
squares = {x**2 for x in range(10)}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
```

### Frozen Sets (Immutable)

```python
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)  # Error! Immutable

# Can be used as dict keys
dict_with_set_key = {frozen: "value"}
```

### When to Use Sets
✓ Need to remove duplicates  
✓ Need fast membership testing  
✓ Need mathematical set operations  
✓ Order doesn't matter  
✓ Need unique elements only  

✗ Need to maintain order (use list)  
✗ Need to access by index (use list)  

---

## 5. Comparison Chart

| Feature | List | Tuple | Dictionary | Set |
|---------|------|-------|------------|-----|
| **Ordered** | Yes | Yes | Yes (3.7+) | No |
| **Mutable** | Yes | No | Yes | Yes |
| **Duplicates** | Yes | Yes | Keys: No | No |
| **Indexed** | Yes | Yes | By key | No |
| **Syntax** | `[]` | `()` | `{}` | `{}` |
| **Fast lookup** | No | No | Yes | Yes |
| **Use for** | Ordered items | Fixed data | Key-value pairs | Unique items |

---

## 6. Performance Comparison

| Operation | List | Tuple | Dict | Set |
|-----------|------|-------|------|-----|
| Access by index/key | O(1) | O(1) | O(1) | N/A |
| Search (membership) | O(n) | O(n) | O(1) | O(1) |
| Insert/Delete | O(n) | N/A | O(1) | O(1) |
| Append | O(1) | N/A | O(1) | O(1) |
| Memory usage | Medium | Low | High | Medium |

**Notes:**
- **Lists**: Good for ordered collections, slower for searching
- **Tuples**: Faster than lists, immutable, less memory
- **Dicts**: Fast lookups, higher memory usage
- **Sets**: Fast membership testing, no duplicates

---

## 7. Real-World Examples

### Shopping Cart (List)
```python
shopping_cart = [
    {"item": "Apple", "quantity": 3, "price": 0.5},
    {"item": "Bread", "quantity": 1, "price": 2.0},
    {"item": "Milk", "quantity": 2, "price": 1.5}
]
total = sum(item["quantity"] * item["price"] for item in shopping_cart)
```

### Geographic Coordinates (Tuple)
```python
locations = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6762, 139.6503)
}
```

### User Profile (Dictionary)
```python
user_profile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 28,
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}
```

### Unique Visitors (Set)
```python
website_visitors = set()
visits = ["user1", "user2", "user1", "user3", "user2", "user4"]

for visitor in visits:
    website_visitors.add(visitor)

print(f"Unique visitors: {len(website_visitors)}")  # 4
```

---

## 8. Decision Tree: Which Data Structure to Use?

```
START
├── Do you need key-value pairs?
│   └── YES → Use DICTIONARY
│
├── Do you only need unique elements?
│   └── YES → Use SET
│
├── Does the data need to change?
│   ├── NO → Use TUPLE
│   │
│   └── YES
│       ├── Do you need to maintain order?
│       │   └── YES → Use LIST
│       │
│       └── Do you need fast lookups?
│           ├── YES → Use SET
│           └── NO → Use LIST
```

### Quick Tips
- **Store student records?** → Dictionary
- **Store coordinates (x, y)?** → Tuple
- **Store a to-do list?** → List
- **Track unique tags?** → Set
- **Configuration settings?** → Dictionary
- **Return multiple values?** → Tuple
- **Remove duplicates?** → Set

---

## Summary

Each data structure in Python serves a specific purpose:

- **Lists** for ordered, changeable collections
- **Tuples** for ordered, unchangeable collections
- **Dictionaries** for key-value mappings
- **Sets** for unique, unordered collections

Choose the right data structure based on your specific needs for order, mutability, uniqueness, and access patterns.