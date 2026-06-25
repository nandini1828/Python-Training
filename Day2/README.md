# Python Learning Framework

This project is a beginner-friendly Python learning repository that is organized into small modules. Each folder focuses on one important Python concept so a viewer can understand what was implemented and why it matters.

## What this project covers
This repository demonstrates:
- how Python modules and packages are organized
- how common data structures such as lists, tuples, sets, and dictionaries work
- how to inspect objects and understand their behavior
- how classes and methods can be designed in a clear and reusable way
- how to use simple command-line arguments and JSON-like data access

## Project structure
The main project is organized as follows:

```text
main.py
├── introspection/
├── list_methods/
├── set_methods/
├── tuple_methods/
├── dictionary_methods/
├── dunder_methods/
├── composition/
├── json_query_engine/
└── argparse_module/
```

## What each folder is for
- introspection: shows how Python can inspect objects and their methods
- list_methods: explains list operations such as adding, removing, sorting, and chunking
- tuple_methods: demonstrates immutable collections and tuple-based patterns
- set_methods: shows set operations such as union, intersection, and difference
- dictionary_methods: explains dictionary storage, lookup, and updates
- dunder_methods: shows special methods like __str__ and __repr__
- composition: demonstrates how classes can be combined to build larger systems
- json_query_engine: shows how to read values from nested data structures
- argparse_module: shows how to parse simple command-line arguments

## How to run the project
```bash
python main.py list
python main.py tuple
python main.py set
python main.py dictionary
python main.py introspection
python main.py dunder
python main.py composition
python main.py json
python main.py argparse
```

## How to install and test
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Learning goals
By reading this repository, a viewer should be able to understand:
- how Python code can be split into meaningful modules
- how common data structures are used in practice
- how simple reusable utilities are written
- how beginner-friendly examples can be organized into a clean project structure
