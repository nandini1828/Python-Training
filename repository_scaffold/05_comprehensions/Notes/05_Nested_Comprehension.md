# Nested Comprehension

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand nested comprehension syntax.
- Flatten nested lists.
- Build pairs from nested loops.
- Transpose rectangular matrices.
- Recognize when nested comprehensions hurt readability.
- Replace complex nested comprehensions with normal loops.

---

# Introduction

A nested comprehension contains more than one `for` clause.

It is useful when working with nested data such as:

- Lists of lists
- Tables
- Matrices
- User records with lists inside them
- Product categories with multiple tags

Example

```python
matrix = [[1, 2], [3, 4]]
flat = [item for row in matrix for item in row]
```

Output

```text
[1, 2, 3, 4]
```

---

# Reading Nested Comprehensions

Nested comprehensions are read in the same order as normal loops.

Comprehension:

```python
[item for row in matrix for item in row]
```

Equivalent loop:

```python
result = []

for row in matrix:
    for item in row:
        result.append(item)
```

The first `for` is the outer loop. The second `for` is the inner loop.

---

# Flattening a Matrix

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
]

flat = [item for row in matrix for item in row]
```

Output

```text
[1, 2, 3, 4, 5, 6]
```

---

# Building Ordered Pairs

```python
numbers = [1, 2, 3]
pairs = [
    (x, y)
    for x in numbers
    for y in numbers
    if x != y
]
```

Output

```text
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

This kind of structure appears in combinations, comparisons, and test cases.

---

# Transposing a Matrix

Transposing means converting rows into columns.

```python
matrix = [
    [1, 2],
    [3, 4],
]

transpose = [
    [row[index] for row in matrix]
    for index in range(len(matrix[0]))
]
```

Output

```text
[[1, 3], [2, 4]]
```

This works correctly only when every row has the same length.

---

# Multiplication Table

```python
size = 3
table = [
    [row * column for column in range(1, size + 1)]
    for row in range(1, size + 1)
]
```

Output

```text
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

Nested comprehensions can express table-like structures naturally.

---

# Real-World Example: Product Tags

```python
products = [
    {"name": "Laptop", "tags": ["electronics", "office"]},
    {"name": "Chair", "tags": ["office", "furniture"]},
]

tags = [
    tag
    for product in products
    for tag in product["tags"]
]
```

Output

```text
['electronics', 'office', 'office', 'furniture']
```

Use a set comprehension if only unique tags are needed.

---

# When Nested Comprehensions Become Too Much

This is hard to read:

```python
result = [x.strip().lower() for row in rows for x in row if x and len(x) > 2]
```

A normal loop may be clearer:

```python
result = []

for row in rows:
    for value in row:
        if value and len(value) > 2:
            result.append(value.strip().lower())
```

Readable code is better than compressed code.

---

# Common Mistakes

## Mistake 1: Reading the loop order backwards

Remember:

```python
[item for row in matrix for item in row]
```

matches:

```python
for row in matrix:
    for item in row:
        ...
```

## Mistake 2: Transposing ragged matrices

```python
[[1, 2], [3]]
```

Rows have different lengths, so transpose logic can fail.

## Mistake 3: Overusing nesting

If the comprehension needs explanation, a loop may be better.

---

# Best Practices

- Use nested comprehensions for simple nested data transformations.
- Keep each expression short.
- Validate matrix shape before transposing.
- Split long comprehensions across multiple lines.
- Prefer normal loops when branching or error handling is needed.

---

# Summary

Nested comprehensions are powerful but should be used carefully.

They are best for familiar patterns like flattening, pairs, and matrix
transforms. When the logic becomes dense, normal loops are more maintainable.
