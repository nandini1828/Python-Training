# python_datatypes_mastery — Project Overview

This document summarizes the `python_datatypes_mastery` educational project.

## Purpose

A trainer-level Python project demonstrating mastery of:

- Python data types (primitives, lists, dicts, tuples, sets)
- Introspection (`dir`, `type`, `isinstance`, `id`, `inspect`)
- Type checking and safe casting
- Dunder (special) methods and operator overloading
- Collections APIs and common idioms
- Classes, objects, composition, `__dict__` and `__new__`
- Recursive object deconstruction to JSON-serializable structures
- Small exercises (queue, tag merging, JSON querying, word counting)
- Automated testing via `pytest`
- CLI usage via `argparse`
- Type hints (PEP 484) and clean code practices

## Folder structure

```
python_datatypes_mastery/
├── main.py                # CLI entrypoint (argparse)
├── primitives/            # introspection, casting, dunder examples
├── collections_pkg/       # list/dict/set/tuple utilities (renamed to avoid stdlib shadowing)
├── classes/               # Student, Computer, deconstructor
├── inspectors/            # method and documentation inspectors
├── exercises/             # queue, tag_merger, json query, word_counter
├── tests/                 # pytest tests
└── README.md
```

## Key Modules and Highlights

- `primitives/introspection.py`:
  - `inspect_object(obj)` returns `{"type": ..., "id": ..., "attributes": ...}`
  - Demonstrates `type()` vs `isinstance()` using example classes.

- `primitives/casting.py`:
  - `safe_cast(value, target_type, default=None)` performs guarded conversions.
  - Supports `int`, `float`, `str`, `bool`, `list`, `tuple`, `set` with fallbacks.

- `primitives/dunder_examples.py`:
  - `Employee` class implements `__add__`, `__str__`, `__repr__`.
  - `demo_dunders()` demonstrates built-in operator mappings.

- `collections_pkg/*`:
  - `list_utils`, `dict_utils`, `set_utils`, `tuple_utils` show common methods.
  - Each function returns results for demonstration and is type-annotated.

- `classes/student.py`:
  - `Student` demonstrates `__dict__`, `__new__` and an `average_grade()` method.

- `classes/computer.py` and `classes/object_deconstructor.py`:
  - Composition example with `CPU` and `Computer`.
  - `deconstruct_object(obj)` recursively converts objects into primitives suitable for JSON.

- `inspectors/method_inspector.py` and `documentation_inspector.py`:
  - `get_methods_and_docs(obj)` gathers callables and their docstrings via `inspect.getdoc()`.
  - Documentation fetching utilities demonstrate `__doc__` and `inspect.getdoc()`.

- `exercises/`:
  - `SimpleQueue` with `enqueue()`, `dequeue()`, `size()`.
  - `merge_tags(tags_a, tags_b)` — case-normalized set merging.
  - `query_json(data, path_str, default=None)` — dot-path traversal of nested dicts.
  - `word_count(text)` — punctuation-insensitive frequency counting.

- `tests/`:
  - Pytest-based tests covering casting, queue, json query, word counting, and deconstructor.

## Command-line Interface (argparse)

`main.py` now exposes a CLI using `argparse`:

```bash
# Run all demos (default)
python3 -m python_datatypes_mastery.main

# Run selected sections
python3 -m python_datatypes_mastery.main --introspection --casting

# Run pytest for the project
python3 -m python_datatypes_mastery.main --run-tests
```

The CLI provides modular demo functions, and returns an exit code of `0` on success.

## Type Hints and Static Quality

- All modules include type hints for public functions and classes following PEP 484.
- Docstrings use Google style and appear for modules, classes, and functions.
- The code follows PEP8 and clean code practices: meaningful names, short functions, and modular design.

## Running Tests

From the project root run:

```bash
pytest
```

Or via the CLI:

```bash
python3 -m python_datatypes_mastery.main --run-tests
```

## VS Code Integration

A small local extension is included that streams the stdout/stderr of the active Python file into a dedicated Output Channel named "Python Datatypes Demo". To use it:

1. Open this workspace in VS Code.
2. Press `F5` to open an Extension Development Host.
3. Open a Python file and run the command `Python Datatypes: Run Active Python File to Output Channel` (or use the context menu / `Ctrl+Alt+R`).

## Educational Notes for Trainers

- Use `deconstruct_object` to demonstrate serialization pitfalls with objects that contain iterators, slots, or non-serializable members.
- Use `inspect` utilities to explore runtime behavior and to show differences between `type()` and `isinstance()`.
- Extend exercises with edge-case tests (empty inputs, deeply nested structures, unicode text) as lab assignments.

## Contact

If you want me to package the VS Code extension as a `.vsix`, add CI (GitHub Actions) to run tests on push, or expand the exercises, tell me which next step you prefer.
