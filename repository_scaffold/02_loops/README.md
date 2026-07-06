# Python Loops

## Overview

Loops are one of the fundamental control flow mechanisms in Python. They allow a block of code to be executed repeatedly, making programs efficient, concise, and scalable.

Python provides two primary looping constructs:

- **for loop** – Used for iterating over iterable objects.
- **while loop** – Used for repeated execution based on a condition.

Loops are heavily used in enterprise applications for:

- Data processing
- File handling
- Database operations
- API integrations
- Machine Learning pipelines
- Automation scripts
- Network programming

---

# Learning Objectives

After completing this module, you will be able to:

- Understand loop fundamentals.
- Differentiate between `for` and `while` loops.
- Control loop execution using `break`, `continue`, and `pass`.
- Understand loop termination.
- Use loop `else` clauses effectively.
- Write efficient looping logic.

---

# Topics Covered

- for Loop
- while Loop
- break Statement
- continue Statement
- pass Statement
- Loop else Clause

---

# Folder Structure

```text
02_loops/
│
├── Notes/
├── for_loop/
├── while_loop/
├── break_statement/
├── continue_statement/
├── pass_statement/
├── loop_else/
│
├── tests/
│
├── README.md
├── __init__.py
├── main.py
├── logging_config.py
└── json_query.py
```

---

# Comparison

| Feature | for | while |
|----------|-----|--------|
| Iterable based | ✅ | ❌ |
| Condition based | ❌ | ✅ |
| Counter required | No | Usually |
| Infinite loop possible | Rare | Yes |

---

# Enterprise Applications

- Reading CSV files
- Processing API responses
- ETL pipelines
- Log analysis
- Batch processing
- Web scraping
- Automation
- Database migration

---

# Best Practices

- Prefer `for` loops when iterating over collections.
- Use `while` loops only when iteration count is unknown.
- Avoid infinite loops.
- Keep loop bodies simple.
- Use `break` and `continue` sparingly.

---

# Common Mistakes

- Forgetting to update loop variables.
- Modifying collections while iterating.
- Creating infinite loops.
- Excessive nesting.

---

# Interview Questions

1. Difference between `for` and `while`.
2. What is loop else?
3. Difference between break and continue?
4. Can for loop become infinite?
5. When should while loops be used?

---

# Summary

Loops enable repetitive execution efficiently and form the backbone of automation, data processing, and algorithm implementation in Python.