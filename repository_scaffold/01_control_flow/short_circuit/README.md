# Short-Circuit Evaluation

## Overview

Short-circuit evaluation is an optimization technique used by Python when evaluating logical expressions involving the `and` and `or` operators.

Instead of evaluating every condition, Python stops evaluating as soon as the final result is already known.

This improves:

- Performance
- Readability
- Safety
- Memory efficiency

It is one of the most commonly used concepts in enterprise Python applications.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand short-circuit evaluation.
- Explain how `and` works internally.
- Explain how `or` works internally.
- Avoid unnecessary computation.
- Prevent runtime errors.
- Write cleaner and safer Python code.

---

# Prerequisites

- if-else
- Truthy and Falsy values
- Logical Operators

---

# Folder Structure

```text
short_circuit/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# How `and` Works

Python evaluates expressions from left to right.

```python
A and B
```

If `A` is `False`, Python immediately returns `False`.

It never evaluates `B`.

Example:

```python
x = 0

if x != 0 and 10 / x > 2:
    print("Valid")
```

Since `x != 0` is `False`, `10/x` is **never executed**.

This prevents a `ZeroDivisionError`.

---

# How `or` Works

```python
A or B
```

If `A` is already `True`, Python skips evaluating `B`.

Example

```python
username = "Ganesh"

result = username or "Guest"
```

Since `username` is truthy, `"Guest"` is never evaluated.

---

# Execution Flow

## AND

```text
Condition A
     │
     ▼
False ? ---- Yes ----> Stop
     │
     No
     ▼
Evaluate Condition B
```

## OR

```text
Condition A
     │
     ▼
True ? ----- Yes ----> Stop
     │
     No
     ▼
Evaluate Condition B
```

---

# Advantages

- Faster execution
- Avoids unnecessary computation
- Prevents runtime errors
- Cleaner code
- Used heavily in production systems

---

# Real-world Applications

- Login validation
- Configuration loading
- API response validation
- Database query handling
- File processing
- Authentication
- Feature flags
- AI workflow routing

---

# Best Practices

- Put inexpensive conditions first.
- Put risky operations last.
- Use short-circuiting to prevent exceptions.
- Don't rely on side effects.

---

# Common Mistakes

❌ Assuming every condition is evaluated.

❌ Placing expensive operations first.

❌ Ignoring truthy/falsy behavior.

---

# Interview Questions

1. What is short-circuit evaluation?
2. Difference between `and` and `or`?
3. Why is short-circuiting useful?
4. How does it prevent exceptions?
5. Give real-world examples.

---

# Practice Exercises

- Safe division
- Login authentication
- Default configuration loader
- API response validator
- Shopping cart validator

---

# Summary

Short-circuit evaluation is a fundamental optimization technique in Python. It improves performance, enhances safety, and is widely used in enterprise software to avoid unnecessary computations and runtime errors.