# Student Management System

A complete FastAPI-based student management application with CRUD operations for students, courses, and attendance records.

## Features
- Student management with validation and pagination
- Course management with enrollment support
- Attendance tracking with daily records and reporting
- JSON-based persistence using local files
- Swagger documentation via FastAPI

## Quick Start
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the API:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open the docs at:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc
