# Any and All Module

## Overview

The built-in `any()` and `all()` functions evaluate iterable objects based on their truth values.

- `any()` returns `True` if at least one element is truthy.
- `all()` returns `True` only if every element is truthy.

These functions simplify validation, filtering, decision-making, and data verification in Python applications.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the difference between `any()` and `all()`.
- Evaluate truthiness in iterables.
- Validate collections efficiently.
- Apply `any()` and `all()` in practical scenarios.
- Improve readability by replacing manual validation loops.

---

# Prerequisites

- Boolean Values
- Truthy and Falsy Objects
- Lists
- Tuples
- Iteration Helpers

---

# Folder Structure

```text
any_all/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
any(iterable)

all(iterable)
```

---

# Example

```python
numbers = [0, 0, 5]

print(any(numbers))
```

Output

```
True
```

```python
numbers = [2, 4, 6]

print(all(number % 2 == 0 for number in numbers))
```

Output

```
True
```

---

# Enterprise Applications

- Form validation
- Authentication checks
- Permission verification
- Data quality validation
- Configuration validation
- Business rule enforcement
- API response verification

---

# Advantages

- Simple and expressive.
- Eliminates manual loops.
- Improves readability.
- Works with any iterable.

---

# Best Practices

✔ Use `any()` when one successful condition is sufficient.

✔ Use `all()` when every condition must be satisfied.

✔ Prefer generator expressions for better memory efficiency.

---

# Common Mistakes

❌ Confusing the behavior of `any()` and `all()`.

❌ Forgetting that empty iterables return `False` for `any()` and `True` for `all()`.

❌ Using unnecessary loops instead of built-in functions.

---

# Interview Questions

1. What is the difference between `any()` and `all()`?
2. What happens when they receive an empty iterable?
3. Can they be used with generator expressions?
4. What types of iterables do they support?

---

# Practice Exercises

1. Check if any student passed.
2. Verify that all passwords meet a rule.
3. Validate positive numbers.
4. Check if any filename ends with `.txt`.

---

# Summary

The `any()` and `all()` functions provide concise and efficient ways to evaluate iterable objects, making them essential tools for validation and decision-making in Python.