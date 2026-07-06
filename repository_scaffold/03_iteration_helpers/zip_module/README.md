# Zip Helper

## Overview

The built-in `zip()` function combines two or more iterables into a single iterator of tuples. Each tuple contains one element from each iterable at the same position.

The iteration stops as soon as the shortest iterable is exhausted.

`zip()` is widely used for processing related datasets, pairing values, creating dictionaries, generating reports, and handling structured data.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand how `zip()` works.
- Combine multiple iterables.
- Iterate over paired values.
- Convert zipped data into dictionaries.
- Unzip data using the unpacking operator (`*`).

---

# Prerequisites

- Lists
- Tuples
- Dictionaries
- for Loop
- Iteration Helpers

---

# Folder Structure

```text
zip_helper/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
zip(iterable1, iterable2)

zip(iterable1, iterable2, iterable3)
```

---

# Example

```python
names = ["Ganesh", "Rahul", "Priya"]
marks = [95, 90, 88]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output

```
Ganesh 95
Rahul 90
Priya 88
```

---

# Unzipping

```python
pairs = [(1, "A"), (2, "B"), (3, "C")]

numbers, letters = zip(*pairs)
```

---

# Enterprise Applications

- Merging datasets
- CSV processing
- Report generation
- API response mapping
- Database imports
- Data transformation
- Configuration pairing

---

# Advantages

- Clean and readable.
- Memory efficient.
- Works with multiple iterables.
- Simplifies parallel iteration.

---

# Best Practices

✔ Ensure related iterables have matching lengths when required.

✔ Use `zip()` instead of manual indexing for parallel iteration.

✔ Convert to `list()` only when necessary.

---

# Common Mistakes

❌ Assuming `zip()` continues to the longest iterable.

❌ Forgetting that `zip()` returns an iterator.

❌ Modifying iterables while iterating.

---

# Interview Questions

1. What does `zip()` return?
2. What happens if iterables have different lengths?
3. How do you unzip data?
4. Can `zip()` combine more than two iterables?

---

# Practice Exercises

1. Pair names with marks.
2. Create a dictionary using `zip()`.
3. Combine three lists.
4. Unzip a list of tuples.

---

# Summary

The `zip()` function provides an elegant and efficient way to iterate over multiple iterables simultaneously, making it a valuable tool for data processing and structured programming.