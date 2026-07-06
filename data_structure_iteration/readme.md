# Python Data Structure Iteration

A beginner-friendly Python project that demonstrates safe iteration and data structure handling using a real-world **order and inventory system**.

---

## About the Project

This module explains how to iterate safely over Python's core data structures and avoid common bugs, especially when modifying lists while looping.

Topics covered:

- Lists: indexing, slicing, and looping
- List Modification Trap: why removing elements while iterating is unsafe
- Dictionaries: `.keys()`, `.values()`, `.items()`
- Dictionary Key Protection: `.get(key, default)` and `collections.defaultdict`
- Sets: fast membership testing and looping

---

## Project Structure

```text
data_structure_iteration/
│
├── main.py
├── readme.md
├── __init__.py
├── dictionary_iteration.py
├── dictionary_key_protection.py
├── list_iteration.py
├── list_modification_trap.py
├── set_iteration.py
└── tests/
    ├── __init__.py
    ├── test_dictionary_iteration.py
    ├── test_dictionary_key_protection.py
    ├── test_list_iteration.py
    ├── test_list_modification_trap.py
    └── test_set_iteration.py
```

---

## Topics Covered

### Lists
- Access elements by index
- Use slicing to get sublists
- Loop over list elements safely

### List Modification Trap
- Removing elements from a list while iterating can skip elements
- Use list comprehensions or iterate over a copy instead

### Dictionaries
- Loop over keys with `.keys()`
- Loop over values with `.values()`
- Loop over key-value pairs with `.items()`

### Dictionary Key Protection
- Use `.get(key, default)` to avoid `KeyError`
- Use `collections.defaultdict` for automatic default values

### Sets
- Fast membership testing (`O(1)` lookup)
- Loop over set elements

---

## Running the Project

### Interactive Menu
```bash
cd /Users/wallstreet/Python-Training/data_structure_iteration
python3 main.py
```

### Direct Module Execution
```bash
cd /Users/wallstreet/Python-Training/data_structure_iteration
python3 main.py
```

---

## Example Use Cases

- Validate and remove processed orders safely
- Examine inventory keys, values, and item pairs
- Protect product lookups from missing keys
- Quickly test whether a product is available in stock

---

## Notes

- The module is standalone and not part of `loops_and_iteration`.
- It uses real-world inventory examples for clarity.
- The main menu provides focused access to each concept.
