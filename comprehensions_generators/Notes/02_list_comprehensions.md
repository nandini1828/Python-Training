# List Comprehensions

---

# Learning Objectives

After completing this chapter, you will understand:

- List comprehension syntax
- Filtering
- Transformations
- Nested list comprehensions
- Best practices

---

# What is a List Comprehension?

A list comprehension creates a new list using a single expression.

General syntax

```python
[
    expression
    for item in iterable
]
```

---

# Basic Example

```python
numbers = [1, 2, 3, 4]

squares = [
    number ** 2
    for number in numbers
]
```

Output

```
[1, 4, 9, 16]
```

---

# Filtering

```python
evens = [
    number
    for number in range(10)
    if number % 2 == 0
]
```

Output

```
[0, 2, 4, 6, 8]
```

---

# String Transformation

```python
words = [
    "Python",
    "Django",
]

upper = [
    word.upper()
    for word in words
]
```

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

# Conditional Expression

```python
labels = [
    "Even"
    if number % 2 == 0
    else "Odd"
    for number in range(6)
]
```

---

# Best Practices

✔ Keep comprehensions short.

✔ Avoid deeply nested expressions.

✔ Prefer comprehensions over simple loops that build collections.

---

# Summary

List comprehensions provide a concise and readable way to transform and filter iterable data.