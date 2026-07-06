# Nested Comprehensions

---

# Learning Objectives

After completing this chapter, you will understand:

- Nested comprehensions
- Matrix flattening
- Matrix transposition
- Cartesian products
- Coordinate generation

---

# What are Nested Comprehensions?

Nested comprehensions contain multiple `for` clauses.

They are commonly used for working with multidimensional data.

---

# Flattening a Matrix

```python
matrix = [
    [1, 2],
    [3, 4],
]

flat = [
    value
    for row in matrix
    for value in row
]
```

Output

```
[1, 2, 3, 4]
```

---

# Matrix Transpose

```python
transpose = [
    [
        row[column]
        for row in matrix
    ]
    for column in range(len(matrix[0]))
]
```

---

# Cartesian Product

```python
letters = ["A", "B"]
numbers = [1, 2]

pairs = [
    (letter, number)
    for letter in letters
    for number in numbers
]
```

Output

```
[
    ("A", 1),
    ("A", 2),
    ("B", 1),
    ("B", 2),
]
```

---

# Coordinate Grid

```python
coordinates = [
    (row, column)
    for row in range(3)
    for column in range(3)
]
```

---

# Enterprise Examples

- Image processing
- Spreadsheet generation
- Grid creation
- Matrix operations
- Data visualization

---

# Best Practices

✔ Avoid deeply nested comprehensions that reduce readability.

✔ Consider normal loops if the logic becomes complex.

✔ Keep nested comprehensions focused on transformation.

---

# Summary

Nested comprehensions provide a compact way to process multidimensional collections and generate structured data.