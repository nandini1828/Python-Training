# If-Else Module

## Overview

The `if`, `elif`, and `else` statements are Python's primary decision-making constructs. They allow programs to execute different blocks of code based on one or more conditions.

This module provides practical examples and reusable utility functions to understand and implement conditional logic.

---

# Learning Objectives

After completing this module, you will be able to:

- Use `if`, `elif`, and `else` statements effectively.
- Write nested conditional statements.
- Handle multiple decision paths.
- Apply conditional logic in real-world applications.
- Write clean and maintainable decision-making code.

---

# Topics Covered

- Basic `if`
- `if-else`
- `if-elif-else`
- Nested `if`
- Comparison operators
- Decision trees
- Enterprise examples

---

# Folder Structure

```
if_else/
│
├── README.md
├── __init__.py
├── demo.py
└── utils.py
```

---

# Basic Syntax

## if

```python
if condition:
    statements
```

## if-else

```python
if condition:
    statements
else:
    statements
```

## if-elif-else

```python
if condition1:
    statements

elif condition2:
    statements

else:
    statements
```

---

# Example

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Adult
```

---

# Real-World Applications

- User Authentication
- ATM Systems
- Student Grade Calculation
- Loan Approval
- Shopping Discounts
- Employee Bonus Calculation
- Traffic Signal Systems
- Inventory Validation

---

# Best Practices

- Keep conditions simple.
- Avoid unnecessary nesting.
- Use meaningful variable names.
- Handle all possible cases.
- Prefer readability over clever code.

---

# Files

### demo.py

Contains executable examples demonstrating different `if-else` scenarios.

### utils.py

Contains reusable utility functions that implement common decision-making logic.

---

# Summary

The `if`, `elif`, and `else` statements form the foundation of decision making in Python. Mastering these constructs enables you to build dynamic and intelligent applications that respond appropriately to different inputs and conditions.