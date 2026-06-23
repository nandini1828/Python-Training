# Python-Training
=======
# Python Data Types: The Exhaustive Mastery Guide

This repository is a structured learning project for Python data types, introspection, collections, serialization, and object internals.

## Project Structure

- `main.py` - Entry point and module import example.
- `primitives/` - Primitive type helpers, introspection utilities, and dunder examples.
- `collection_utils/` - Examples of list, tuple, set, and dict operations.
- `classes/` - Class definitions and object deconstruction.
- `inspectors/` - Reflection utilities for methods and docstrings.
- `exercises/` - Practical exercise modules.
- `tests/` - Basic unit tests for core functionality.

## How to Use

1. Run the code directly:
   ```bash
   python main.py
   ```

2. Run tests with pytest:
   ```bash
   python -m pytest
   ```

## Key Functions

- `list_public_attributes(obj)` - returns public names from `dir(obj)`.
- `safe_cast(value, target_type, default=None)` - safe conversion with fallback.
- `count_truthy_falsy(items)` - counts truthy and falsy values.
- `SimpleQueue` - a queue implemented with list methods.
- `merge_tags(tags_a, tags_b)` - normalize tags, sort, and return unique/shared/difference lists.
- `query_json(data_dict, path_str, default=None)` - nested dict query using dot notation.
- `word_count(text)` - lowercase and punctuation-safe word frequency counter.
- `deconstruct_object(obj)` - recursively convert custom instances into nested dictionaries.
>>>>>>> 6dd5e5f (Pushing structured code)
