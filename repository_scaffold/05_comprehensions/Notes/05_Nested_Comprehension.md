# Nested Comprehension

Use loops inside loops in a single expression.

Flattening example:

```python
matrix = [[1, 2], [3, 4]]
flat = [item for row in matrix for item in row]
```

Nested comprehensions are read from left to right in loop order:

```python
[item for row in matrix for item in row]
```

This matches:

```python
result = []
for row in matrix:
    for item in row:
        result.append(item)
```

Use nested comprehensions sparingly. Once validation or branching becomes
important, a regular loop communicates intent more clearly.
