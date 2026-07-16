# Hospital Management System

## Project Description

This is a beginner-friendly Hospital Management System developed using **FastAPI** and **Python**.

The project does not use any database. Instead, all data is stored in Python data structures such as:

- Dictionary
- List
- Set
- Tuple

## Features

- Add Patient
- View Patients
- Delete Patient
- Search Patient

- Add Doctor
- View Doctors
- Delete Doctor

- Book Appointment
- View Appointments
- Delete Appointment

## Python Concepts Used

- Data Types
- Classes & Objects
- Dunder Methods
- Naming Conventions
- Modular Programming
- Type Annotations
- Conditional Statements
- Loops
- enumerate()
- sorted()
- reversed()
- List Comprehension
- Generator
- Counter
- Introspection
- FastAPI
- Pytest

## Run the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

Run Tests

```bash
pytest
```

Generate Coverage Report

```bash
pytest --cov=app
```