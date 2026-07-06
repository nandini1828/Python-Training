# Loop Foundations

The **Loop Foundations** module introduces Python's looping constructs and control flow mechanisms. It is designed to help learners understand how to iterate over data, control loop execution, and write clean, efficient, and maintainable looping logic.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand the purpose of loops
* Use `for` loops effectively
* Use `while` loops correctly
* Iterate over different Python collections
* Control loop execution using `break`, `continue`, and `pass`
* Understand `for-else` and `while-else`
* Apply looping concepts to real-world programming scenarios
* Write clean, Pythonic looping code

---

# Module Structure

```text
loop_foundations/
│
├── __init__.py
├── utils.py
├── loops.py
├── break_continue.py
├── for_else_while_else.py
├── demo.py
├── cli.py
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_for_loops.md
│   ├── 03_while_loops.md
│   ├── 04_break_continue_pass.md
│   ├── 05_for_else_while_else.md
│   ├── 06_best_practices.md
│   ├── 07_interview_questions.md
│   └── 08_exercises.md
│
└── tests/
    ├── __init__.py
    ├── test_loops.py
    ├── test_break_continue.py
    └── test_for_else.py
```

---

# Topics Covered

## Basic Loops

* `for` loops
* `while` loops
* Nested loops
* `range()`

## Iterating Collections

* Lists
* Tuples
* Sets
* Dictionaries
* Strings

## Loop Control Statements

* `break`
* `continue`
* `pass`

## Advanced Loop Features

* `for-else`
* `while-else`
* Searching
* Retry logic
* Prime number detection

---

# Source Files

## `loops.py`

Covers:

* Collection iteration
* String iteration
* Dictionary iteration
* `range()`
* Factorial
* Fibonacci sequence
* Countdown
* Multiplication tables
* Nested loops
* Searching
* Aggregation

---

## `break_continue.py`

Covers:

* `break`
* `continue`
* `pass`
* Validation
* Filtering
* Order processing
* Duplicate detection
* Username validation

---

## `for_else_while_else.py`

Covers:

* `for-else`
* `while-else`
* Searching
* Login attempts
* Retry logic
* Queue processing
* Inventory validation
* Prime number checking

---

# Running the Demo

Run the complete demonstration:

```bash
python -m loop_foundations.demo
```

---

# Using the CLI

List available topics:

```bash
python -m loop_foundations.cli --list
```

Run the loop demonstrations:

```bash
python -m loop_foundations.cli --topic loops
```

Run while loop demonstrations:

```bash
python -m loop_foundations.cli --topic while
```

Run break/continue/pass demonstrations:

```bash
python -m loop_foundations.cli --topic break
```

Run for-else/while-else demonstrations:

```bash
python -m loop_foundations.cli --topic else
```

---

# Running the Tests

Run all tests:

```bash
pytest
```

Run only this module:

```bash
pytest tests/
```

Run with verbose output:

```bash
pytest -v
```

Generate a coverage report:

```bash
pytest --cov=loop_foundations --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=loop_foundations --cov-report=html
```

Open the generated report:

```text
htmlcov/index.html
```

---

# Learning Path

Study the module in this order:

1. Introduction
2. `for` Loops
3. `while` Loops
4. `break`, `continue`, and `pass`
5. `for-else` and `while-else`
6. Best Practices
7. Interview Questions
8. Exercises
9. Demo Programs
10. Unit Tests

---

# Best Practices

* Prefer `for` loops when iterating over collections.
* Use `while` loops when repetition depends on a condition.
* Keep loop bodies small and readable.
* Use meaningful variable names.
* Use `break` only when an early exit is required.
* Use `continue` to skip invalid data.
* Avoid modifying a collection while iterating over it.
* Add type hints and docstrings to public functions.
* Write unit tests for all public APIs.

---

# Skills You Will Gain

By completing this module, you will be able to:

* Write efficient loop-based programs
* Process lists, dictionaries, strings, tuples, and sets
* Use loop control statements confidently
* Implement searching and filtering algorithms
* Build retry and polling logic
* Apply Python loop best practices
* Write clean, maintainable, and testable code

---

# Prerequisites

Before starting this module, you should understand:

* Variables
* Data Types
* Operators
* Basic Functions

---

# Next Module

After completing **Loop Foundations**, continue with:

**Iteration Helpers**

Topics include:

* `range()`
* `enumerate()`
* `zip()`
* `zip_longest()`
* `reversed()`
* `sorted()`
* `any()`
* `all()`

These utilities make iteration more expressive, readable, and Pythonic.



