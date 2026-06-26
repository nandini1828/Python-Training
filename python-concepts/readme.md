# Python Concepts Training Project

## Overview

This project is designed to provide hands-on practice with core Python concepts including:

* Introspection
* Type Casting
* Truthiness
* Collections (List, Set, Queue)
* Dictionaries & JSON
* Object-Oriented Programming
* Object Memory (`__dict__`)
* Recursion
* Type Annotations
* Pytest Unit Testing

The project is organized into modules based on concepts, making the code modular, readable, and easy to maintain.

---

# Project Structure

```text
python-concepts/
│
├── collections/
│   └── exercises.py
│
├── dictionary/
│   ├── dictionaries_json.py
│   └── exercises.py
│
├── Introspection/
│   ├── introspection.py
│   ├── argparse.py
│   └── exercises.py
│
├── oop_memory/
│   ├── oop_memory.py
│   └── exercises.py
│
├── type_casting/
│   ├── type_casting.py
│   └── exercises.py
│
├── tests/
│   ├── test_casting.py
│   ├── test_collections.py
│   ├── test_introspect.py
│   ├── test_json.py
│   └── test_objects.py
│
└── main.py
```

---

# Folder Explanation

## Introspection

### Purpose

Learn how Python objects can inspect themselves at runtime.

### Files

#### introspection.py

Contains functions such as:

```python
list_public_attributes()
get_methods_and_docs()
```

Concepts covered:

* dir()
* type()
* id()
* **doc**
* Introspection
* Public vs Private attributes

---

#### argparse.py

Demonstrates command-line argument parsing.

Concepts covered:

* argparse
* CLI applications
* ArgumentParser
* parse_args()

Example:

```bash
python app.py --name John
```

---

#### exercises.py

Contains practice implementations for introspection exercises.

---

# type_casting

### Purpose

Understand type checking, type conversion, and truthiness.

### Files

#### type_casting.py

Concepts covered:

```python
type()
isinstance()
```

Difference between:

```python
type(obj)
```

and

```python
isinstance(obj, Class)
```

---

#### exercises.py

Contains:

```python
safe_cast()
count_truthy_falsy()
```

Concepts covered:

* Type conversion
* Exception handling
* Truthy values
* Falsy values

Examples:

```python
safe_cast("123", int)
```

```python
count_truthy_falsy(
    [0, "", 1, "hello"]
)
```

---

# collections

### Purpose

Learn Lists, Sets, and custom data structures.

### Files

#### exercises.py

Contains:

### SimpleQueue

Implementation of Queue using List.

Concepts:

* FIFO
* append()
* pop(0)
* Classes
* Objects

---

### merge_tags()

Concepts:

* Set Comprehension
* Union
* Intersection
* Difference
* Duplicate Removal

Example:

```python
merge_tags(
    ["Python", "AI"],
    ["python", "ML"]
)
```

---

# dictionary

### Purpose

Learn Dictionary operations and JSON navigation.

### Files

#### dictionaries_json.py

Contains examples of:

```python
get()
items()
keys()
values()
update()
copy()
setdefault()
```

Concepts:

* Dictionary Methods
* Nested Dictionaries
* JSON Structures

---

#### exercises.py

Contains:

### query_json()

Navigate nested dictionaries using dot notation.

Example:

```python
query_json(
    data,
    "user.profile.name"
)
```

---

### word_count()

Counts word frequency.

Concepts:

* Dictionaries
* String Manipulation
* get()
* Frequency Counting

---

# oop_memory

### Purpose

Understand how Python objects store data.

### Files

#### oop_memory.py

Concepts:

* Classes
* Objects
* self
* Composition
* **dict**

Example:

```python
student.__dict__
```

---

#### exercises.py

Contains:

### deconstruct_object()

Recursively converts custom objects into dictionaries.

Example:

```python
Computer(
    "Dell",
    CPU(8)
)
```

becomes:

```python
{
    "brand": "Dell",
    "cpu": {
        "cores": 8
    }
}
```

Concepts:

* Recursion
* Object Serialization
* Composition
* **dict**

---

# main.py

### Purpose

Acts as the entry point of the application.

Runs demonstrations from all modules.

Modules executed:

* Introspection
* Type Casting
* Collections
* Dictionary
* OOP Memory

Run:

```bash
python main.py
```

---

# tests

### Purpose

Contains unit tests written using Pytest.

---

## test_introspect.py

Tests:

```python
list_public_attributes()
```

---

## test_casting.py

Tests:

```python
safe_cast()
count_truthy_falsy()
```

---

## test_collections.py

Tests:

```python
SimpleQueue()
merge_tags()
```

---

## test_json.py

Tests:

```python
query_json()
word_count()
```

---

## test_objects.py

Tests:

```python
deconstruct_object()
```

---

# Running the Project

## Run Main Program

```bash
python main.py
```

---

# Running Tests

Run all tests:

```bash
pytest tests -v
```

Run a single file:

```bash
pytest tests/test_json.py
```

---

# Concepts Covered

## Python Fundamentals

* Variables
* Data Types
* Lists
* Sets
* Dictionaries

---

## Introspection

* dir()
* type()
* id()
* **doc**

---

## Type System

* type()
* isinstance()
* Type Casting
* Type Hints

---

## Collections

* List Methods
* Set Methods
* Queue Implementation

---

## JSON

* Nested Dictionaries
* Query Engine
* Serialization Concepts

---

## OOP

* Classes
* Objects
* self
* Composition
* **dict**

---

## Advanced Topics

* Recursion
* Object Deconstruction
* Serialization

---

## Testing

* Pytest
* Assertions
* Unit Testing

---

# Learning Outcome

After completing this project, you should be able to:

* Inspect any Python object.
* Understand Python's object model.
* Work confidently with Lists, Sets, Dictionaries, and JSON.
* Implement custom data structures.
* Write modular and readable code.
* Add type annotations.
* Write Pytest test cases.
* Understand object memory using `__dict__`.
* Convert complex objects into serializable structures.
* Follow professional Python project organization practices.
