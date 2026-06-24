# Python Data Types & Introspection - Overview

## 1. Python Objects

In Python, everything is an object. Every value such as integers, strings, lists, and functions is an instance of a class.

Examples:

- `10` → `int`
- `"Hello"` → `str`
- `[1, 2, 3]` → `list`

---

## 2. Introspection

Introspection is the ability to inspect objects at runtime.

### `type()`
Returns the type of an object.

```python
type(10)
```

Output:

```python
<class 'int'>
```

### `id()`
Returns the unique identifier (memory reference) of an object.

```python
id(10)
```

### `dir()`
Returns all available attributes and methods of an object.

```python
dir(list)
```

### `isinstance()`
Checks whether an object belongs to a specific class.

```python
isinstance(10, int)
```

### `callable()`
Checks whether an object can be called like a function.

```python
callable(print)
```

---

## 3. Dunder Methods

Dunder (Double Underscore) methods are special methods used internally by Python.

Examples:

```python
a + b
```

Internally becomes:

```python
a.__add__(b)
```

Common dunder methods:

- `__add__()`
- `__sub__()`
- `__eq__()`
- `__len__()`
- `__str__()`
- `__repr__()`

---

## 4. Type Casting

Type casting converts one data type into another.

Examples:

```python
int("10")
float("12.5")
str(100)
```

Safe casting uses exception handling to prevent application crashes.

---

## 5. Lists

Lists are ordered and mutable collections.

Common methods:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`
- `copy()`

Example:

```python
numbers = [1, 2]
numbers.append(3)
```

---

## 6. Tuples

Tuples are ordered but immutable collections.

Common methods:

- `count()`
- `index()`

Example:

```python
data = (1, 2, 2, 3)
```

---

## 7. Sets

Sets store unique elements and support mathematical set operations.

Common methods:

- `add()`
- `remove()`
- `discard()`
- `union()`
- `intersection()`
- `difference()`
- `symmetric_difference()`

Example:

```python
{1, 2} | {2, 3}
```

---

## 8. Dictionaries

Dictionaries store data as key-value pairs.

Common methods:

- `get()`
- `setdefault()`
- `update()`
- `keys()`
- `values()`
- `items()`
- `pop()`

Example:

```python
student = {
    "name": "Bhavya",
    "age": 22
}
```

---

## 9. JSON & Nested Dictionaries

JSON data is represented in Python using dictionaries and lists.

Example:

```python
{
    "user": {
        "profile": {
            "name": "Bhavya"
        }
    }
}
```

Nested values can be accessed using path traversal.

---

## 10. Classes & Objects

A class is a blueprint used to create objects.

Example:

```python
class Student:
    pass
```

Creating an object:

```python
student = Student()
```

---

## 11. Composition

Composition represents a "has-a" relationship between classes.

Example:

```python
class CPU:
    pass

class Computer:
    pass
```

A computer has a CPU.

---

## 12. self

`self` refers to the current object instance.

Example:

```python
def display(self):
    print(self.name)
```

Python automatically passes the current object as `self`.

---

## 13. __dict__

Every object stores its attributes inside a dictionary called `__dict__`.

Example:

```python
student.__dict__
```

Output:

```python
{
    "name": "Bhavya",
    "grades": [90, 95, 85]
}
```

---

## 14. __doc__

`__doc__` contains the documentation string of modules, classes, and functions.

Example:

```python
Student.__doc__
```

Useful for documentation and introspection.

---

## 15. Type Annotations

Type annotations improve readability and help static analysis tools.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Benefits:

- Better readability
- IDE support
- Easier maintenance
- Static type checking

---

## 16. argparse

`argparse` is used to accept command-line arguments.

Example:

```python
python main.py --section queue
```

Benefits:

- Flexible execution
- User-friendly CLI
- Real-world application usage

---

## 17. Pytest

Pytest is a testing framework used to validate code behavior.

Example:

```python
def test_add():
    assert 2 + 2 == 4
```

Run tests:

```bash
pytest
```

Benefits:

- Automated testing
- Regression prevention
- Improved code quality

---

## Key Takeaways

- Everything in Python is an object.
- Introspection helps inspect objects at runtime.
- Collections are fundamental data structures.
- Classes and objects enable object-oriented programming.
- Type hints improve maintainability.
- argparse provides command-line flexibility.
- Pytest ensures correctness through automated testing.
- Python provides powerful built-in tools for writing clean, reusable, and maintainable code.