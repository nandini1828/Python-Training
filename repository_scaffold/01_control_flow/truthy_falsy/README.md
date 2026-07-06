# Truthy and Falsy

## Overview

In Python, every object has an inherent truth value. Objects evaluate to either **True** or **False** when used in conditions such as `if`, `while`, logical expressions, and boolean operations.

Understanding truthy and falsy values is essential for writing concise, readable, and Pythonic code.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand Truthy and Falsy values.
- Identify objects that evaluate to False.
- Write cleaner conditional statements.
- Avoid unnecessary comparisons with `True` and `False`.
- Apply Truthy/Falsy concepts in real-world applications.

---

# Topics Covered

- Boolean Context
- Truthy Values
- Falsy Values
- bool() Function
- Empty Collections
- None
- Real-world Examples
- Best Practices

---

# Folder Structure

```
truthy_falsy/
│
├── README.md
├── __init__.py
├── demo.py
└── utils.py
```

---

# Falsy Values

The following values evaluate to `False`:

```python
False
None
0
0.0
0j
''
""
[]
()
{}
set()
range(0)
```

---

# Truthy Values

Everything else evaluates to `True`.

Examples:

```python
1
-10
3.14
"Python"
[1, 2, 3]
{"name": "Ganesh"}
(10,)
{1, 2}
True
```

---

# Example

```python
name = "Ganesh"

if name:
    print("Valid Name")
```

Output

```
Valid Name
```

---

# Real-World Applications

- User Input Validation
- Login Systems
- API Response Validation
- Database Query Results
- File Handling
- Configuration Validation

---

# Best Practices

- Prefer `if value:` instead of `if value == True`.
- Prefer `if not value:` to check empty objects.
- Use `is None` when checking for `None`.
- Avoid comparing collections with `== []` or `== {}`.

---

# Files

### demo.py

Contains executable examples demonstrating Truthy and Falsy behavior.

### utils.py

Contains reusable helper functions related to boolean evaluation.

---

# Summary

Truthy and Falsy values allow Python to write elegant and readable conditional logic without unnecessary comparisons.