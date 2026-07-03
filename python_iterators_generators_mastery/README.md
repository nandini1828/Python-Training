# Python Iterators & Generators Mastery

This project demonstrates Python iterators and generators in a clean, modular structure.

## Topics Covered

### Iterators & Generators
- Iterator Protocol: `__iter__()` and `__next__()`
- Generators using `yield`
- Generator Expressions

### Testing
Pytest-based unit tests are included for all major iterator/generator modules.

## Project Structure

```text
python_iterators_generators_mastery/
│
├── main.py
├── pytest.ini
├── README.md
│
├── iterators_generators/
│   ├── __init__.py
│   ├── iterator_protocol.py
│   ├── generators.py
│   └── generator_expressions.py
│
├── tests/
│   ├── test_iterator_protocol.py
│   ├── test_generators.py
│   └── test_generator_expressions.py
│
└── docs/
    └── overview.md