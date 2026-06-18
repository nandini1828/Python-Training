# Python Learning Notes

## Methods Useful for Data Types

### String Methods
- strip() → Remove spaces from beginning and end
- upper() → Convert to uppercase
- lower() → Convert to lowercase
- replace(old, new) → Replace text
- split() → Convert string to list

### List Methods
- append() → Add element at end
- insert(index, value) → Add at specific position
- remove(value) → Remove value
- pop() → Remove last element
- extend(iterable) → Add multiple elements
- sort() → Sort list
- reverse() → Reverse list

### Tuple Methods
- count(value) → Count occurrences
- index(value) → Find position

### Set Methods
- add() → Add element
- update() → Add multiple elements
- remove() → Remove element
- union() → Combine sets
- intersection() → Common elements
- difference() → Unique elements

### Dictionary Methods
- get(key) → Get value
- keys() → Get all keys
- values() → Get all values
- items() → Get key-value pairs
- update() → Update dictionary
- pop(key) → Remove key

---

## Class Objects

### Class
A blueprint used to create objects.

python class Mobile:     pass 

### Object
An instance of a class.

python mobile1 = Mobile() 

### Constructor

python def __init__(self, brand, price): 

- Runs automatically when an object is created.
- Initializes object data.

### Instance Variables

python self.brand = brand self.price = price 

Store data specific to an object.

### Methods

python def display(self):     print(self.brand) 

Functions inside a class.

### self
Refers to the current object.

### str()

python def __str__(self): 

Controls how an object is displayed when printed.

---

## Data Structures

### List
- Ordered
- Mutable
- Allows duplicates

python numbers = [10, 20, 30] 

### Tuple
- Ordered
- Immutable
- Allows duplicates

python data = (10, 20, 30) 

### Set
- Unordered
- Mutable
- No duplicates

python skills = {"Python", "SQL"} 

### Dictionary
- Key-Value pairs
- Mutable
- Keys are unique

python student = {"name": "Bhavya"} 

---

## OOP Fundamentals

### Class
Blueprint for objects.

### Object
Instance of a class.

### Inheritance
Child class inherits properties and methods from parent class.

python class SmartPhone(Mobile):     pass 

### Polymorphism
Same method name, different behavior.

python Car.start() ElectricCar.start() 

### Encapsulation
Hide data using private variables.

python self.__balance 

### Abstraction
Show only essential functionality and hide implementation details.

python class Vehicle:     def move(self):         pass 

### OOP Flow

text Class   ↓ Object   ↓ Constructor (__init__)   ↓ Instance Variables   ↓ Methods   ↓ Inheritance   ↓ Polymorphism   ↓ Encapsulation   ↓ Abstraction 