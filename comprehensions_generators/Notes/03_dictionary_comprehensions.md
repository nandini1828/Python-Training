# Dictionary Comprehensions

---

# Learning Objectives

After completing this chapter, you will understand:

- Dictionary comprehension syntax
- Filtering dictionaries
- Transforming keys and values
- Practical use cases

---

# What is a Dictionary Comprehension?

Dictionary comprehensions create dictionaries dynamically.

General syntax

```python
{
    key: value
    for item in iterable
}
```

---

# Basic Example

```python
squares = {
    number: number ** 2
    for number in range(5)
}
```

Output

```
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16,
}
```

---

# Word Length Mapping

```python
words = [
    "Python",
    "Django",
]

lengths = {
    word: len(word)
    for word in words
}
```

---

# Filtering

```python
positive = {
    key: value
    for key, value in data.items()
    if value > 0
}
```

---

# Dictionary Inversion

```python
inverse = {
    value: key
    for key, value in mapping.items()
}
```

---

# Enterprise Examples

- Employee salary mapping
- Product catalog creation
- API response formatting
- Configuration loading
- Database record mapping

---

# Best Practices

✔ Keep key expressions simple.

✔ Ensure keys remain unique.

✔ Use filtering to remove unnecessary data.

---

# Summary

Dictionary comprehensions provide an elegant way to create mappings while keeping code concise and readable.