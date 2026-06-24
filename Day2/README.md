# Python Learning Framework

A professional, enterprise-style Python learning repository that demonstrates modular design, introspection, reusable utilities, package exports, logging, CLI entry points, and testing.

## Architecture Diagram
```text
main.py
├── introspection/
├── list_methods/
├── set_methods/
├── tuple_methods/
├── dictionary_methods/
├── dunder_methods/
└── composition/
```

## Folder Structure
```text
.
├── main.py
├── composition/
├── dictionary_methods/
├── dunder_methods/
├── introspection/
├── list_methods/
├── set_methods/
├── tuple_methods/
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Examples
```bash
python main.py introspection
python main.py dictionary
python main.py list
python main.py set
python main.py tuple
python main.py dunder
python main.py composition
```

## Running Tests
```bash
pytest -q
```

## CLI Examples
```bash
python main.py introspection
python main.py composition
```

## Learning Objectives
- Understand Python packaging and modular architecture
- Practice introspection and documentation extraction
- Explore common collection utility patterns
- Learn how custom classes use dunder methods
- See composition as a design principle
