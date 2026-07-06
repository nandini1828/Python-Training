# Comprehensions

> "A comprehension is a loop with a destination."

---

# Module Overview

Comprehensions are a compact Python syntax for building collections from
iterables. They are useful when the goal is clear: transform values, filter
values, or build a new collection from existing data.

This module covers list, dictionary, set, and nested comprehensions. The code is
split into reusable `utils.py` helpers, runnable `demo.py` files, topic
READMEs, notes, and tests.

---

# Learning Objectives

After completing this module, you will be able to:

- Convert simple loops into readable comprehensions.
- Choose list, dictionary, or set output based on the data you need.
- Use filtering conditions inside comprehensions.
- Flatten one level of nested data.
- Build dictionaries from pairs, transformations, and filters.
- Avoid nested comprehensions when they harm readability.
- Test comprehension helpers like ordinary functions.

---

# When to Use Comprehensions

Use a comprehension when:

- You are building a new collection.
- The expression is short and readable.
- The loop has one clear transformation or filter.

Prefer a regular loop when:

- You need multiple steps with names.
- You need error handling inside the loop.
- The comprehension becomes difficult to scan.

---

# How to Run

```bash
python3 repository_scaffold/05_comprehensions/main.py
```

Run tests when `pytest` is installed:

```bash
python3 -m pytest repository_scaffold/05_comprehensions/tests
```
