# Iterators & Generators Overview

This module focuses on Python iterators and generators for lazy iteration and memory-efficient data handling.

## Implemented Topics

### 1. Iterator Protocol
Implemented in:

- `iterators_generators/iterator_protocol.py`

Covered:
- Custom iterator class
- `__iter__()` method
- `__next__()` method
- `StopIteration`

---

### 2. Generators using `yield`
Implemented in:

- `iterators_generators/generators.py`

Covered:
- Creating generator functions with `yield`
- Producing values lazily one at a time
- Generating sequences without storing all values in memory

---

### 3. Generator Expressions
Implemented in:

- `iterators_generators/generator_expressions.py`

Covered:
- Single-line lazy iteration using parentheses
- Squaring values lazily
- Filtering even values lazily

---

## Testing

Pytest files are available in the `tests/` folder for validating all iterator and generator modules.