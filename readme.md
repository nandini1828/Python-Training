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
# Django Learning

A complete **beginner-to-enterprise Django learning repository** designed to help Python developers master Django and Django REST Framework (DRF) through structured theory, hands-on projects, detailed notes, and real-world examples.

---

# 🎯 Objective

This repository is not just a collection of code.

It is a **complete learning handbook** that explains:

* Django fundamentals
* Internal working of Django
* Enterprise development practices
* REST API development using Django REST Framework (DRF)
* Real-world project architecture
* Best practices followed in production environments

By the end of this bootcamp, you'll be able to build production-ready Django applications and REST APIs.

---

# 👨‍🎓 Prerequisites

Before starting this repository, you should know:

* Basic Python
* Variables
* Data Types
* Functions
* Classes & Objects
* File Handling
* Modules & Packages

No prior Django knowledge is required.

---

# 📚 Learning Roadmap

## Phase 1 – Django Fundamentals

* Introduction to Django
* Installing Django
* Creating a Django Project
* Understanding Project Structure
* Django Apps
* Views
* URL Routing
* Request–Response Cycle
* Templates
* Static Files

---

## Phase 2 – Database & ORM

* Databases
* SQLite
* Models
* ORM (Object Relational Mapper)
* Model Fields
* Migrations
* Django Admin
* CRUD Operations

---

## Phase 3 – Django REST Framework (DRF)

* Introduction to APIs
* REST Architecture
* JSON
* Serializers
* Function-Based APIs
* Class-Based APIs
* Generic Views
* ViewSets
* ModelViewSet
* Routers

---

## Phase 4 – Authentication & Security

* Session Authentication
* Token Authentication
* JWT Authentication
* Permissions
* Authentication Classes
* Custom Permissions

---

## Phase 5 – Advanced DRF

* Pagination
* Filtering
* Searching
* Ordering
* File Uploads
* Image Uploads
* Nested Serializers
* Relationships
* Custom Validation

---

## Phase 6 – Enterprise Django

* Project Structure
* Environment Variables
* Logging
* Testing
* Deployment
* PostgreSQL
* Docker Basics
* Performance Optimization
* Caching
* Production Best Practices

---

# 📁 Repository Structure

```text
django_learning/

│
├── Notes/
│   ├── 01_Introduction.md
│   ├── 02_Installation.md
│   ├── ...
│   └── 19_SQLite.md
│
├── commands/
│   ├── django_project_commands.md
│   ├── django_app_commands.md
│   ├── model_commands.md
│   └── ...
│
├── config/
│
├── students/
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```

---

# 📖 Notes

Every chapter contains:

* Learning Objectives
* Theory
* Internal Working
* Architecture Diagrams
* Code Examples
* Enterprise Best Practices
* Common Mistakes
* Interview Questions
* Exercises

---

# 💻 Commands Folder

The `commands/` folder contains reusable command references for:

* Django Project Commands
* Django App Commands
* Model Commands
* Migration Commands
* Django Admin Commands
* DRF Commands
* Authentication Commands
* Deployment Commands

---

# 🛠 Technologies Covered

* Python
* Django
* Django REST Framework
* SQLite
* PostgreSQL
* Git
* GitHub
* VS Code
* JSON
* REST APIs


---
# 🏗 Learning Flow

```text
Python

↓

Django Basics

↓

Projects

↓

Apps

↓

Views

↓

URL Routing

↓

Models

↓

ORM

↓

Migrations

↓

Admin

↓

CRUD

↓

REST APIs

↓

Serializers

↓

ViewSets

↓

Authentication

↓

Permissions

↓

Deployment
```






