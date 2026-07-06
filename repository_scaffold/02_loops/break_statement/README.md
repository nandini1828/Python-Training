# Break Statement

## Overview

The `break` statement is a loop control statement that immediately terminates the execution of the nearest enclosing loop. Once a `break` statement is encountered, control transfers to the first statement following the loop.

It can be used with both `for` and `while` loops.

The `break` statement is commonly used in enterprise applications to stop processing once the required result has been found, reducing unnecessary computation and improving performance.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand how the `break` statement works.
- Use `break` with `for` loops.
- Use `break` with `while` loops.
- Exit loops efficiently.
- Improve performance using early termination.

---

# Prerequisites

- for Loop
- while Loop
- Conditional Statements

---

# Folder Structure

```text
break_statement/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
for item in iterable:
    if condition:
        break
```

```python
while condition:
    if condition:
        break
```

---

# Execution Flow

```text
Loop Starts
     │
     ▼
Execute Statement
     │
     ▼
Break Condition?
   │      │
  No     Yes
   │      │
   ▼      ▼
Next    Exit Loop
Iteration
```

---

# Example

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    if number == 30:
        break

    print(number)
```

Output

```
10
20
```

---

# Enterprise Applications

- Search operations
- Database record lookup
- API polling
- Authentication
- File parsing
- Queue processing
- Event handling
- Network communication

---

# Advantages

- Stops unnecessary iterations.
- Improves execution speed.
- Simplifies loop logic.
- Saves system resources.

---

# Best Practices

✔ Use `break` only when early termination is required.

✔ Keep break conditions clear.

✔ Avoid multiple break statements in the same loop whenever possible.

---

# Common Mistakes

❌ Using `break` outside a loop.

❌ Creating unreachable code.

❌ Breaking too early.

---

# Interview Questions

1. What is the purpose of `break`?
2. Difference between `break` and `continue`?
3. Can `break` be used inside nested loops?
4. What happens after a `break` executes?

---

# Practice Exercises

1. Search an element in a list.
2. Stop reading when a sentinel value is found.
3. Exit after successful login.
4. Stop processing after the first error.
5. Find the first prime number.

---

# Summary

The `break` statement provides an efficient mechanism for terminating loops early, making Python programs faster, cleaner, and easier to maintain.