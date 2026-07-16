# Employee Management System

A beginner-friendly Python project that demonstrates object-oriented programming, collections, JSON handling, FastAPI, argparse, and pytest.

## Project Overview

This project contains a small employee management system with these parts:

- Employee and department data models
- Repository and service layers
- FastAPI endpoints for REST usage
- Basic business rules for salary, age, email, promotion, and leave
- Utility modules for lists, dictionaries, sets, JSON, iterators, generators, and inspection
- A simple CLI built with `argparse`
- Pytest-based unit tests

## Folder Structure

- `app/` contains the main application code.
- `tests/` contains the test suite.
- `data/` stores JSON and CSV files used as simple data storage.

## Features

- Add, update, delete, list, search, and filter employees
- Manage departments
- Calculate salary bonuses
- Validate age, salary, email, and leave rules
- Produce simple reports and analytics
- Expose endpoints through FastAPI
- Demonstrate Python fundamentals with clean and readable code

## Installation

```bash
cd employee_management_system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the FastAPI Application

```bash
uvicorn app.main:app --reload
```

## Running the CLI

```bash
python -m app.cli.argparse_demo employees
python -m app.cli.argparse_demo departments
python -m app.cli.argparse_demo report
python -m app.cli.argparse_demo analytics
```

## Running pytest

```bash
pytest
```

## Learning Outcomes

This project helps a trainee practice:

- Classes and objects
- Composition and encapsulation
- JSON and CSV usage
- Type hints and simple validation
- FastAPI route design
- CLI development with argparse
- Unit testing with pytest
