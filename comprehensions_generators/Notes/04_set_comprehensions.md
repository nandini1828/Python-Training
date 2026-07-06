# Set Comprehensions

---

# Learning Objectives

After completing this chapter, you will understand:

- What set comprehensions are
- Removing duplicates
- Filtering values
- Transforming data
- Practical applications

---

# What is a Set Comprehension?

A set comprehension creates a **set** using a single expression.

General syntax

```python
{
    expression
    for item in iterable
}
```

Unlike list comprehensions, duplicate values are automatically removed.

---

# Basic Example

```python
numbers = [1, 2, 2, 3, 4, 4]

unique = {
    number
    for number in numbers
}
```

Output

```
{1, 2, 3, 4}
```

---

# Lowercase Words

```python
words = [
    "Python",
    "python",
    "DJANGO",
]

result = {
    word.lower()
    for word in words
}
```

Output

```
{"python", "django"}
```

---

# Filtering

```python
even_numbers = {
    number
    for number in range(10)
    if number % 2 == 0
}
```

Output

```
{0, 2, 4, 6, 8}
```

---

# Unique First Letters

```python
words = [
    "Python",
    "Programming",
    "Django",
]

letters = {
    word[0]
    for word in words
}
```

---

# Enterprise Examples

- Removing duplicate usernames
- Unique email domains
- Extracting unique categories
- Removing duplicate IDs
- Unique tags from datasets

---

# Best Practices

✔ Use set comprehensions when uniqueness is required.

✔ Avoid converting lists to sets after creation if a set comprehension is sufficient.

✔ Keep expressions simple and readable.

---

# Summary

Set comprehensions provide a concise and efficient way to build collections containing only unique values.