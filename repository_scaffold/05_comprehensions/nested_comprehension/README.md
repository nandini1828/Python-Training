# Nested Comprehension

Nested comprehensions represent loops inside loops.

Example:

```python
[item for row in matrix for item in row]
```

This package includes helpers for:

- Transposing rectangular matrices.
- Building ordered pairs.
- Flattening nested lists.
- Filtering each row independently.
- Creating multiplication tables.

Nested comprehensions can become dense quickly. Use them when the shape is
familiar, such as flattening a matrix. Prefer normal loops when the logic needs
comments, validation, or multiple branches.
