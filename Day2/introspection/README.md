# Introspection

## What this folder contains
This folder explains introspection, which means looking inside an object to understand what it is and what it can do.

## What the code demonstrates
The introspection utilities show how to:
- inspect an object and identify its type
- list its methods and attributes
- extract documentation strings from Python objects
- understand how Python exposes internal information at runtime

## Why this is important
Introspection is useful for debugging, learning Python, and building tools that work with unknown objects dynamically.

## Example
```python
from introspection.introspection_utils import inspect_object

summary = inspect_object([1, 2, 3])
print(summary["kind"])
print(summary["methods"])
```

## What a viewer should understand after reading this folder
A viewer should understand that Python can reveal information about objects and help developers explore them interactively.
