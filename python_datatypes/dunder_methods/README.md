# Dunder Methods

## Concept Overview

The `dunder_methods` package demonstrates custom Python object behavior using special methods such as `__getitem__`, `__len__`, `__repr__`, `__eq__`, and `__getattr__`.

## Why It Exists

Special methods allow developers to create objects that behave like built-in containers, support equality, and expose dynamic attribute access in enterprise systems.

## Real World Use Cases

- Immutable data containers with custom indexing
- Domain-specific value objects
- Configuration wrappers and context objects
- Operator overloading for mathematical models

## Example Code

```python
from python_datatypes.dunder_methods import ImmutableMatrix, NamingContext

matrix = ImmutableMatrix(((1, 2), (3, 4)))
print(matrix)
print(matrix.transpose())

context = NamingContext({"project": "Python Datatypes", "version": "1.0.0"})
print(context.project)
```

## Expected Output

```text
ImmutableMatrix(((1, 2), (3, 4)))
ImmutableMatrix(((1, 3), (2, 4)))
Python Datatypes
```
