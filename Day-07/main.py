"""
PYTHON DATA STRUCTURES COMPREHENSIVE GUIDE
==========================================
Everything you need to know about Lists, Tuples, Dictionaries, and Sets
"""

# ============================================================================
# 1. LISTS - Ordered, Mutable Collections
# ============================================================================

print("="*70)
print("LISTS - Ordered, Mutable, Allow Duplicates")
print("="*70)

# --- Creating Lists ---
# Empty list
empty_list = []
empty_list_alt = list()

# List with initial values
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]  # Can contain different types

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print()


# --- Accessing Elements ---
print("Accessing List Elements:")
print(f"First fruit: {fruits[0]}")           # Index starts at 0
print(f"Last fruit: {fruits[-1]}")           # Negative indexing from end
print(f"Second to last: {fruits[-2]}")
print()


# --- Slicing ---
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slicing Lists:")
print(f"Original: {numbers}")
print(f"First 3 elements: {numbers[:3]}")    # [0, 1, 2]
print(f"Elements 3-6: {numbers[3:7]}")       # [3, 4, 5, 6]
print(f"Last 3 elements: {numbers[-3:]}")    # [7, 8, 9]
print(f"Every 2nd element: {numbers[::2]}")  # [0, 2, 4, 6, 8]
print(f"Reversed: {numbers[::-1]}")          # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print()


# --- Modifying Lists ---
print("Modifying Lists:")
fruits = ["apple", "banana", "cherry"]

# Change an element
fruits[1] = "blueberry"
print(f"After change: {fruits}")

# Append (add to end)
fruits.append("date")
print(f"After append: {fruits}")

# Insert at specific position
fruits.insert(1, "avocado")
print(f"After insert: {fruits}")

# Extend (add multiple items)
fruits.extend(["elderberry", "fig"])
print(f"After extend: {fruits}")

# Remove by value
fruits.remove("cherry")
print(f"After remove: {fruits}")

# Pop (remove and return last item or at index)
last_item = fruits.pop()
print(f"Popped: {last_item}, Remaining: {fruits}")

second_item = fruits.pop(1)
print(f"Popped at index 1: {second_item}, Remaining: {fruits}")
print()


# --- List Operations ---
print("List Operations:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Combined: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Length
print(f"Length: {len(list1)}")

# Check membership
print(f"2 in list1: {2 in list1}")
print(f"10 in list1: {10 in list1}")
print()


# --- List Methods ---
print("Common List Methods:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Count occurrences
print(f"Count of 1: {numbers.count(1)}")

# Find index
print(f"Index of 4: {numbers.index(4)}")

# Sort (modifies original)
numbers.sort()
print(f"Sorted: {numbers}")

# Sort in reverse
numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")

# Reverse (modifies original)
numbers.reverse()
print(f"Reversed: {numbers}")

# Copy a list
numbers_copy = numbers.copy()
# or: numbers_copy = numbers[:]
# or: numbers_copy = list(numbers)
print(f"Copy: {numbers_copy}")

# Clear all elements
test_list = [1, 2, 3]
test_list.clear()
print(f"After clear: {test_list}")
print()


# --- List Comprehensions (Powerful!) ---
print("List Comprehensions:")

# Basic: create list of squares
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition: even numbers only
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Transform strings
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")
print()


# --- When to Use Lists ---
print("WHEN TO USE LISTS:")
print("✓ Need ordered collection")
print("✓ Need to modify elements (add, remove, change)")
print("✓ Need to allow duplicates")
print("✓ Need indexing and slicing")
print("✓ Order matters")
print("✗ Need fast membership testing (use set instead)")
print("✗ Need to prevent modification (use tuple instead)")
print()


# ============================================================================
# 2. TUPLES - Ordered, Immutable Collections
# ============================================================================

print("="*70)
print("TUPLES - Ordered, Immutable, Allow Duplicates")
print("="*70)

# --- Creating Tuples ---
# Empty tuple
empty_tuple = ()
empty_tuple_alt = tuple()

# Tuple with values
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# Single element tuple (note the comma!)
single = (42,)  # Comma is required!
not_a_tuple = (42)  # This is just an int

print(f"Coordinates: {coordinates}")
print(f"RGB Color: {rgb_color}")
print(f"Single element tuple: {single}, type: {type(single)}")
print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")
print()


# --- Tuple Packing and Unpacking ---
print("Tuple Packing and Unpacking:")

# Packing
person = "Alice", 25, "Engineer"  # Parentheses optional
print(f"Packed: {person}")

# Unpacking
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Swap variables using tuple unpacking
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking (Python 3)
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")
print()


# --- Accessing Tuples ---
print("Accessing Tuples:")
colors = ("red", "green", "blue", "yellow")

print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Slice: {colors[1:3]}")
print()


# --- Tuple Operations ---
print("Tuple Operations:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated: {repeated}")

# Length
print(f"Length: {len(tuple1)}")

# Count and index
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print()


# --- Immutability ---
print("Immutability:")
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise TypeError!
print("Tuples cannot be modified after creation")

# However, if tuple contains mutable objects...
mixed_tuple = ([1, 2], [3, 4])
mixed_tuple[0].append(3)  # This works! Modifying the list inside
print(f"Modified inner list: {mixed_tuple}")
print()


# --- Converting Between Lists and Tuples ---
print("Converting:")
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

back_to_list = list(my_tuple)
print(f"Tuple to list: {back_to_list}")
print()


# --- When to Use Tuples ---
print("WHEN TO USE TUPLES:")
print("✓ Data should not change (immutable)")
print("✓ Returning multiple values from function")
print("✓ Dictionary keys (tuples are hashable, lists aren't)")
print("✓ Slightly faster than lists")
print("✓ Protect data from accidental modification")
print("✓ Represent fixed collections (coordinates, RGB values)")
print("✗ Need to modify contents (use list instead)")
print()


# ============================================================================
# 3. DICTIONARIES - Key-Value Pairs, Unordered (ordered in Python 3.7+)
# ============================================================================

print("="*70)
print("DICTIONARIES - Key-Value Pairs, Mutable, No Duplicate Keys")
print("="*70)

# --- Creating Dictionaries ---
# Empty dictionary
empty_dict = {}
empty_dict_alt = dict()

# Dictionary with values
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "CS"]
}

# Using dict() constructor
person = dict(name="Bob", age=25, city="New York")

print(f"Student: {student}")
print(f"Person: {person}")
print()


# --- Accessing Dictionary Values ---
print("Accessing Dictionary Values:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Using get() - safer, returns None if key doesn't exist
print(f"Grade: {student.get('grade')}")
print(f"GPA: {student.get('gpa', 'Not found')}")  # Default value
print()


# --- Adding and Modifying ---
print("Adding and Modifying:")
student["gpa"] = 3.8  # Add new key-value
print(f"After adding GPA: {student}")

student["age"] = 21  # Modify existing
print(f"After modifying age: {student}")

# Update multiple values
student.update({"semester": 3, "major": "Computer Science"})
print(f"After update: {student}")
print()


# --- Removing Items ---
print("Removing Items:")
sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Remove specific key
removed_value = sample_dict.pop("b")
print(f"Popped 'b': {removed_value}, Remaining: {sample_dict}")

# Remove and return arbitrary item (Python 3.7+ removes last item)
item = sample_dict.popitem()
print(f"Popped item: {item}, Remaining: {sample_dict}")

# Delete specific key
del sample_dict["a"]
print(f"After del: {sample_dict}")

# Clear all items
sample_dict.clear()
print(f"After clear: {sample_dict}")
print()


# --- Dictionary Methods ---
print("Dictionary Methods:")
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "Blue"
}

# Get all keys
print(f"Keys: {list(car.keys())}")

# Get all values
print(f"Values: {list(car.values())}")

# Get all key-value pairs
print(f"Items: {list(car.items())}")

# Check if key exists
print(f"'brand' in car: {'brand' in car}")
print(f"'price' in car: {'price' in car}")
print()


# --- Iterating Through Dictionaries ---
print("Iterating Through Dictionaries:")

# Iterate over keys
print("Keys:")
for key in car:
    print(f"  {key}")

# Iterate over values
print("Values:")
for value in car.values():
    print(f"  {value}")

# Iterate over key-value pairs
print("Key-Value Pairs:")
for key, value in car.items():
    print(f"  {key}: {value}")
print()


# --- Dictionary Comprehensions ---
print("Dictionary Comprehensions:")

# Create dictionary from lists
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(f"Squares: {squares_dict}")

# With condition
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transform existing dictionary
prices = {"apple": 0.5, "banana": 0.3, "cherry": 0.8}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Discounted prices: {discounted}")
print()


# --- Nested Dictionaries ---
print("Nested Dictionaries:")
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 88]
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": [92, 88, 95]
    }
}

print(f"Student1 name: {students['student1']['name']}")
print(f"Student2 grades: {students['student2']['grades']}")
print()


# --- When to Use Dictionaries ---
print("WHEN TO USE DICTIONARIES:")
print("✓ Need key-value associations")
print("✓ Need fast lookups by key")
print("✓ Keys are meaningful (not just numeric indices)")
print("✓ Need to count occurrences")
print("✓ Storing configuration settings")
print("✓ JSON-like data structures")
print("✗ Need ordered sequence (use list instead)")
print("✗ Need duplicate keys (not possible)")
print()


# ============================================================================
# 4. SETS - Unordered, Unique Elements
# ============================================================================

print("="*70)
print("SETS - Unordered, Mutable, No Duplicates")
print("="*70)

# --- Creating Sets ---
# Empty set (must use set(), {} creates empty dict!)
empty_set = set()

# Set with values
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

# From list (removes duplicates!)
list_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(list_with_dupes)

print(f"Fruits set: {fruits_set}")
print(f"Numbers set: {numbers_set}")
print(f"Unique from list: {unique_numbers}")
print()


# --- Adding and Removing Elements ---
print("Adding and Removing Elements:")
colors = {"red", "green", "blue"}

# Add single element
colors.add("yellow")
print(f"After add: {colors}")

# Add multiple elements
colors.update(["orange", "purple", "pink"])
print(f"After update: {colors}")

# Remove element (raises error if not found)
colors.remove("green")
print(f"After remove: {colors}")

# Discard element (no error if not found)
colors.discard("purple")
colors.discard("black")  # No error even though black isn't in set
print(f"After discard: {colors}")

# Pop random element
popped = colors.pop()
print(f"Popped: {popped}, Remaining: {colors}")

# Clear all
colors.clear()
print(f"After clear: {colors}")
print()


# --- Set Operations ---
print("Set Operations (Mathematical):")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
union = set_a | set_b
# or: union = set_a.union(set_b)
print(f"Union: {union}")

# Intersection (common elements)
intersection = set_a & set_b
# or: intersection = set_a.intersection(set_b)
print(f"Intersection: {intersection}")

# Difference (in A but not in B)
difference = set_a - set_b
# or: difference = set_a.difference(set_b)
print(f"Difference (A-B): {difference}")

# Symmetric difference (in A or B but not both)
sym_diff = set_a ^ set_b
# or: sym_diff = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference: {sym_diff}")

# Subset check
set_c = {1, 2, 3}
print(f"{set_c} is subset of {set_a}: {set_c.issubset(set_a)}")
print(f"{set_a} is superset of {set_c}: {set_a.issuperset(set_c)}")

# Disjoint (no common elements)
set_d = {10, 11, 12}
print(f"{set_a} and {set_d} are disjoint: {set_a.isdisjoint(set_d)}")
print()


# --- Set Comprehensions ---
print("Set Comprehensions:")
squares_set = {x**2 for x in range(10)}
print(f"Squares: {squares_set}")

even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")
print()


# --- Frozen Sets (Immutable Sets) ---
print("Frozen Sets:")
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
# frozen.add(6)  # This would raise AttributeError!

# Can be used as dictionary keys
dict_with_set_key = {frozen: "This works!"}
print(f"Dict with frozen set key: {dict_with_set_key}")
print()


# --- Practical Set Examples ---
print("Practical Examples:")

# Remove duplicates from list
numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique = list(set(numbers_with_dupes))
print(f"Remove duplicates: {unique}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Common elements: {common}")

# Find unique elements across lists
unique_to_list1 = set(list1) - set(list2)
print(f"Unique to list1: {unique_to_list1}")

# Membership testing (very fast!)
large_set = set(range(1000000))
print(f"999999 in large set: {999999 in large_set}")  # Very fast!
print()


# --- When to Use Sets ---
print("WHEN TO USE SETS:")
print("✓ Need to remove duplicates")
print("✓ Need fast membership testing")
print("✓ Need mathematical set operations (union, intersection, etc.)")
print("✓ Order doesn't matter")
print("✓ Need unique elements only")
print("✗ Need to maintain order (use list instead)")
print("✗ Need to access by index (use list instead)")
print("✗ Need to allow duplicates (use list instead)")
print()


# ============================================================================
# 5. COMPARISON AND WHEN TO USE EACH
# ============================================================================

print("="*70)
print("QUICK COMPARISON CHART")
print("="*70)

comparison = """
Feature          | List    | Tuple   | Dictionary | Set
-----------------+---------+---------+------------+--------
Ordered          | Yes     | Yes     | Yes(3.7+)  | No
Mutable          | Yes     | No      | Yes        | Yes
Duplicates       | Yes     | Yes     | Keys: No   | No
Indexed          | Yes     | Yes     | By key     | No
Syntax           | []      | ()      | {}         | {}
Fast lookup      | No      | No      | Yes        | Yes
Use for          | Ordered | Fixed   | Key-value  | Unique
                 | items   | data    | pairs      | items
"""
print(comparison)


# ============================================================================
# 6. PERFORMANCE COMPARISON
# ============================================================================

print("="*70)
print("PERFORMANCE CHARACTERISTICS")
print("="*70)

performance = """
Operation              | List      | Tuple     | Dict      | Set
-----------------------+-----------+-----------+-----------+----------
Access by index/key    | O(1)      | O(1)      | O(1)      | N/A
Search (membership)    | O(n)      | O(n)      | O(1)      | O(1)
Insert/Delete          | O(n)      | N/A       | O(1)      | O(1)
Append                 | O(1)      | N/A       | O(1)      | O(1)
Memory usage           | Medium    | Low       | High      | Medium

Notes:
- Lists: Good for ordered collections, slower for searching
- Tuples: Faster than lists, immutable, less memory
- Dicts: Fast lookups, higher memory usage
- Sets: Fast membership testing, no duplicates
"""
print(performance)


# ============================================================================
# 7. REAL-WORLD EXAMPLES
# ============================================================================

print("="*70)
print("REAL-WORLD USAGE EXAMPLES")
print("="*70)

# Example 1: Shopping Cart (List)
shopping_cart = [
    {"item": "Apple", "quantity": 3, "price": 0.5},
    {"item": "Bread", "quantity": 1, "price": 2.0},
    {"item": "Milk", "quantity": 2, "price": 1.5}
]
total = sum(item["quantity"] * item["price"] for item in shopping_cart)
print(f"Shopping Cart Total: ${total}")
print()

# Example 2: Geographic Coordinates (Tuple)
locations = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Tokyo": (35.6762, 139.6503)
}
print(f"Coordinates (immutable): {locations['Tokyo']}")
print()

# Example 3: User Profile (Dictionary)
user_profile = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 28,
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}
print(f"User theme: {user_profile['preferences']['theme']}")
print()

# Example 4: Unique Visitors (Set)
website_visitors = set()
visits = ["user1", "user2", "user1", "user3", "user2", "user4"]

for visitor in visits:
    website_visitors.add(visitor)

print(f"Unique visitors: {len(website_visitors)}")
print(f"Visitor list: {website_visitors}")
print()


# ============================================================================
# 8. CHOOSING THE RIGHT DATA STRUCTURE - DECISION TREE
# ============================================================================

print("="*70)
print("DECISION TREE: WHICH DATA STRUCTURE TO USE?")
print("="*70)

decision_tree = """
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

Quick Tips:
• Need to store student records? → Dictionary
• Need coordinates (x, y)? → Tuple
• Need a to-do list? → List
• Need to track unique tags? → Set
• Need configuration settings? → Dictionary
• Need to return multiple values? → Tuple
• Need to remove duplicates? → Set
"""
print(decision_tree)

print("\n" + "="*70)
print("END OF DATA STRUCTURES GUIDE")
print("="*70)