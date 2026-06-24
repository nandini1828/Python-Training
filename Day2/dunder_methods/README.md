# Dunder Methods

## Concept Overview
This package demonstrates Python's special methods, also known as dunder methods, which allow objects to behave like built-in types.

## Why It Exists
Dunder methods make classes more Pythonic and enable rich behaviors such as string conversion, equality comparison, and ordering.

## Real World Use Cases
- Custom value objects
- Domain models
- Data containers and comparables

## Example Code
```python
from dunder_methods.dunder_utils import DunderDemo

person = DunderDemo("Ada", 37)
print(repr(person))
print(str(person))
```

## Expected Output
A human-readable string and a developer-friendly representation of the object.
