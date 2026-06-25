# Dunder Methods

## What this folder contains
This folder explains dunder methods, which are Python's special methods that begin and end with double underscores. These methods allow classes to behave more like built-in Python objects.

## What the code demonstrates
The dunder examples show how classes can define behavior for:
- string conversion with __str__
- object representation with __repr__
- comparison and equality behavior

## Why this is important
Dunder methods are a key part of Python's object model and are used heavily in framework and library development.

## Example
```python
from dunder_methods.dunder_utils import DunderDemo

person = DunderDemo("Ada", 37)
print(str(person))
print(repr(person))
```

## What a viewer should understand after reading this folder
A viewer should understand that dunder methods let custom classes integrate naturally with Python's built-in behavior.
