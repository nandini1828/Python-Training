# Comprehensions & Generators

The **Comprehensions & Generators** module introduces Python's most powerful tools for writing concise, efficient, and memory-friendly code. It covers comprehensions for transforming collections, the iterator protocol that powers Python's iteration model, and generators for lazy evaluation and streaming data.

This module builds upon the concepts learned in **Control Flow**, **Loop Foundations**, and **Iteration Helpers**, preparing learners for advanced Python development and enterprise applications.

---

# Learning Objectives

After completing this module, you will be able to:

* Write clean and Pythonic list comprehensions
* Build dictionaries using dictionary comprehensions
* Create unique collections using set comprehensions
* Understand and write nested comprehensions
* Explain the Iterator Protocol
* Implement custom iterator classes
* Build generators using `yield`
* Use generator expressions for memory-efficient processing
* Understand lazy evaluation
* Build streaming data pipelines

---

# Module Structure

```text
comprehensions_generators/
│
├── __init__.py
├── utils.py
├── list_comprehensions.py
├── dictionary_comprehensions.py
├── set_comprehensions.py
├── nested_comprehensions.py
├── iterators.py
├── generators.py
├── demo.py
├── cli.py
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_list_comprehensions.md
│   ├── 03_dictionary_comprehensions.md
│   ├── 04_set_comprehensions.md
│   ├── 05_nested_comprehensions.md
│   ├── 06_iterators.md
│   ├── 07_generators.md
│   ├── 08_generator_expressions.md
│   ├── 09_interview_questions.md
│   └── 10_exercises.md
│
└── tests/
    ├── __init__.py
    ├── test_list_comprehensions.py
    ├── test_dictionary_comprehensions.py
    ├── test_set_comprehensions.py
    ├── test_nested_comprehensions.py
    ├── test_iterators.py
    └── test_generators.py
```

---

# Topics Covered

## List Comprehensions

Learn how to create lists using concise expressions.

Examples include:

* Squaring numbers
* Filtering even and odd numbers
* Transforming strings
* Flattening matrices
* Removing unwanted values

---

## Dictionary Comprehensions

Learn how to build dictionaries dynamically.

Examples include:

* Number-to-square mappings
* Word-length mappings
* Employee salary dictionaries
* Dictionary filtering
* Dictionary inversion

---

## Set Comprehensions

Learn how to create unique collections efficiently.

Examples include:

* Removing duplicates
* Unique lowercase words
* Unique first letters
* Unique remainders
* Character extraction

---

## Nested Comprehensions

Create complex data structures using nested comprehensions.

Examples include:

* Matrix transposition
* Matrix generation
* Cartesian products
* Coordinate grids
* Identity matrices
* Chessboard coordinates

---

## Iterator Protocol

Understand how Python's iteration system works internally.

Topics include:

* `iter()`
* `next()`
* `__iter__()`
* `__next__()`
* `StopIteration`
* Custom iterator classes

---

## Generators

Learn how generators produce values lazily.

Topics include:

* `yield`
* Countdown generators
* Fibonacci generators
* Infinite generators
* File generators
* Batch generators
* Generator pipelines

---

## Generator Expressions

Create memory-efficient generators using expression syntax.

Example:

```python
(number ** 2 for number in numbers)
```

---

# Running the Demo

Run every demonstration:

```bash
python -m comprehensions_generators.demo
```

---

# Using the CLI

List available topics:

```bash
python -m comprehensions_generators.cli --list
```

Run only list comprehensions:

```bash
python -m comprehensions_generators.cli --topic list
```

Run only dictionary comprehensions:

```bash
python -m comprehensions_generators.cli --topic dictionary
```

Run only set comprehensions:

```bash
python -m comprehensions_generators.cli --topic set
```

Run only nested comprehensions:

```bash
python -m comprehensions_generators.cli --topic nested
```

Run only iterator examples:

```bash
python -m comprehensions_generators.cli --topic iterators
```

Run only generator examples:

```bash
python -m comprehensions_generators.cli --topic generators
```

---

# Running the Tests

Run the entire test suite:

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
pytest --cov=comprehensions_generators --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=comprehensions_generators --cov-report=html
```

---

# Best Practices

* Prefer comprehensions over simple loops when transforming collections.
* Keep comprehensions readable; avoid excessive nesting.
* Use dictionary comprehensions for dynamic mappings.
* Use set comprehensions when uniqueness is required.
* Use generators when processing large datasets.
* Prefer generator expressions over list comprehensions when only sequential iteration is required.
* Implement custom iterators when building reusable iteration logic.
* Use lazy evaluation to reduce memory usage.

---

# Learning Path

Study the module in the following order:

1. Introduction
2. List Comprehensions
3. Dictionary Comprehensions
4. Set Comprehensions
5. Nested Comprehensions
6. Iterator Protocol
7. Generators
8. Generator Expressions
9. Interview Questions
10. Exercises
11. Demo
12. Unit Tests

---

# Skills You Will Gain

After completing this module, you will be able to:

* Write concise and expressive Python code
* Transform collections efficiently
* Create complex data structures using comprehensions
* Understand Python's iterator model
* Build custom iterators
* Design memory-efficient generators
* Stream large datasets without loading everything into memory
* Build reusable data-processing pipelines

---

# Prerequisites

Before starting this module, you should be comfortable with:

* Variables and Data Types
* Conditional Statements
* Loops
* Functions
* Collections
* Iteration Helpers

---

# Next Module

After completing **Comprehensions & Generators**, continue with more advanced Python topics such as:

* File Handling
* Exception Handling
* Object-Oriented Programming
* Decorators
* Context Managers
* Functional Programming


