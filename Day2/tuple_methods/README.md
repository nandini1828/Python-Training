# Tuple Methods

## Concept Overview
This package highlights tuple-based patterns for fixed collections and structured data.

## Why It Exists
Tuples are immutable and useful for encoding relationships that should not change unexpectedly.

## Real World Use Cases
- Coordinates and records
- Returning multiple values from functions
- Immutable configuration objects

## Example Code
```python
from tuple_methods.tuple_utils import tuple_to_dict

mapping = tuple_to_dict(("a", "b"), (1, 2))
```

## Expected Output
A dictionary synthesized from two tuples.
