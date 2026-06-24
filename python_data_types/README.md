# Python Data Types

## Overview

This repository is a hands-on learning module covering Python fundamentals with a focus on writing clean, modular, and testable code.

The project demonstrates:

* Introspection
* Dunder (Magic) Methods
* Truthiness
* Type Checking
* Type Casting
* Lists
* Tuples
* Sets
* Dictionaries
* JSON Querying
* Word Frequency Counter
* Type Annotations
* Pytest
* Argparse

The project follows a modular structure where each concept is implemented in its own package. Every package exposes a simple public API through its `__init__.py`, allowing `main.py` to communicate only with the package instead of individual implementation files.

---

# Project Structure

```text
python_data_types/
│
├── main.py
│
├── introspection/
├── dunder/
├── truthiness/
├── type_checking_casting/
├── lists/
├── tuples/
├── sets/
├── dictionaries/
├── utilities/
│
└── tests/
```

---

# Folder Description

## 1. introspection/

Demonstrates Python's built-in introspection capabilities.

Topics covered:

* `type()`
* `id()`
* `dir()`
* `inspect.getdoc()`
* Listing methods
* Listing public attributes

Files:

* `__init__.py` – Public API
* `inspector.py` – Introspection helper functions
* `models.py` – Sample classes used for demonstrations

---

## 2. dunder/

Demonstrates Python Magic (Dunder) Methods.

Topics covered:

* `__add__`
* `__eq__`
* `__str__`
* `__repr__`

Files:

* `__init__.py`
* `operators.py`

---

## 3. truthiness/

Demonstrates how Python evaluates objects as Truthy or Falsy.

Topics covered:

* Truthy values
* Falsy values
* Boolean evaluation
* Counting truthy and falsy values

Files:

* `__init__.py`
* `evaluator.py`

---

## 4. type_checking_casting/

Covers Python's type system.

Topics covered:

### Type Checking

* `type()`
* `isinstance()`

### Type Casting

* `int()`
* `float()`
* `str()`
* `bool()`
* Safe casting using exception handling

Files:

* `__init__.py`
* `checker.py`
* `casting.py`

---

## 5. lists/

Demonstrates Python List methods and operations.

Topics covered:

* append()
* extend()
* insert()
* remove()
* pop()
* clear()
* reverse()
* sort()
* copy()

Includes:

* Simple Queue implementation using lists

Files:

* `__init__.py`
* `list_methods.py`
* `simple_queue.py`

---

## 6. tuples/

Demonstrates Tuple operations.

Topics covered:

* count()
* index()

Files:

* `__init__.py`
* `tuple_methods.py`

---

## 7. sets/

Demonstrates Set operations.

Topics covered:

* add()
* remove()
* discard()
* pop()
* clear()
* union()
* intersection()
* difference()
* symmetric_difference()
* issubset()
* issuperset()
* isdisjoint()

Includes:

* Tag Merger exercise

Files:

* `__init__.py`
* `set_methods.py`
* `tag_merger.py`

---

## 8. dictionaries/

Demonstrates Dictionary operations.

Topics covered:

* get()
* setdefault()
* update()
* pop()
* popitem()
* keys()
* values()
* items()
* copy()
* clear()

Includes:

### JSON Query Engine

Access nested dictionaries using dot notation.

Example:

```python
query_json(data, "user.profile.name")
```

### Vocabulary Word Counter

Counts word frequency while ignoring punctuation and case.

Files:

* `__init__.py`
* `dictionary_methods.py`
* `json_query.py`
* `vocabulary.py`

---

## 9. utilities/

Contains reusable helper functions.

Currently includes:

* Documentation Helper (`__doc__`)
* Method documentation extractor

Files:

* `__init__.py`
* `doc_helper.py`

---

## 10. tests/

Contains unit tests written using **Pytest**.

Each module has a dedicated test file.

Examples:

* `test_introspection.py`
* `test_dunder.py`
* `test_truthiness.py`
* `test_type_checking_casting.py`
* `test_lists.py`
* `test_tuples.py`
* `test_sets.py`
* `test_dictionaries.py`

---

# Design Principles

This project follows a modular architecture.

Each package:

* Encapsulates related functionality.
* Exposes only its public interface through `__init__.py`.
* Hides implementation details from `main.py`.

This reduces coupling and improves maintainability.

---

# Main Runner

`main.py` serves as the entry point.

It demonstrates every module and supports command-line execution using **argparse**.

Examples:

Run everything:

```bash
python main.py
```

Run only introspection:

```bash
python main.py --module introspection
```

Run only sets:

```bash
python main.py --module sets
```

Run only dictionaries:

```bash
python main.py --module dicts
```

---

# Technologies Used

* Python 3
* argparse
* inspect
* typing (Type Annotations)
* pytest

---

# Learning Outcomes

After completing this project, you should be able to:

* Understand Python data types.
* Use introspection effectively.
* Work with dunder methods.
* Perform type checking and safe casting.
* Use Python collections efficiently.
* Query nested dictionaries.
* Write reusable and modular code.
* Add type annotations to improve code readability.
* Write unit tests using Pytest.
* Build simple command-line applications using argparse.
