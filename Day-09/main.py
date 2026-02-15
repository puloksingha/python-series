"""
PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) COMPREHENSIVE GUIDE
=============================================================
Everything you need to know about Classes, Objects, Inheritance,
Encapsulation, and Polymorphism
"""

# ============================================================================
# 1. CLASSES AND OBJECTS - BASICS
# ============================================================================

print("="*70)
print("CLASSES AND OBJECTS - BASICS")
print("="*70)

# --- Simple Class Definition ---
print("\n1. Simple Class:")

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
    
    # Instance method
    def get_info(self):
        return f"{self.name} is {self.age} years old"


# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")
print(f"Dog 1: {dog1.bark()}")
print(f"Species (class attribute): {Dog.species}")
print()


# --- Understanding self ---
print("2. Understanding 'self':")

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value  # 'self' refers to the instance
    
    def increment(self):
        self.value += 1
        return self.value
    
    def decrement(self):
        self.value -= 1
        return self.value
    
    def get_value(self):
        return self.value


counter1 = Counter(10)
counter2 = Counter(100)

print(f"Counter 1: {counter1.get_value()}")
print(f"Counter 2: {counter2.get_value()}")
counter1.increment()
print(f"Counter 1 after increment: {counter1.get_value()}")
print(f"Counter 2 unchanged: {counter2.get_value()}")
print()


# --- Class vs Instance Attributes ---
print("3. Class vs Instance Attributes:")

class Employee:
    # Class attribute
    company_name = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance attributes
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display(self):
        return f"{self.name} works at {Employee.company_name}"


emp1 = Employee("Alice", 70000)
emp2 = Employee("Bob", 80000)

print(f"Employee 1: {emp1.display()}")
print(f"Employee 2: {emp2.display()}")
print(f"Total employees: {Employee.employee_count}")

# Changing class attribute
Employee.company_name = "NewTech"
print(f"After company rename: {emp1.display()}")
print()


# ============================================================================
# 2. SPECIAL METHODS (MAGIC METHODS / DUNDER METHODS)
# ============================================================================

print("="*70)
print("SPECIAL METHODS (MAGIC METHODS)")
print("="*70)

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

print(f"str(book1): {str(book1)}")
print(f"repr(book1): {repr(book1)}")
print(f"len(book1): {len(book1)} pages")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 + book2: {book1 + book2}")
print()


# --- More Magic Methods ---
print("More Magic Methods:")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector index out of range")


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
print()


# ============================================================================
# 3. ENCAPSULATION - PRIVATE AND PUBLIC
# ============================================================================

print("="*70)
print("ENCAPSULATION - DATA HIDING")
print("="*70)

class BankAccount:
    """Demonstrates encapsulation with private attributes."""
    
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Public
        self._balance = balance  # Protected (convention: single underscore)
        self.__transactions = []  # Private (name mangling: double underscore)
    
    # Getter method
    def get_balance(self):
        """Get current balance."""
        return self._balance
    
    # Setter method with validation
    def deposit(self, amount):
        """Deposit money into account."""
        if amount > 0:
            self._balance += amount
            self.__transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__transactions.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_transaction_history(self):
        """Get transaction history."""
        return self.__transactions.copy()
    
    def __str__(self):
        return f"Account {self.account_number}: ${self._balance}"


account = BankAccount("12345", 1000)
print(f"Initial: {account}")

account.deposit(500)
print(f"After deposit: {account}")

account.withdraw(200)
print(f"After withdrawal: {account}")

print(f"Balance: ${account.get_balance()}")
print(f"Transactions: {account.get_transaction_history()}")

# Direct access to public attribute works
print(f"Account number: {account.account_number}")

# Protected attribute (works but discouraged)
print(f"Protected _balance: ${account._balance}")

# Private attribute (name mangling - works but very discouraged)
# print(account.__transactions)  # This would raise AttributeError
# print(account._BankAccount__transactions)  # This works (name mangling)
print()


# --- Properties (Pythonic Getters/Setters) ---
print("Properties (Pythonic way):")

class Temperature:
    """Temperature class with property decorators."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
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


temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

# Using properties like attributes
temp.celsius = 30
print(f"After setting celsius: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 212
print(f"After setting fahrenheit: {temp.celsius}°C = {temp.fahrenheit}°F")
print()


# ============================================================================
# 4. INHERITANCE - SINGLE INHERITANCE
# ============================================================================

print("="*70)
print("INHERITANCE - SINGLE INHERITANCE")
print("="*70)

# Parent (Base) class
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "Some sound"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"


# Child (Derived) class
class Cat(Animal):
    """Cat inherits from Animal."""
    
    def __init__(self, name, age, color):
        # Call parent constructor
        super().__init__(name, age)
        self.color = color
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Meow!"
    
    # Add new method
    def purr(self):
        return f"{self.name} is purring"


class DogNew(Animal):
    """Dog inherits from Animal."""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Woof!"
    
    # Add new method
    def fetch(self):
        return f"{self.name} is fetching"


# Using inherited classes
cat = Cat("Whiskers", 3, "Orange")
dog = DogNew("Buddy", 5, "Golden Retriever")

print(f"Cat info: {cat.get_info()}")  # Inherited method
print(f"Cat speaks: {cat.speak()}")   # Overridden method
print(f"Cat purrs: {cat.purr()}")     # New method

print(f"\nDog info: {dog.get_info()}")
print(f"Dog speaks: {dog.speak()}")
print(f"Dog fetches: {dog.fetch()}")
print()


# --- Method Resolution Order (MRO) ---
print("Method Resolution Order:")
print(f"Cat MRO: {Cat.__mro__}")
print()


# ============================================================================
# 5. INHERITANCE - MULTIPLE INHERITANCE
# ============================================================================

print("="*70)
print("MULTIPLE INHERITANCE")
print("="*70)

class Flyer:
    """Mixin for flying ability."""
    
    def fly(self):
        return f"{self.name} is flying"


class Swimmer:
    """Mixin for swimming ability."""
    
    def swim(self):
        return f"{self.name} is swimming"


class Duck(Animal, Flyer, Swimmer):
    """Duck can do everything: walk, fly, and swim."""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return f"{self.name} says Quack!"


class Penguin(Animal, Swimmer):
    """Penguin can walk and swim, but not fly."""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        return f"{self.name} says Honk!"


# Using multiple inheritance
duck = Duck("Donald", 2)
penguin = Penguin("Pingu", 3)

print(f"Duck: {duck.get_info()}")
print(f"Duck speaks: {duck.speak()}")
print(f"Duck flies: {duck.fly()}")
print(f"Duck swims: {duck.swim()}")

print(f"\nPenguin: {penguin.get_info()}")
print(f"Penguin speaks: {penguin.speak()}")
print(f"Penguin swims: {penguin.swim()}")
# print(f"Penguin flies: {penguin.fly()}")  # Would raise AttributeError
print()


# ============================================================================
# 6. POLYMORPHISM
# ============================================================================

print("="*70)
print("POLYMORPHISM")
print("="*70)

# --- Method Overriding (Polymorphism) ---
print("1. Method Overriding:")

class Shape:
    """Base class for shapes."""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate area - to be overridden."""
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        """Calculate perimeter - to be overridden."""
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


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        import math
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Polymorphism in action
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{shape.name}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
print()


# --- Duck Typing (Polymorphism without inheritance) ---
print("2. Duck Typing:")

class Duck:
    def speak(self):
        return "Quack!"
    
    def walk(self):
        return "Waddle waddle"


class Person:
    def speak(self):
        return "Hello!"
    
    def walk(self):
        return "Walking normally"


class Robot:
    def speak(self):
        return "Beep boop!"
    
    def walk(self):
        return "Rolling on wheels"


def make_it_speak_and_walk(thing):
    """If it can speak and walk, we don't care what it is."""
    print(f"Speaking: {thing.speak()}")
    print(f"Walking: {thing.walk()}")


# Duck typing in action
print("Duck typing - 'If it walks like a duck and quacks like a duck...'")
things = [Duck(), Person(), Robot()]

for thing in things:
    print(f"\n{thing.__class__.__name__}:")
    make_it_speak_and_walk(thing)
print()


# ============================================================================
# 7. ABSTRACT BASE CLASSES
# ============================================================================

print("="*70)
print("ABSTRACT BASE CLASSES (ABC)")
print("="*70)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processing."""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process payment - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def refund(self, amount):
        """Process refund - must be implemented by subclasses."""
        pass
    
    # Concrete method (shared by all subclasses)
    def log_transaction(self, transaction_type, amount):
        print(f"Transaction logged: {transaction_type} ${amount}")


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction("Credit Card Payment", amount)
        return f"Processing ${amount} via Credit Card"
    
    def refund(self, amount):
        self.log_transaction("Credit Card Refund", amount)
        return f"Refunding ${amount} to Credit Card"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        self.log_transaction("PayPal Payment", amount)
        return f"Processing ${amount} via PayPal"
    
    def refund(self, amount):
        self.log_transaction("PayPal Refund", amount)
        return f"Refunding ${amount} to PayPal"


# Using abstract base classes
# payment = PaymentProcessor()  # This would raise TypeError!

credit_card = CreditCardProcessor()
paypal = PayPalProcessor()

print(credit_card.process_payment(100))
print(paypal.process_payment(50))
print()


# ============================================================================
# 8. CLASS METHODS AND STATIC METHODS
# ============================================================================

print("="*70)
print("CLASS METHODS AND STATIC METHODS")
print("="*70)

class Pizza:
    """Pizza class demonstrating different method types."""
    
    # Class attribute
    pizza_count = 0
    
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        Pizza.pizza_count += 1
    
    # Instance method (regular method)
    def get_description(self):
        return f"{self.size} pizza with {', '.join(self.toppings)}"
    
    # Class method (works with class, not instance)
    @classmethod
    def margherita(cls, size):
        """Factory method to create Margherita pizza."""
        return cls(size, ["mozzarella", "tomato", "basil"])
    
    @classmethod
    def pepperoni(cls, size):
        """Factory method to create Pepperoni pizza."""
        return cls(size, ["mozzarella", "pepperoni"])
    
    @classmethod
    def get_pizza_count(cls):
        """Get total number of pizzas created."""
        return cls.pizza_count
    
    # Static method (doesn't use class or instance)
    @staticmethod
    def is_valid_size(size):
        """Check if size is valid."""
        valid_sizes = ["small", "medium", "large"]
        return size.lower() in valid_sizes


# Using different method types
print("Instance method:")
pizza1 = Pizza("large", ["cheese", "pepperoni", "mushrooms"])
print(f"  {pizza1.get_description()}")

print("\nClass methods (factory methods):")
pizza2 = Pizza.margherita("medium")
pizza3 = Pizza.pepperoni("large")
print(f"  {pizza2.get_description()}")
print(f"  {pizza3.get_description()}")

print(f"\nTotal pizzas created: {Pizza.get_pizza_count()}")

print("\nStatic method:")
print(f"  Is 'large' valid? {Pizza.is_valid_size('large')}")
print(f"  Is 'extra-large' valid? {Pizza.is_valid_size('extra-large')}")
print()


# ============================================================================
# 9. COMPOSITION OVER INHERITANCE
# ============================================================================

print("="*70)
print("COMPOSITION OVER INHERITANCE")
print("="*70)

# Using composition
class Engine:
    """Engine component."""
    
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
    """Wheels component."""
    
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
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def drive(self):
        if self.engine.running:
            return f"{self.make} {self.model} is driving. {self.wheels.roll()}"
        return "Start the engine first!"
    
    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"


# Using composition
car = Car("Toyota", "Camry", 200)
print(car.start())
print(car.drive())
print(car.stop())
print()


# ============================================================================
# 10. DATACLASSES (PYTHON 3.7+)
# ============================================================================

print("="*70)
print("DATACLASSES (Modern Python)")
print("="*70)

from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    """Product dataclass - auto-generates __init__, __repr__, etc."""
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

print(product1)
print(f"Total value: ${product1.total_value()}")
print(product2)
print()


# ============================================================================
# 11. PRACTICAL EXAMPLE - COMPLETE SYSTEM
# ============================================================================

print("="*70)
print("PRACTICAL EXAMPLE - LIBRARY MANAGEMENT SYSTEM")
print("="*70)

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
                else:
                    print(f"Item already checked out: {item}")
                    return False
        print("Item not found")
        return False
    
    def return_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                if item.return_item():
                    print(f"Returned: {item}")
                    return True
                else:
                    print(f"Item not checked out: {item}")
                    return False
        print("Item not found")
        return False
    
    def list_available_items(self):
        print(f"\n{self.name} - Available Items:")
        for item in self.items:
            if not item.is_checked_out:
                print(f"  {item}")


# Using the library system
library = Library("City Library")

# Add items
book1 = Book("Python Crash Course", "B001", "Eric Matthes", 544)
book2 = Book("Clean Code", "B002", "Robert Martin", 464)
dvd1 = DVD("Inception", "D001", "Christopher Nolan", 148)

library.add_item(book1)
library.add_item(book2)
library.add_item(dvd1)

# Operations
print()
library.list_available_items()

print()
library.checkout_item("B001")
library.checkout_item("D001")

print()
library.list_available_items()

print()
library.return_item("B001")

print()
library.list_available_items()
print()


# ============================================================================
# 12. BEST PRACTICES AND DESIGN PRINCIPLES
# ============================================================================

print("="*70)
print("OOP BEST PRACTICES")
print("="*70)

best_practices = """
1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
   - A class should have only one reason to change
   - Each class should do one thing well

2. OPEN/CLOSED PRINCIPLE (OCP)
   - Open for extension, closed for modification
   - Use inheritance and composition to extend behavior

3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
   - Subtypes must be substitutable for their base types
   - Child classes should enhance, not break parent functionality

4. INTERFACE SEGREGATION PRINCIPLE (ISP)
   - Many specific interfaces are better than one general interface
   - Don't force classes to implement methods they don't need

5. DEPENDENCY INVERSION PRINCIPLE (DIP)
   - Depend on abstractions, not concretions
   - Use abstract base classes and interfaces

NAMING CONVENTIONS:
- Class names: PascalCase (MyClass)
- Method/attribute names: snake_case (my_method)
- Private attributes: _single_underscore
- Name mangling: __double_underscore
- Constants: UPPER_SNAKE_CASE

WHEN TO USE:
- Inheritance: "IS-A" relationship (Car IS-A Vehicle)
- Composition: "HAS-A" relationship (Car HAS-A Engine)
- Prefer composition over inheritance for flexibility

ENCAPSULATION TIPS:
- Make attributes private by default
- Provide public methods (getters/setters) when needed
- Use @property for Pythonic attribute access
- Validate data in setters

POLYMORPHISM BENEFITS:
- Write flexible, reusable code
- Treat different objects uniformly
- Easy to extend with new types
"""

print(best_practices)

print("="*70)
print("END OF OOP GUIDE")
print("="*70)