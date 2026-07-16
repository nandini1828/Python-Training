# Library Management System

A beginner-friendly Library Management System built with Python and FastAPI.

## Project Structure

- `main.py` - FastAPI application entry point.
- `apis/` - Routers for books, members, and transactions.
- `models/` - Domain models for books, members, transactions, and library.
- `services/` - Business logic and in-memory operations.
- `utils/` - Constants, ID generators, validation helpers, and introspection utilities.
- `data/` - In-memory storage collections.

## Run the project

1. Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

2. Run the app:

```bash
cd library_management
uvicorn main:app --reload
```

3. API documentation:

- Open `http://127.0.0.1:8000/docs`
- Open `http://127.0.0.1:8000/redoc`

## Features

- Add, view, update, and delete books
- Search books by title, author, and category
- Register, view, update, and delete members
- Issue, return, renew, reserve, and cancel reservation
- In-memory storage only; no database or external file storage
