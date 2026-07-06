# Iteration Helpers

The **Iteration Helpers** module introduces Python's built-in helper functions that make iteration simpler, cleaner, and more Pythonic. These functions reduce boilerplate code and improve readability when working with collections and sequences.

This module builds upon the concepts learned in the **Loop Foundations** module and prepares learners for **Comprehensions**, **Iterators**, and **Generators**.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand the purpose of Python's iteration helper functions
* Generate numeric sequences using `range()`
* Retrieve indices while iterating using `enumerate()`
* Iterate over multiple collections simultaneously using `zip()`
* Handle uneven collections using `zip_longest()`
* Reverse collections using `reversed()`
* Sort collections using `sorted()`
* Validate collections using `any()` and `all()`
* Write cleaner, more maintainable Python code

---

# Module Structure

```text
iteration_helpers/
│
├── __init__.py
├── utils.py
├── range_examples.py
├── enumerate_examples.py
├── zip_examples.py
├── reversed_sorted.py
├── any_all.py
├── demo.py
├── cli.py
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_range.md
│   ├── 03_enumerate.md
│   ├── 04_zip.md
│   ├── 05_reversed_sorted.md
│   ├── 06_any_all.md
│   ├── 07_interview_questions.md
│   └── 08_exercises.md
│
└── tests/
    ├── __init__.py
    ├── test_range_examples.py
    ├── test_enumerate_examples.py
    ├── test_zip_examples.py
    ├── test_reversed_sorted.py
    └── test_any_all.py
```

---

# Topics Covered

## `range()`

* `range(stop)`
* `range(start, stop)`
* `range(start, stop, step)`
* Reverse ranges
* Even numbers
* Odd numbers
* Batch processing

---

## `enumerate()`

* Basic enumeration
* Custom starting index
* Enumerating strings
* Enumerating dictionaries
* Ranking
* Report generation

---

## `zip()`

* Parallel iteration
* Combining collections
* Creating dictionaries
* Unzipping
* Matrix transposition
* `zip_longest()`

---

## `reversed()` and `sorted()`

* Reverse iteration
* Sorting numbers
* Sorting strings
* Case-insensitive sorting
* Custom sorting with `key`
* Sorting dictionaries and records

---

## `any()` and `all()`

* Boolean evaluation
* Data validation
* Membership testing
* Score validation
* File validation
* User validation

---

# Running the Demo

Run the complete demonstration:

```bash
python -m iteration_helpers.demo
```

---

# Using the CLI

List available topics:

```bash
python -m iteration_helpers.cli --list
```

Run `range()` examples:

```bash
python -m iteration_helpers.cli --topic range
```

Run `enumerate()` examples:

```bash
python -m iteration_helpers.cli --topic enumerate
```

Run `zip()` examples:

```bash
python -m iteration_helpers.cli --topic zip
```

Run `reversed()` and `sorted()` examples:

```bash
python -m iteration_helpers.cli --topic sorted
```

Run `any()` and `all()` examples:

```bash
python -m iteration_helpers.cli --topic any_all
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
pytest --cov=iteration_helpers --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=iteration_helpers --cov-report=html
```

---

# Best Practices

* Use `range()` for numeric sequences.
* Use `enumerate()` instead of `range(len(...))` when you need both the index and value.
* Use `zip()` for parallel iteration over multiple collections.
* Use `zip_longest()` when collections have different lengths.
* Prefer `sorted()` over modifying collections in place when you need a new sorted sequence.
* Use `any()` and `all()` to simplify validation logic.
* Keep iteration code readable and expressive.

---

# Learning Path

Study this module in the following order:

1. Introduction
2. `range()`
3. `enumerate()`
4. `zip()`
5. `reversed()` and `sorted()`
6. `any()` and `all()`
7. Interview Questions
8. Exercises
9. Demo
10. Tests

---

# Skills You Will Gain

By completing this module, you will be able to:

* Write more Pythonic iteration code
* Process multiple collections efficiently
* Generate numeric sequences
* Build readable reports with indices
* Merge and transform data
* Sort collections using custom rules
* Validate collections using concise built-in functions

---

# Prerequisites

Before starting this module, you should be comfortable with:

* Variables
* Data Types
* Control Flow
* Loop Foundations

---

# Next Module

After completing **Iteration Helpers**, continue with **Iteration Safety**, where you'll learn:

* Safe list iteration
* Avoiding modification traps
* Dictionary iteration
* Safe dictionary access
* `defaultdict`
* Set membership and performance


