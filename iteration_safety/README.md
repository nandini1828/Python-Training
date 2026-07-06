# Iteration Safety

The **Iteration Safety** module teaches how to safely iterate over and modify Python collections without introducing bugs. It explains the dangers of changing lists, dictionaries, and sets during iteration and demonstrates enterprise-safe techniques such as snapshot iteration, defensive programming, copy-on-write, and immutable transformations.

This module builds on the concepts learned in **Loop Foundations**, **Iteration Helpers**, and **Comprehensions & Generators**.

---

# Learning Objectives

After completing this module, you will be able to:

* Understand why modifying collections during iteration is dangerous.
* Safely iterate over lists, dictionaries, and sets.
* Explain the difference between references and copies.
* Create shallow and deep copies.
* Apply safe mutation patterns.
* Implement defensive iteration techniques.
* Write robust and maintainable Python code.

---

# Module Structure

```text
iteration_safety/
│
├── __init__.py
├── utils.py
├── safe_list_iteration.py
├── safe_dictionary_iteration.py
├── safe_set_iteration.py
├── copy_vs_reference.py
├── mutation_patterns.py
├── defensive_iteration.py
├── demo.py
├── cli.py
├── README.md
│
├── notes/
│   ├── 01_introduction.md
│   ├── 02_safe_list_iteration.md
│   ├── 03_safe_dictionary_iteration.md
│   ├── 04_safe_set_iteration.md
│   ├── 05_copy_vs_reference.md
│   ├── 06_mutation_patterns.md
│   ├── 07_defensive_iteration.md
│   ├── 08_best_practices.md
│   ├── 09_interview_questions.md
│   └── 10_exercises.md
│
└── tests/
    ├── __init__.py
    ├── test_safe_list_iteration.py
    ├── test_safe_dictionary_iteration.py
    ├── test_safe_set_iteration.py
    ├── test_copy_vs_reference.py
    ├── test_mutation_patterns.py
    └── test_defensive_iteration.py
```

---

# Topics Covered

## Safe List Iteration

Learn how to safely process lists without modifying them during iteration.

Examples include:

* Removing negative values
* Filtering even numbers
* Removing duplicates
* Snapshot iteration
* Replacing values

---

## Safe Dictionary Iteration

Learn how to safely work with dictionaries.

Examples include:

* Removing keys
* Removing empty values
* Transforming keys
* Transforming values
* Snapshotting keys and items

---

## Safe Set Iteration

Learn safe techniques for processing sets.

Examples include:

* Filtering values
* Safe removal
* Set intersections
* Set differences
* Snapshot iteration

---

## Copy vs Reference

Understand Python's object model.

Topics include:

* Assignment
* References
* Shallow copy
* Deep copy
* Object identity
* Object equality

---

## Mutation Patterns

Learn safe ways to modify data.

Examples include:

* Filtering
* Replacing values
* Merging collections
* Dictionary updates
* Removing duplicates

---

## Defensive Iteration

Enterprise-safe processing techniques.

Topics include:

* Snapshot iteration
* Batch processing
* Validation
* Immutable filtering
* Safe processing

---

# Running the Demo

Run every demonstration:

```bash
python -m iteration_safety.demo
```

---

# Using the CLI

List available topics:

```bash
python -m iteration_safety.cli --list
```

Run only list examples:

```bash
python -m iteration_safety.cli --topic list
```

Run dictionary examples:

```bash
python -m iteration_safety.cli --topic dictionary
```

Run set examples:

```bash
python -m iteration_safety.cli --topic set
```

Run copy/reference examples:

```bash
python -m iteration_safety.cli --topic copy
```

Run mutation examples:

```bash
python -m iteration_safety.cli --topic mutation
```

Run defensive iteration examples:

```bash
python -m iteration_safety.cli --topic defensive
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
pytest --cov=iteration_safety --cov-report=term-missing
```

Generate an HTML coverage report:

```bash
pytest --cov=iteration_safety --cov-report=html
```

---

# Best Practices

* Never modify a collection while iterating over it directly.
* Iterate over a copy when changes are required.
* Prefer rebuilding collections over mutating them.
* Use shallow or deep copies appropriately.
* Validate data before processing.
* Keep transformations simple and predictable.
* Prefer immutable patterns when practical.

---

# Learning Path

Study the module in this order:

1. Introduction
2. Safe List Iteration
3. Safe Dictionary Iteration
4. Safe Set Iteration
5. Copy vs Reference
6. Mutation Patterns
7. Defensive Iteration
8. Best Practices
9. Interview Questions
10. Exercises
11. Demo
12. Unit Tests

---

# Skills You Will Gain

After completing this module, you will be able to:

* Identify unsafe iteration patterns.
* Prevent common collection-mutation bugs.
* Explain Python reference semantics.
* Write defensive Python code.
* Build reliable collection-processing logic.
* Apply enterprise coding practices.

---

# Prerequisites

Before starting this module, you should understand:

* Variables and Data Types
* Lists, Tuples, Dictionaries, and Sets
* Loops
* Functions
* Comprehensions
* Iterators
* Generators

---

# Next Module

After completing **Iteration Safety**, continue with:

* File Handling
* Exception Handling
* Object-Oriented Programming
* Decorators
* Context Managers
* Functional Programming


