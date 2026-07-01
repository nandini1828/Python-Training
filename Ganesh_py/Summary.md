# Python Data Types, Classes, and Data Structures - A Complete Guide

## Table of Contents
1. [Data Types & Methods](#data-types--methods)
2. [Class Objects](#class-objects)
3. [Data Structures](#data-structures)
4. [Understanding OOPS](#understanding-oops)

---

## Data Types & Methods

### What are Data Types?
Data types are classifications of data that tell Python how to handle the data. Common types: int, float, str, bool, list, tuple, dict, set.

### 1. Integer (int)
```python
# Creating integers
age = 25
year = 2024
temperature = -5

# Methods and operations for integers
number = 42

# Convert to string
print(str(number))  # Output: "42"

# Get absolute value
num = -10
print(abs(num))  # Output: 10

# Power operation
print(pow(2, 3))  # Output: 8 (2 to the power of 3)

# Check type
print(type(number))  # Output: <class 'int'>

# Arithmetic operations
print(10 + 5)   # Addition: 15
print(10 - 5)   # Subtraction: 5
print(10 * 5)   # Multiplication: 50
print(10 / 5)   # Division: 2.0
print(10 // 3)  # Floor division: 3
print(10 % 3)   # Modulo (remainder): 1
```

### 2. Float (Decimal Numbers)
```python
# Creating floats
price = 19.99
height = 5.8
temperature = -3.5

# Methods for floats
number = 3.14159

# Round to decimal places
print(round(number, 2))  # Output: 3.14

# Convert to integer
print(int(number))  # Output: 3

# Check if it's a whole number
print(number.is_integer())  # Output: False

# Get the format
print(f"{number:.2f}")  # Output: 3.14

# Mathematical operations
print(10.5 + 5.2)   # Addition: 15.7
print(10.5 - 5.2)   # Subtraction: 5.3
print(10.5 * 2)     # Multiplication: 21.0
print(10.5 / 3)     # Division: 3.5
```

### 3. String (Text)
```python
# Creating strings
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# Useful String Methods
text = "Python Programming"

# Length
print(len(text))  # Output: 19

# Convert case
print(text.lower())   # Output: "python programming"
print(text.upper())   # Output: "PYTHON PROGRAMMING"
print(text.capitalize())  # Output: "Python programming"

# Find and replace
print(text.find("Python"))  # Output: 0 (found at index 0)
print(text.replace("Python", "Java"))  # Output: "Java Programming"

# Split and join
words = text.split()  # Output: ['Python', 'Programming']
print(" ".join(words))  # Output: "Python Programming"

# Check if string contains
print("Python" in text)  # Output: True

# Strip whitespace
text_with_spaces = "  Hello  "
print(text_with_spaces.strip())  # Output: "Hello"

# Count occurrences
text = "banana"
print(text.count("a"))  # Output: 3

# String formatting
name = "Bob"
age = 25
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old")
# Output: "My name is Bob and I am 25 years old"
```

### 4. Boolean (True/False)
```python
# Boolean values
is_student = True
is_adult = False

# Boolean operations
print(True and False)   # Output: False
print(True or False)    # Output: True
print(not True)         # Output: False

# Comparisons return boolean
print(5 > 3)    # Output: True
print(5 == 5)   # Output: True
print(5 != 3)   # Output: True
print(5 < 3)    # Output: False

# Converting to boolean
print(bool(1))      # Output: True
print(bool(0))      # Output: False
print(bool("text")) # Output: True
print(bool(""))     # Output: False
```

### 5. List (Collection of Items)
```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing elements (indexing starts at 0)
print(fruits[0])    # Output: "apple"
print(fruits[-1])   # Output: "orange" (last item)

# List methods
fruits = ["apple", "banana", "orange"]

# Add items
fruits.append("grape")  # Add at end: ["apple", "banana", "orange", "grape"]
fruits.insert(1, "mango")  # Add at position 1

# Remove items
fruits.remove("banana")  # Remove by value
fruits.pop()  # Remove last item
fruits.pop(0)  # Remove at index 0

# Length and searching
print(len(fruits))  # Output: number of items
print("apple" in fruits)  # Output: True/False
print(fruits.index("apple"))  # Output: 0

# Sorting and reversing
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Sorts in place: [1, 1, 3, 4, 5]
numbers.reverse()  # Reverses in place

# Slicing
print(fruits[0:2])  # Output: first 2 items
print(fruits[1:])   # Output: from index 1 to end
print(fruits[:2])   # Output: first 2 items
print(fruits[::2])  # Output: every 2nd item

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # Output: 3

# Loop through list
for fruit in fruits:
    print(fruit)
```

### 6. Tuple (Immutable List)
```python
# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Need comma for single item

# Accessing elements (same as list)
print(coordinates[0])  # Output: 10
print(coordinates[-1])  # Output: 20

# Tuples are immutable (cannot change)
# coordinates[0] = 15  # This would cause an error!

# Useful tuple methods
numbers = (1, 2, 3, 2, 4, 2)

# Count occurrences
print(numbers.count(2))  # Output: 3

# Find index
print(numbers.index(3))  # Output: 2

# Unpack tuple
x, y = coordinates  # x=10, y=20

# Length
print(len(coordinates))  # Output: 2

# Loop through tuple
for color in colors:
    print(color)
```

### 7. Dictionary (Key-Value Pairs)
```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "gpa": 3.8,
    "city": "New York"
}

# Accessing values
print(student["name"])  # Output: "Alice"
print(student.get("age"))  # Output: 20
print(student.get("grade", "N/A"))  # Default value if key not found

# Adding and updating items
student["grade"] = "A"  # Add new key-value pair
student["age"] = 21    # Update existing value

# Removing items
del student["city"]  # Remove by key
student.pop("grade")  # Remove and return value

# Useful dictionary methods
print(student.keys())    # Output: dict_keys(['name', 'age', 'gpa'])
print(student.values())  # Output: dict_values(['Alice', 21, 3.8])
print(student.items())   # Output: key-value pairs as tuples

# Check if key exists
print("name" in student)  # Output: True
print("grade" in student)  # Output: False

# Length
print(len(student))  # Output: number of key-value pairs

# Loop through dictionary
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

# Clear all items
student.clear()  # Dictionary becomes empty
```

### 8. Set (Unique Unordered Collection)
```python
# Creating sets
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates empty dict, not set

# Add and remove items
fruits.add("grape")
fruits.remove("banana")  # Error if not found
fruits.discard("mango")  # No error if not found

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1 | set2)  # Union: {1, 2, 3, 4}
print(set1 & set2)  # Intersection: {2, 3}
print(set1 - set2)  # Difference: {1}
print(set1 ^ set2)  # Symmetric difference: {1, 4}

# Useful set methods
print(len(set1))      # Output: 3
print(2 in set1)      # Output: True
print(set1.issubset(set2))  # Check if subset
print(set1.issuperset(set2))  # Check if superset

# Loop through set
for item in fruits:
    print(item)
```
---

## Class Objects

### What is a Class?
A class is a blueprint for creating objects. It defines what data and behaviors (methods) objects of that class will have.

### Basic Class Structure
```python
# Define a simple class
class Student:
    # This runs when you create a new object
    def __init__(self, name, age, grade):
        # self refers to the object itself
        # These are attributes (data)
        self.name = name
        self.age = age
        self.grade = grade
    
    # This is a method (behavior)
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    def pass_exam(self):
        self.grade = "A"
        return f"{self.name} passed the exam!"

# Create objects from the class
student1 = Student("Alice", 20, "B")
student2 = Student("Bob", 19, "C")

# Access attributes
print(student1.name)   # Output: "Alice"
print(student2.age)    # Output: 19

# Call methods
print(student1.introduce())      # Output: "Hi, I'm Alice, 20 years old"
print(student2.pass_exam())      # Output: "Bob passed the exam!"

# Modify attributes
student1.grade = "A"
print(student1.grade)  # Output: "A"
```

### Class with Different Types of Methods
```python
class Car:
    # Class variable (shared by all objects)
    total_cars = 0
    
    def __init__(self, brand, model, year):
        # Instance variables (unique to each object)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        Car.total_cars += 1
    
    # Instance method (operates on specific object)
    def accelerate(self, increase):
        self.speed += increase
        return f"{self.brand} {self.model} speed: {self.speed} km/h"
    
    def brake(self):
        self.speed = max(0, self.speed - 10)
        return f"{self.brand} {self.model} stopped"
    
    # Class method (operates on class itself)
    @classmethod
    def total_cars_created(cls):
        return f"Total cars created: {cls.total_cars}"
    
    # Static method (doesn't need self or cls)
    @staticmethod
    def is_vintage(year):
        return year < 2000

# Create objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 1995)
# Use instance methods
print(car1.accelerate(50))  # Output: "Toyota Camry speed: 50 km/h"
print(car1.brake())          # Output: "Toyota Camry stopped"
# Use class method
print(Car.total_cars_created())  # Output: "Total cars created: 2"

# Use static method
print(Car.is_vintage(1995))  # Output: True
print(Car.is_vintage(2020))  # Output: False
```

### Inheritance (Classes Inheriting from Other Classes)
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child class inherits from parent
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof Woof!"
    
    def fetch(self):
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())   # Output: "Buddy barks: Woof Woof!"
print(dog.fetch())   # Output: "Buddy fetches the ball"
print(cat.speak())   # Output: "Whiskers meows: Meow!"

# Check inheritance
print(isinstance(dog, Animal))  # Output: True
print(isinstance(dog, Dog))     # Output: True
```

---

## Data Structures

### 1. Stack (LIFO - Last In First Out)
```python
# Stack implementation using list
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """View top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)

# Using the stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())  # Output: 30
print(stack.pop())   # Output: 30, removes it
print(stack.size())  # Output: 2
```

### 2. Queue (FIFO - First In First Out)
```python
# Queue implementation using list
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to back of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """View front item without removing"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)

# Using the queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())    # Output: 1
print(queue.dequeue()) # Output: 1, removes it
print(queue.size())    # Output: 2
```

### 3. Linked List
```python
# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # First node
    
    def append(self, data):
        """Add item to end of list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        """Print all items"""
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items))
    
    def insert_at_beginning(self, data):
        """Add item at start"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def remove(self, data):
        """Remove item by value"""
        if not self.head:
            return
        
        # If head needs to be removed
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Using the linked list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30

ll.insert_at_beginning(5)
ll.display()  # Output: 5 -> 10 -> 20 -> 30

ll.remove(20)
ll.display()  # Output: 5 -> 10 -> 30
```

### 4. Binary Search Tree
```python
# Node class for binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # Left child
        self.right = None  # Right child

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Add value to tree"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper function for recursive insertion"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Check if value exists in tree"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper function for recursive search"""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """Visit nodes in order: Left, Root, Right"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper function for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Using the binary search tree
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

print(bst.search(30))  # Output: True
print(bst.search(100)) # Output: False
print(bst.inorder_traversal())  # Output: [20, 30, 40, 50, 70]
```

### 5. Hash Table / Dictionary
```python
# Simple Hash Table implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists
    
    def _hash(self, key):
        """Generate hash for key"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Add or update key-value pair"""
        index = self._hash(key)
        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Add new key-value pair
        self.table[index].append((key, value))
    
    def search(self, key):
        """Find value by key"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Remove key-value pair"""
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

# Using the hash table
ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 20)
ht.insert("city", "New York")

print(ht.search("name"))  # Output: "Alice"
print(ht.search("age"))   # Output: 20
ht.delete("age")
print(ht.search("age"))   # Output: None
```

---

## Understanding OOPS

### What is Object-Oriented Programming?
OOP is a programming approach that organizes code into objects that contain both data (attributes) and functions (methods).

### Four Pillars of OOP

### 1. **Encapsulation** (Bundling data and methods together)


```python
class BankAccount:
    def __init__(self, account_holder, balance):
        # Private attributes (by convention, prefix with _)
        self.__account_holder = account_holder
        self.__balance = balance
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount}"
        return "Invalid amount"
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn: ${amount}"
        return "Insufficient funds or invalid amount"
    
    # Public method to check balance
    def get_balance(self):
        return self.__balance
    
    # Getter method
    def get_account_holder(self):
        return self.__account_holder

# Using encapsulation 


account = BankAccount("John", 1000)
print(account.deposit(500))      # Output: "Deposited: $500"
print(account.withdraw(200))     # Output: "Withdrawn: $200"
print(account.get_balance())     # Output: 1300


# Cannot directly access private attributes
# print(account.__balance)  # This would cause an error!
```

### 2. **Inheritance** (Child class inherits from parent class)
```python
# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model}"
    
    def start(self):
        return "Engine started"

# Child class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def display_info(self):
        return f"{self.brand} {self.model} ({self.doors} doors)"
    
    def open_trunk(self):
        return "Trunk opened"

# Another child class
class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar
    
    def wheelie(self):
        return "Performing a wheelie!"

# Using inheritance
car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", False)

print(car.display_info())     # Output: "Toyota Camry (4 doors)"
print(car.start())            # Output: "Engine started"
print(car.open_trunk())       # Output: "Trunk opened"

print(motorcycle.display_info())  # Output: "Harley-Davidson Sportster"
print(motorcycle.wheelie())       # Output: "Performing a wheelie!"
```

### 3. **Polymorphism** (Same method, different behaviors)
```python
# Parent class
class Animal:
    def speak(self):
        pass

# Different child classes
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo! Moo!"

# Function that works with any Animal
def make_sound(animal):
    print(animal.speak())

# Create different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Same method, different behaviors!
make_sound(dog)   # Output: "Woof! Woof!"
make_sound(cat)   # Output: "Meow! Meow!"
make_sound(cow)   # Output: "Moo! Moo!"

# Using isinstance to check type
print(isinstance(dog, Animal))  # Output: True
print(isinstance(dog, Dog))     # Output: True
```

### 4. **Abstraction** (Hiding complex details)
```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    """Abstract class that defines the interface"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by child classes"""
        pass
    
    def describe(self):
        """Concrete method in abstract class"""
        return f"This is a {self.__class__.__name__}"

# Concrete class implementing abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Using abstraction
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(circle.describe())      # Output: "This is a Circle"
print(f"Circle area: {circle.area()}")        # Output: "Circle area: 78.5"
print(f"Circle perimeter: {circle.perimeter()}")  # Output: "Circle perimeter: 31.4"

print(rectangle.describe())   # Output: "This is a Rectangle"
print(f"Rectangle area: {rectangle.area()}")      # Output: "Rectangle area: 24"
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: "Rectangle perimeter: 20"

# Cannot create object of abstract class directly
# shape = Shape()  # This would cause an error!
```

---

## Practical Example: Complete School Management System

```python
# Example combining all concepts

from abc import ABC, abstractmethod

# Abstract base class
class Person(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @abstractmethod
    def role(self):
        pass
    
    def get_name(self):
        return self.__name

# Encapsulation example
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grade = grade
        self.__marks = []
    
    def add_marks(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
        else:
            print("Invalid mark!")
    
    def get_average(self):
        if self.__marks:
            return sum(self.__marks) / len(self.__marks)
        return 0
    
    def role(self):
        return f"{self.get_name()} is a student"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject
    
    def role(self):
        return f"{self.get_name()} teaches {self.__subject}"

class Principal(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def role(self):
        return f"{self.get_name()} is the principal"

# School system using polymorphism
class School:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def add_person(self, person):
        self.people.append(person)
    
    def display_roles(self):
        print(f"=== {self.name} ===")
        for person in self.people:
            print(person.role())

# Using the system
school = School("ABC High School")

student1 = Student("Alice", 15, "S001", "10th")
student1.add_marks(85)
student1.add_marks(90)
student1.add_marks(88)

student2 = Student("Bob", 16, "S002", "11th")
student2.add_marks(75)
student2.add_marks(80)

teacher = Teacher("Mr. Smith", 40, "Mathematics")
principal = Principal("Dr. Johnson", 50)

school.add_person(student1)
school.add_person(student2)
school.add_person(teacher)
school.add_person(principal)

school.display_roles()
print(f"\nAlice's average: {student1.get_average()}")  # Output: 87.67
print(f"Bob's average: {student2.get_average()}")      # Output: 77.5
```

---
## Summary Table

| Concept | What is it? | Example |
|---------|-----------|---------|
| Data Type | Classification of data | int, str, list, dict |
| Method | Function belonging to an object | `str.upper()`, `list.append()` |
| Class | Blueprint for objects | `class Student:` |
| Object | Instance of a class | `student1 = Student()` |
| Attribute | Data stored in object | `self.name`, `self.age` |
| Inheritance | Child class gets parent's features | `class Dog(Animal):` |
| Polymorphism | Same method, different behaviors | `speak()` different for each animal |
| Encapsulation | Hide internal details | Private attributes with `__` |
| Abstraction | Hide complexity | Abstract methods in ABC |
| Data Structure | Organized data storage | Stack, Queue, Tree, LinkedList |

---