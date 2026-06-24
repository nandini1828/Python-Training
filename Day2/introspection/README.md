# Introspection

## Concept Overview
This package shows how Python can inspect objects at runtime to discover behavior and structure.

## Why It Exists
Introspection is essential for debugging, framework development, and building reusable tooling.

## Real World Use Cases
- Debugging object state
- Building generic serializers
- Inspecting plugin systems

## Example Code
```python
from introspection.introspection_utils import inspect_object, query_json

summary = inspect_object([1, 2, 3])
value = query_json({"user": {"name": "Ada"}}, "user.name")
```

## Expected Output
Structured metadata about the inspected object and a value extracted from a nested JSON-like structure.
