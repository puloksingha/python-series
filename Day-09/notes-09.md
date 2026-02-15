# Python Object-Oriented Programming (OOP)

Comprehensive guide to classes, objects, inheritance, encapsulation, and polymorphism

---

## 1. Classes and Objects - Basics

### Overview
- **Classes**: Blueprints for creating objects
- **Objects**: Instances of classes
- **Attributes**: Variables inside a class
- **Methods**: Functions inside a class
- **self**: Refers to the instance itself

### Class Definition

```python
class Dog:
    """A simple Dog class."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
```

### Creating Objects

```python
dog1 = Dog("Buddy", 3)  # Creating an instance
dog2 = Dog("Max", 5)    # Creating another instance

print(dog1.name)          # Accessing instance attribute
print(dog1.bark())        # Calling instance method
print(Dog.species)        # Accessing class attribute
```

### Class Attributes vs Instance Attributes

| Aspect | Class Attributes | Instance Attributes |
|--------|-----------------|-------------------|
| **Shared By** | All instances | Single instance |
| **Definition** | Inside class, outside __init__ | In __init__ method using self |
| **Access** | ClassName.attr or self.attr | self.attr |
| **Modification** | Affects all instances | Affects only one instance |
| **Use Case** | Constants, shared data | Unique per object |

### Understanding self

```python
class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value  # self refers to the instance
    
    def increment(self):
        self.value += 1
        return self.value

counter1 = Counter(10)
counter2 = Counter(100)

counter1.increment()  # Increments counter1.value, not counter2.value
```

---

## 2. Special Methods (Magic/Dunder Methods)

### Overview
- Special methods have double underscores: `__method__`
- Allow objects to behave like built-in types
- Enable operator overloading
- Called automatically by Python

### Common Special Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `__init__` | Constructor (initializer) | Initializes new objects |
| `__str__` | String representation for users | `print(obj)` |
| `__repr__` | String representation for developers | `repr(obj)` |
| `__len__` | Length of object | `len(obj)` |
| `__eq__` | Equality comparison | `obj1 == obj2` |
| `__lt__` | Less than comparison | `obj1 < obj2` |
| `__add__` | Addition operator | `obj1 + obj2` |
| `__sub__` | Subtraction operator | `obj1 - obj2` |
| `__mul__` | Multiplication operator | `obj1 * 3` |
| `__getitem__` | Index access | `obj[0]` |

### Example: Implementing Special Methods

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation for users
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # String representation for developers
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # Length of book
    def __len__(self):
        return self.pages
    
    # Comparison operators
    def __eq__(self, other):
        return self.pages == other.pages
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    # Addition (combine pages)
    def __add__(self, other):
        total_pages = self.pages + other.pages
        return f"Combined: {total_pages} pages"


book1 = Book("Python 101", "Alice", 300)
book2 = Book("Advanced Python", "Bob", 450)

print(str(book1))        # Uses __str__
print(len(book1))        # Uses __len__
print(book1 == book2)    # Uses __eq__
print(book1 < book2)     # Uses __lt__
print(book1 + book2)     # Uses __add__
```

---

## 3. Encapsulation - Data Hiding

### Overview
- **Public**: Accessible from anywhere (no prefix)
- **Protected**: Accessible within class and subclasses (single underscore: `_attr`)
- **Private**: Accessible only within class (double underscore: `__attr`)
- Encapsulation protects internal data and ensures data integrity

### Access Levels

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Public
        self._balance = balance               # Protected (convention)
        self.__transactions = []              # Private (name mangling)
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def get_transaction_history(self):
        return self.__transactions.copy()

account = BankAccount("12345", 1000)
print(account.get_balance())            # OK: Use getter method
print(account._balance)                 # Works but discouraged
# print(account.__transactions)          # Error: AttributeError
```

### Properties (Pythonic Getters/Setters)

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit."""
        self.celsius = (value - 32) * 5/9

# Using properties like attributes
temp = Temperature(25)
print(temp.celsius)        # Calls getter
temp.celsius = 30          # Calls setter
print(temp.fahrenheit)     # Calculated property
```

---

## 4. Inheritance - Single Inheritance

### Overview
- Child (derived) class inherits from parent (base) class
- **IS-A relationship**: "Dog IS-A Animal"
- Child can override parent methods
- Use `super()` to call parent methods

### Single Inheritance Example

```python
# Parent (Base) class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "Some sound"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Child (Derived) class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call parent constructor
        self.color = color
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Meow!"
    
    # Add new method
    def purr(self):
        return f"{self.name} is purring"

# Using inheritance
cat = Cat("Whiskers", 3, "Orange")
print(cat.get_info())  # Inherited method
print(cat.speak())     # Overridden method
print(cat.purr())      # New method
```

### Method Resolution Order (MRO)

```python
# View the inheritance chain
print(Cat.__mro__)
# Output: (<class 'Cat'>, <class 'Animal'>, <class 'object'>)
```

---

## 5. Inheritance - Multiple Inheritance

### Overview
- Class inherits from multiple parents
- Use mixins for additional functionality
- Python uses C3 linearization for MRO

### Multiple Inheritance Example

```python
class Flyer:
    """Mixin for flying ability."""
    def fly(self):
        return f"{self.name} is flying"

class Swimmer:
    """Mixin for swimming ability."""
    def swim(self):
        return f"{self.name} is swimming"

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Duck(Animal, Flyer, Swimmer):
    """Duck can walk, fly, and swim."""
    def speak(self):
        return f"{self.name} says Quack!"

# Using multiple inheritance
duck = Duck("Donald", 2)
print(duck.speak())   # From Duck
print(duck.fly())     # From Flyer
print(duck.swim())    # From Swimmer
```

### Best Practices for Multiple Inheritance

- Use mixins for specific functionality
- Keep inheritance hierarchy simple
- Understand MRO: `ClassName.__mro__`
- Avoid diamond problem when possible

---

## 6. Polymorphism

### Overview
- **Polymorphism**: "Many forms"
- Same method name, different behavior in different classes
- Allows treating different objects uniformly
- Enables flexible, extensible code

### Type 1: Method Overriding

```python
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polymorphism in action
shapes = [Rectangle(5, 10), Circle(7)]

for shape in shapes:
    print(f"{shape.name}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
```

### Type 2: Duck Typing

```python
class Duck:
    def speak(self):
        return "Quack!"

class Person:
    def speak(self):
        return "Hello!"

def make_it_speak(thing):
    """If it can speak, we don't care what it is."""
    print(thing.speak())

# Duck typing: "If it walks like a duck and quacks like a duck..."
make_it_speak(Duck())    # Quack!
make_it_speak(Person())  # Hello!
```

---

## 7. Abstract Base Classes (ABC)

### Overview
- Define interfaces that subclasses must implement
- Cannot instantiate abstract classes
- Use `@abstractmethod` decorator
- Enforce contract for subclasses

### Abstract Base Class Example

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processing."""
    
    @abstractmethod
    def process_payment(self, amount):
        """Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def refund(self, amount):
        """Must be implemented by subclasses."""
        pass
    
    # Concrete method (shared by all subclasses)
    def log_transaction(self, transaction_type, amount):
        print(f"Transaction: {transaction_type} ${amount}")

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction("Credit Card", amount)
        return f"Processing ${amount}"
    
    def refund(self, amount):
        self.log_transaction("Refund", amount)
        return f"Refunding ${amount}"

# Using abstract base classes
# payment = PaymentProcessor()  # Error: TypeError
processor = CreditCardProcessor()  # OK
print(processor.process_payment(100))
```

---

## 8. Class Methods and Static Methods

### Overview
- **Instance methods**: Operate on instance data (use `self`)
- **Class methods**: Operate on class data (use `cls`, decorated with `@classmethod`)
- **Static methods**: Don't need instance or class data (decorated with `@staticmethod`)

### Different Method Types

```python
class Pizza:
    pizza_count = 0
    
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        Pizza.pizza_count += 1
    
    # Instance method
    def get_description(self):
        return f"{self.size} pizza with {', '.join(self.toppings)}"
    
    # Class method (factory method)
    @classmethod
    def margherita(cls, size):
        """Create Margherita pizza."""
        return cls(size, ["mozzarella", "tomato", "basil"])
    
    @classmethod
    def get_pizza_count(cls):
        """Get total pizzas created."""
        return cls.pizza_count
    
    # Static method
    @staticmethod
    def is_valid_size(size):
        """Check if size is valid."""
        valid_sizes = ["small", "medium", "large"]
        return size.lower() in valid_sizes

# Using different method types
pizza1 = Pizza("large", ["cheese", "pepperoni"])
print(pizza1.get_description())  # Instance method

pizza2 = Pizza.margherita("medium")  # Class method
print(Pizza.get_pizza_count())       # Class method

print(Pizza.is_valid_size("large"))  # Static method
```

| Method Type | Decorator | First Parameter | Use Case |
|------------|-----------|------------------|----------|
| Instance | None | `self` | Data specific to instance |
| Class | `@classmethod` | `cls` | Factory methods, class data |
| Static | `@staticmethod` | None | Utility functions related to class |

---

## 9. Composition Over Inheritance

### Overview
- **Inheritance**: IS-A relationship (Car IS-A Vehicle)
- **Composition**: HAS-A relationship (Car HAS-A Engine)
- Composition is more flexible than inheritance
- Prefer composition for better code design

### Composition Example

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False
    
    def start(self):
        self.running = True
        return "Engine started"
    
    def stop(self):
        self.running = False
        return "Engine stopped"

class Wheels:
    def __init__(self, count):
        self.count = count
    
    def roll(self):
        return f"{self.count} wheels rolling"

class Car:
    """Car composed of Engine and Wheels."""
    
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        # Composition: Car HAS-A engine and wheels
        self.engine = Engine(horsepower)
        self.wheels = Wheels(4)
    
    def start(self):
        if self.engine.start():
            return f"{self.make} {self.model} started"
    
    def drive(self):
        if self.engine.running:
            return f"Driving: {self.wheels.roll()}"
        return "Start the engine first!"

# Using composition
car = Car("Toyota", "Camry", 200)
print(car.start())
print(car.drive())
```

### Composition vs Inheritance

| Aspect | Inheritance | Composition |
|--------|-------------|------------|
| **Relationship** | IS-A | HAS-A |
| **Flexibility** | Less flexible | More flexible |
| **Complexity** | Can be complex | Cleaner design |
| **Change** | Hard to refactor | Easy to refactor |
| **Multiple** | Diamond problem | Works well |

---

## 10. Dataclasses (Python 3.7+)

### Overview
- Automatically generate `__init__`, `__repr__`, `__eq__`, etc.
- Less boilerplate code
- Type hints for better IDE support
- Great for simple data-holding classes

### Dataclass Example

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    """Product dataclass with auto-generated methods."""
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)
    
    def total_value(self):
        return self.price * self.quantity
    
    def __post_init__(self):
        """Called after __init__."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")

# Using dataclasses
product1 = Product("Laptop", 999.99, 5, ["electronics", "computers"])
product2 = Product("Mouse", 29.99, 10)

print(product1)  # Auto-generated __repr__
print(product1.total_value())
print(f"Equal? {product1 == product2}")  # Auto-generated __eq__
```

### Dataclass Features

```python
@dataclass
class Point:
    x: float
    y: float = 0.0  # Default value
    
    def distance(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Auto-generated methods:
# __init__: Initializes all attributes
# __repr__: String representation for debugging
# __eq__: Equality comparison
# __hash__: If frozen=True (make immutable)
```

---

## 11. OOP Best Practices and Design Principles

### SOLID Principles

#### 1. Single Responsibility Principle (SRP)
- A class should have only one reason to change
- Each class should do one thing well

```python
# Bad: FileManager does too much
class FileManager:
    def read_file(self, path): pass
    def write_file(self, path): pass
    def parse_json(self): pass
    def parse_csv(self): pass

# Good: Separate concerns
class FileManager:
    def read_file(self, path): pass
    def write_file(self, path): pass

class JsonParser:
    def parse(self): pass

class CsvParser:
    def parse(self): pass
```

#### 2. Open/Closed Principle (OCP)
- Open for extension, closed for modification
- Use inheritance and composition to extend behavior

```python
# Use abstract class instead of modifying existing code
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount): pass

# Extend with new payment methods
class CreditCard(PaymentProcessor):
    def process(self, amount): pass

class Bitcoin(PaymentProcessor):
    def process(self, amount): pass
```

#### 3. Liskov Substitution Principle (LSP)
- Subtypes must be substitutable for their base types
- Child classes should enhance, not break parent functionality

```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
        # BAD: This breaks the contract!

# Better approach
class FlyingBird(Bird):
    def fly(self): return "Flying"

class SwimmingBird(Bird):
    def swim(self): return "Swimming"

class Penguin(SwimmingBird):
    def swim(self): return "Swimming"  # OK: Uses own capability
```

#### 4. Interface Segregation Principle (ISP)
- Many specific interfaces are better than one general interface
- Don't force classes to implement methods they don't need

```python
# Bad: One large interface
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

# Good: Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): pass
    def eat(self): pass

class Robot(Workable):  # Only implements what it needs
    def work(self): pass
```

#### 5. Dependency Inversion Principle (DIP)
- Depend on abstractions, not concretions
- Use abstract base classes and interfaces

```python
# Bad: Depends on concrete classes
class EmailSender:
    def send(self, msg): pass

class NotificationService:
    def __init__(self):
        self.email = EmailSender()  # Tight coupling

# Good: Depends on abstraction
class Sender(ABC):
    @abstractmethod
    def send(self, msg): pass

class NotificationService:
    def __init__(self, sender: Sender):
        self.sender = sender  # Loose coupling
```

### Naming Conventions

```python
class MyClass:               # Class names: PascalCase
    CONSTANT = 10           # Constants: UPPER_SNAKE_CASE
    
    def public_method(self): pass      # Methods: snake_case
    
    def _protected_method(self): pass  # Protected: _single_underscore
    
    def __private_method(self): pass   # Private: __double_underscore
    
    self.public_attr = 1               # Public attribute: snake_case
    self._protected_attr = 2           # Protected attribute
    self.__private_attr = 3            # Private attribute
```

### When to Use What

| Concept | When to Use |
|---------|------------|
| **Inheritance** | IS-A relationship, shared behavior |
| **Composition** | HAS-A relationship, more flexibility |
| **Abstract Classes** | Define interfaces, enforce contracts |
| **Dataclasses** | Simple data-holding classes |
| **Properties** | Computed attributes, validation |
| **Class Methods** | Factory methods, class operations |
| **Static Methods** | Utility functions |

### Encapsulation Tips

- Make attributes private by default
- Provide public methods when needed
- Use `@property` for Pythonic access
- Validate data in setters
- Document public interface

### Polymorphism Benefits

- Write more flexible code
- Treat different objects uniformly
- Easy to extend with new types
- Reduces code repetition
- Better maintainability

---

## 12. Practical Example: Library Management System

### Full Implementation

```python
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """Abstract base class for library items."""
    
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False
    
    @abstractmethod
    def get_type(self):
        pass
    
    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def __str__(self):
        status = "Checked out" if self.is_checked_out else "Available"
        return f"{self.get_type()}: {self.title} ({status})"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
    
    def get_type(self):
        return "Book"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} by {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration
    
    def get_type(self):
        return "DVD"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} directed by {self.director}"

class Library:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")
    
    def checkout_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                if item.checkout():
                    print(f"Checked out: {item}")
                    return True
                print(f"Already checked out")
                return False
        print("Item not found")
        return False
    
    def return_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                if item.return_item():
                    print(f"Returned: {item}")
                    return True
                print(f"Not checked out")
                return False
        print("Item not found")
        return False
    
    def list_available_items(self):
        print(f"\n{self.name} - Available Items:")
        for item in self.items:
            if not item.is_checked_out:
                print(f"  {item}")

# Using the system
library = Library("City Library")

book1 = Book("Python Crash Course", "B001", "Eric Matthes", 544)
dvd1 = DVD("Inception", "D001", "Christopher Nolan", 148)

library.add_item(book1)
library.add_item(dvd1)

library.list_available_items()
library.checkout_item("B001")
library.list_available_items()
library.return_item("B001")
```

---

## 📚 Key Takeaways

1. **Classes and Objects**: Blueprints and instances
2. **Encapsulation**: Hide implementation details
3. **Inheritance**: Share behavior through IS-A relationships
4. **Polymorphism**: Same interface, different implementations
5. **Composition**: Use HAS-A relationships for flexibility
6. **Abstract Classes**: Define contracts and interfaces
7. **Properties**: Pythonic getters and setters
8. **Design Principles**: Follow SOLID for maintainable code
9. **Dataclasses**: Reduce boilerplate for simple classes
10. **Best Practices**: Clear code, single responsibility, flexibility

---

## 🎯 Tips for Effective OOP

1. **Plan Before Coding**: Think about class relationships
2. **Keep It Simple**: Don't over-engineer; start simple
3. **Use Meaningful Names**: Class and method names should be clear
4. **Encapsulate**: Hide internal details, expose only what's necessary
5. **Favor Composition**: Prefer HAS-A over IS-A when possible
6. **Follow SOLID**: Write maintainable, flexible code
7. **Document**: Write docstrings for classes and methods
8. **Test**: Write unit tests for your classes
9. **Refactor**: Improve design as you learn more
10. **Learn from Others**: Study well-designed libraries

---

*Day 09: Object-Oriented Programming - The foundation of scalable Python applications*
