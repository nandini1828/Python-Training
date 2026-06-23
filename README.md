# Python Topics

This project demonstrates important Python concepts in a structured manner.

---

# Folder Structure

```text
python_topics/
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
├── dunder_methods/
│   ├── __init__.py
│   ├── dunder_examples.py
│   └── demo.py
│
└── README.md
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

---

# Author

Nandini