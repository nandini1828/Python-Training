# Data Structure Iteration

> "Iteration becomes powerful when you understand the shape of the data you are walking through."

---

# Module Overview

This module focuses on iterating over Python's most common built-in data
structures: lists, dictionaries, and sets.

Looping over a collection is simple at first glance, but real programs need more
than basic repetition. They need predictable ordering, safe mutation, defensive
dictionary access, clear transformations, and tests that prove helper functions
do not change input data unexpectedly.

The examples in this folder are intentionally small and reusable. Each topic has
a `utils.py` file for importable functions, a `demo.py` file for console
examples, a README for quick orientation, and a matching test file.

---

# Learning Objectives

After completing this module, you will be able to:

- Iterate over lists without losing index or value context.
- Filter, transform, summarize, and flatten list data.
- Modify lists safely by returning copies instead of mutating callers' data.
- Read dictionary keys, values, and key/value pairs clearly.
- Merge, invert, and search dictionaries.
- Access dictionary keys defensively with `get`, `setdefault`, and safe removal.
- Use set operations such as union, intersection, difference, and subset checks.
- Write small utility functions that are easy to test.

---

# Topics Covered

## 1. List Iteration

Lists preserve insertion order, so iteration is predictable.

```python
names = ["Asha", "Ravi", "Mira"]

for index, name in enumerate(names):
    print(index, name)
```

Folder: `list_iteration`

## 2. List Modification

Changing a list while iterating over it can skip values or produce confusing
results. This module favors copy-based helpers.

```python
def append_item(values, item):
    result = values.copy()
    result.append(item)
    return result
```

Folder: `list_modification`

## 3. Dictionary Iteration

Dictionaries preserve insertion order in modern Python and provide dedicated
views for keys, values, and items.

```python
scores = {"math": 90, "science": 84}

for subject, score in scores.items():
    print(subject, score)
```

Folder: `dictionary_iteration`

## 4. Dictionary Key Protection

Direct indexing raises `KeyError` when a key is missing. Defensive helpers make
programs easier to reason about.

```python
city = profile.get("city", "Unknown")
```

Folder: `dictionary_key_protection`

## 5. Set Iteration

Sets are useful for uniqueness and membership operations. Their iteration order
should not be treated as part of program logic.

```python
common = active_users & paid_users
```

Folder: `set_iteration`

---

# How to Run

Run all demonstrations:

```bash
python3 repository_scaffold/04_data_structure_iteration/main.py
```

Run the tests when `pytest` is installed:

```bash
python3 -m pytest repository_scaffold/04_data_structure_iteration/tests
```

---

# Project Structure

```text
04_data_structure_iteration/
├── Notes/
├── dictionary_iteration/
├── dictionary_key_protection/
├── list_iteration/
├── list_modification/
├── set_iteration/
├── tests/
├── json_query.py
├── logging_config.py
└── main.py
```
