# While Loop

## Overview

The `while` loop repeatedly executes a block of code as long as a specified condition evaluates to `True`. Unlike a `for` loop, which iterates over an iterable, a `while` loop is condition-driven.

It is commonly used when the number of iterations is not known beforehand.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the working of while loops.
- Write condition-controlled loops.
- Prevent infinite loops.
- Use counters effectively.
- Apply while loops in real-world scenarios.

---

# Prerequisites

- Variables
- Conditional Statements
- Boolean Expressions

---

# Folder Structure

```text
while_loop/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
while condition:
    # statements
```

---

# Execution Flow

```text
      Start
        │
        ▼
 Evaluate Condition
        │
   ┌────┴────┐
   │         │
 True      False
   │         │
   ▼         ▼
Execute     End
   │
   ▼
Update Condition
   │
   └──────────────► Repeat
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# Enterprise Applications

- Waiting for user input
- Polling APIs
- Monitoring services
- Background workers
- Queue processing
- Retry mechanisms
- Network communication

---

# Advantages

- Ideal when iteration count is unknown.
- Flexible.
- Easy to understand.
- Supports complex conditions.

---

# Best Practices

✔ Always update the loop variable.

✔ Avoid infinite loops.

✔ Keep loop bodies concise.

✔ Prefer `for` loops when the iteration count is known.

---

# Common Mistakes

❌ Forgetting to update the condition.

❌ Creating infinite loops.

❌ Using `while True` unnecessarily.

---

# Interview Questions

1. Difference between `for` and `while`?
2. What is an infinite loop?
3. When should you use a while loop?
4. How can an infinite loop be stopped?

---

# Practice Exercises

1. Print numbers from 1 to 50.
2. Reverse a number.
3. Find factorial.
4. Generate Fibonacci series.
5. Validate user input.

---

# Summary

The `while` loop is a powerful condition-controlled looping construct that is widely used in automation, monitoring systems, user interaction, and background processing.