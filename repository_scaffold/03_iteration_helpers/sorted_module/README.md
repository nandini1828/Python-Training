# Sorted Module

## Overview

The built-in `sorted()` function returns a new sorted list from any iterable without modifying the original data. It supports ascending and descending order, custom sorting using the `key` parameter, and works with strings, tuples, dictionaries, sets, and custom objects.

Unlike the `list.sort()` method, `sorted()` creates a new sorted collection, preserving the original iterable.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand how `sorted()` works.
- Sort numbers, strings, and dictionaries.
- Sort in ascending and descending order.
- Use the `key` parameter for custom sorting.
- Apply sorting techniques in real-world scenarios.

---

# Prerequisites

- Lists
- Tuples
- Dictionaries
- Strings
- Iteration Helpers

---

# Folder Structure

```text
sorted_module/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
sorted(iterable)

sorted(iterable, reverse=True)

sorted(iterable, key=function)
```

---

# Example

```python
numbers = [5, 2, 9, 1]

print(sorted(numbers))
```

Output

```
[1, 2, 5, 9]
```

---

# Sort in Descending Order

```python
sorted(numbers, reverse=True)
```

---

# Custom Sorting

```python
names = ["Ganesh", "Rahul", "Priya"]

sorted(names, key=len)
```

---

# Enterprise Applications

- Report generation
- Ranking systems
- Leaderboards
- Data analysis
- Database result ordering
- Employee and student management
- Product catalog sorting

---

# Advantages

- Preserves the original iterable.
- Works with any iterable.
- Supports custom sorting.
- Highly readable and efficient.

---

# Best Practices

✔ Use `sorted()` when you need to keep the original data unchanged.

✔ Use the `key` parameter instead of complex comparison logic.

✔ Choose meaningful sorting criteria.

---

# Common Mistakes

❌ Confusing `sorted()` with `list.sort()`.

❌ Assuming the original iterable is modified.

❌ Forgetting to specify `reverse=True` for descending order.

---

# Interview Questions

1. What is the difference between `sorted()` and `list.sort()`?
2. What does the `key` parameter do?
3. Can `sorted()` sort dictionaries?
4. Does `sorted()` modify the original iterable?

---

# Practice Exercises

1. Sort numbers in ascending order.
2. Sort numbers in descending order.
3. Sort strings alphabetically.
4. Sort names by length.
5. Sort dictionary keys.

---

# Summary

The `sorted()` function is one of Python's most powerful built-in utilities for ordering data. It is flexible, efficient, and widely used in data processing, analytics, reporting, and enterprise software development.