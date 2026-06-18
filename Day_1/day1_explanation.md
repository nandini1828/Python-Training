# Python Concepts Assignment

## Overview

This project demonstrates the fundamental concepts of Python programming including Data Types, Classes and Objects, Data Structures, and Object-Oriented Programming (OOP).

---

# 1. Data Types

Data types define the kind of value a variable can store.

### Programs Covered

- Type Conversion
- Mutable vs Immutable Objects
- Basic Data Types

Files and program explanations

- `data_types/data_types_examples.py`: Contains three demo functions:
  - `type_conversion_demo()` — shows converting a string to `int` and converting an integer salary to `float`; prints values and their runtime types.
  - `mutable_immutable_demo()` — demonstrates immutability of integers (reassignment creates a new object) and mutability of lists via `append()`.
  - `data_types_demo()` — creates variables of types `str`, `int`, `float`, and `bool` and prints their types using `type()`.

How to run the Data Types examples:

```bash
python3 python_prac/data_types/data_types_examples.py
```

### Concepts Learned

- int
- float
- str
- bool
- type casting
- mutability

---

# 2. Classes and Objects

A class is a blueprint for creating objects.

### Programs Covered

- Student Class
- Bank Account Class

### Concepts Learned

- Class creation
- Constructors
- Instance variables
- Methods
- Object creation

Files and program explanations

- `class_objects/class_objects_examples.py`: Contains two classes and a `demo()` runner:
  - `Student` — simple class with `__init__` taking `name` and `roll_no`, and a `display()` method that prints the student's details.
  - `BankAccount` — has a `balance` attribute, `deposit(amount)` method (validates positive amounts), and `show_balance()` method.
  - `demo()` — creates example instances (`Student("Vamshi", 101)` and `BankAccount(1000)`), exercises the methods, and prints outputs.

How to run the Classes and Objects example:

```bash
python3 python_prac/class_objects/class_objects_examples.py
```

---

# 3. Data Structures

Data structures are used to organize and store data efficiently.

### Programs Covered

- List Operations
- Tuple Operations
- Dictionary Operations
- Set Operations

### Concepts Learned

- List manipulation
- Tuple indexing
- Dictionary key-value pairs
- Set uniqueness

Files and program explanations

- `data_structures/data_structures_examples.py`: Provides four small demos:
  - `list_demo()` — shows `append()` and `remove()` on a list of integers.
  - `tuple_demo()` — demonstrates tuple indexing and `len()`.
  - `dictionary_demo()` — creates a dictionary for an `employee`, adds a new key, and prints the mapping.
  - `set_demo()` — shows `add()` and the uniqueness property of sets (duplicates are ignored).

How to run the Data Structures examples:

```bash
python3 python_prac/data_structures/data_structures_examples.py
```

---

# 4. Object-Oriented Programming (OOP)

OOP helps organize code into reusable and maintainable components.

### Programs Covered

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### Concepts Learned

- Data hiding
- Code reusability
- Method overriding
- Abstract classes

Files and program explanations

- `oops/oops_examples.py`: Demonstrates common OOP patterns:
  - **Encapsulation**: `Employee` class stores `__salary` as a private attribute and exposes `get_salary()` to access it.
  - **Inheritance**: `Animal` base class with `sound()` and a `Dog` subclass that adds `bark()`.
  - **Polymorphism**: `Bird` and `Fish` classes both implement `move()`; the demo iterates over instances and calls `move()` to show different behaviors.
  - **Abstraction**: `Shape` is an abstract base class with an abstract `area()` method; `Square` implements `area()`.
  - `demo()` — runs each of the above examples and prints results.

How to run the OOP examples:

```bash
python3 python_prac/oops/oops_examples.py
```

---

# Conclusion

This project provides a practical understanding of Python fundamentals and OOP principles. The programs demonstrate how Python handles data, structures information, and supports object-oriented design for building scalable applications.
