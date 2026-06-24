# Python Datatypes

Enterprise-grade Python learning package showcasing modular design, introspection, JSON querying, collection utilities, composition, dunder patterns, and professional tooling.

## Architecture Diagram

```text
python_datatypes/
├── __init__.py
├── __main__.py
├── main.py
├── logging_config.py
├── json_query.py
├── introspection/
│   ├── __init__.py
│   ├── documentation_extractor.py
│   ├── introspection_engine.py
│   └── method_explorer.py
├── composition/
│   ├── __init__.py
│   ├── composition_utils.py
│   └── demo.py
├── dunder_methods/
│   ├── __init__.py
│   ├── dunder_utils.py
│   └── demo.py
├── dictionary_methods/
│   ├── __init__.py
│   ├── dictionary_utils.py
│   └── demo.py
├── list_methods/
│   ├── __init__.py
│   ├── list_utils.py
│   └── demo.py
├── set_methods/
│   ├── __init__.py
│   ├── set_utils.py
│   └── demo.py
├── tuple_methods/
│   ├── __init__.py
│   ├── tuple_utils.py
│   └── demo.py
└── tests/
    ├── test_dictionary.py
    ├── test_introspection.py
    ├── test_json_query.py
    ├── test_list.py
    ├── test_set.py
    └── test_tuple.py
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Package

Execute the package with CLI subcommands:

```bash
python -m python_datatypes introspect "[1, 2, 3]"
python -m python_datatypes query '{"a": {"b": [10, 20]}}' a.b[1]
python -m python_datatypes methods "{'name':'Alice'}"
python -m python_datatypes docs "python_datatypes.introspection.introspection_engine"
python -m python_datatypes demo composition
```

## Running Tests

```bash
pytest
```

## CLI Examples

```bash
python -m python_datatypes introspect "{'value': 42}"
python -m python_datatypes query '{"user": {"profile": {"id": 10}}}' user.profile.id
python -m python_datatypes methods "[1, 2, 3]"
python -m python_datatypes docs "python_datatypes.composition.Address"
```

## Learning Objectives

- Demonstrate clean module boundaries and explicit package exports.
- Implement advanced introspection and documentation extraction using `inspect`.
- Build a safe nested JSON query engine for mixed structures.
- Use `argparse` with subcommands and structured CLI output.
- Apply reusable collection utilities with type safety and pytest coverage.
- Model composition and dunder method patterns with professional examples.
