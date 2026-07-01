Python training:
# Python Datatypes — Enterprise Learning Repository

Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Running examples

```bash
# Introspection examples
python main.py introspect --object list
python main.py introspect --object dict
python main.py introspect --object tuple
python main.py introspect --object bank        # sample custom object
python main.py introspect --object computer    # composition example

# JSON query examples (uses samples/sample.json)
python main.py json-query --file samples/sample.json --path user.name
python main.py json-query --file samples/sample.json --path user.address.city
python main.py json-query --file samples/sample.json --path employees.0.name

# Utility demos (run the demo modules directly)
python -m list_methods.demo
python -m set_methods.demo
python -m tuple_methods.demo
python -m dictionary_methods.demo
python -m dunder_methods.demo
python -m composition.demo
```

Running tests

```bash
pytest -v
```

Learning objectives
- Understand Python introspection and dynamic analysis
- Build reusable utilities with type hints and logging
- Explore dunder methods and composition patterns
- Use argparse, pytest and logging for professional code
# Python Topics

This project demonstrates important Python concepts in a structured manner.

---

# Folder Structure

```text
python_datatypes/
│
├── main.py
│
├── list_methods/
│   ├── __init__.py
│   ├── list_utils.py
│   └── demo.py
│
├── tuple_methods/
│   ├── __init__.py
│   ├── tuple_utils.py
│   └── demo.py
│
├── set_methods/
│   ├── __init__.py
│   ├── set_utils.py
│   └── demo.py
│
├── dictionary_methods/
│   ├── __init__.py
│   ├── dictionary_utils.py
│   └── demo.py
│
├── introspection/
│   ├── __init__.py
│   ├── introspection_utils.py
│   └── demo.py
│
├── composition/
│   ├── __init__.py
│   ├── composition_example.py
│   └── demo.py
│
└── dunder_methods/
    ├── __init__.py
    ├── dunder_examples.py
    └── demo.py
```

---

# Topics Covered

## 1. Introspection

Introspection is the ability of Python to examine objects at runtime.

### Functions Used

- type()
- id()
- dir()
- __class__

---

## 2. Composition

Composition allows one class to contain another class as an attribute.

Example:

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## 3. Dunder Methods

Dunder means Double Underscore methods.

Examples:

- __init__()
- __str__()
- __repr__()
- __len__()

---

# Running Examples

Navigate into a topic folder and execute:

```bash
python demo.py
```

Example:

```bash
cd introspection
python demo.py
```

---

# Naming Conventions

## Files

```python
student_manager.py
introspection_utils.py
```

## Functions

```python
get_student()
calculate_salary()
```

## Variables

```python
student_name
employee_id
```

## Classes

```python
Student
Employee
Car
```

----------------------------------------------------------------------------------------------------------------

