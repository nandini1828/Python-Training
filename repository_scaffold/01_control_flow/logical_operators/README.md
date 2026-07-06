# Logical Operators

## Overview

Logical operators are used to combine multiple conditions into a single boolean expression. They are fundamental in decision-making, validation, authentication, filtering, and business rule implementation.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the purpose of logical operators.
- Combine multiple conditions effectively.
- Write complex conditional expressions.
- Apply logical operators in real-world scenarios.
- Improve readability and maintainability of decision-making code.

---

# Topics Covered

- AND Operator
- OR Operator
- NOT Operator
- Operator Precedence
- Truth Tables
- Real-world Examples
- Best Practices

---

# Folder Structure

```
logical_operators/
│
├── README.md
├── __init__.py
├── demo.py
└── utils.py
```

---

# AND Operator

Returns `True` only if **both** conditions are true.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
```

---

# OR Operator

Returns `True` if **at least one** condition is true.

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")
```

---

# NOT Operator

Reverses a boolean value.

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

# Best Practices

- Keep conditions readable.
- Avoid deeply nested logical expressions.
- Use parentheses for clarity.
- Prefer descriptive variable names.

---

# Summary

Logical operators allow multiple conditions to be evaluated together, making Python programs more expressive and powerful.