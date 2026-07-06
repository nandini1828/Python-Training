# Iterators & Generators

> "Iteration is Python's way of asking for the next value only when it is needed."

---

# Module Overview

This module explains how Python produces values lazily through iterators,
generator functions, and generator expressions.

The examples focus on behavior that matters in real programs:

- How `iter` and `next` work.
- How custom iterator objects store state.
- How generator functions pause and resume.
- How generator expressions avoid building full lists.
- How to test lazy code by collecting only the values you need.

---

# Learning Objectives

After completing this module, you will be able to:

- Implement and consume iterator objects.
- Explain `__iter__` and `__next__`.
- Use `yield` to create generator functions.
- Build lazy transformations with generator expressions.
- Batch and filter streams of values.
- Recognize when lazy evaluation is better than eager collection creation.

---

# How to Run

```bash
python3 repository_scaffold/06_iterators_generators/main.py
```

Run tests when `pytest` is installed:

```bash
python3 -m pytest repository_scaffold/06_iterators_generators/tests
```
