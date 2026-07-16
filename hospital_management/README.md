# Hospital Management System - FastAPI

A beginner-friendly REST API for managing hospital operations including patients, doctors, and appointments.

This project is designed as a learning resource to understand:
- FastAPI basics
- Pydantic models and validation
- RESTful API design
- Service-oriented architecture
- Pytest testing
- Python fundamentals (classes, type hints, list comprehensions, etc.)

## Project Overview

The Hospital Management System is a simple API that demonstrates how to build a REST service with FastAPI. It manages three main resources:
- **Patients**: Store and manage patient information
- **Doctors**: Store and manage doctor information  
- **Appointments**: Book and manage appointments between patients and doctors

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation and parsing using Python type hints
- **Uvicorn**: ASGI server for running the application
- **Pytest**: Testing framework for writing and running tests

## Folder Structure

```
hospital_management/
├── app/
│   ├── main.py              # Main FastAPI application
│   ├── models/              # Pydantic models for data validation
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── appointment.py
│   ├── routers/             # API route handlers
│   │   ├── patient_router.py
│   │   ├── doctor_router.py
│   │   └── appointment_router.py
│   ├── services/            # Business logic and data management
│   │   ├── patient_service.py
│   │   ├── doctor_service.py
│   │   └── appointment_service.py
│   └── utils/               # Helper functions
│       └── helper.py
├── tests/                   # Pytest test files
│   ├── test_patient.py
│   ├── test_doctor.py
│   └── test_appointment.py
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── .gitignore               # Git ignore file
```

## Key Features

✅ **REST API Endpoints** for CRUD operations on patients, doctors, and appointments

✅ **Pydantic Validation** - Automatic input validation and documentation

✅ **In-Memory Data Storage** - No database setup required (perfect for learning)

✅ **Type Hints** - Full type annotations for better IDE support

✅ **Error Handling** - Proper HTTP status codes and error messages

✅ **Interactive Documentation** - Auto-generated API docs with Swagger UI

✅ **Comprehensive Tests** - Pytest test suite for all services

✅ **Beginner-Friendly Code** - Well-commented, clear structure

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

### 3. View API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 4. Run Tests

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

## API Endpoints

### Patients

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/patients` | Get all patients |
| GET | `/patients/{id}` | Get a specific patient |
| POST | `/patients` | Create a new patient |
| PUT | `/patients/{id}` | Update a patient |
| DELETE | `/patients/{id}` | Delete a patient |

### Doctors

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/doctors` | Get all doctors |
| GET | `/doctors/{id}` | Get a specific doctor |
| POST | `/doctors` | Create a new doctor |
| PUT | `/doctors/{id}` | Update a doctor |
| DELETE | `/doctors/{id}` | Delete a doctor |

### Appointments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/appointments` | Get all appointments |
| GET | `/appointments/{id}` | Get a specific appointment |
| GET | `/appointments/patient/{patient_id}` | Get appointments for a patient |
| GET | `/appointments/doctor/{doctor_id}` | Get appointments for a doctor |
| POST | `/appointments` | Book a new appointment |
| PUT | `/appointments/{id}` | Update appointment status or date |
| DELETE | `/appointments/{id}` | Cancel an appointment |

## Sample Requests

### Create a Patient

**Request:**
```bash
curl -X POST "http://localhost:8000/patients" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 4,
    "name": "Sarah Wilson",
    "age": 35,
    "gender": "Female",
    "phone": "9876543210"
  }'
```

**Response:**
```json
{
  "id": 4,
  "name": "Sarah Wilson",
  "age": 35,
  "gender": "Female",
  "phone": "9876543210"
}
```

### Get All Patients

**Request:**
```bash
curl "http://localhost:8000/patients"
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "phone": "9876543210"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 28,
    "gender": "Female",
    "phone": "9123456789"
  }
]
```

### Create a Doctor

**Request:**
```bash
curl -X POST "http://localhost:8000/doctors" \
  -H "Content-Type: application/json" \
  -d '{
    "id": 4,
    "name": "Dr. Brown",
    "specialization": "General Practice",
    "experience": 15
  }'
```

### Book an Appointment

**Request:**
```bash
curl -X POST "http://localhost:8000/appointments" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "appointment_date": "2024-12-25T10:00:00"
  }'
```

**Response:**
```json
{
  "id": 3,
  "patient_id": 1,
  "doctor_id": 1,
  "appointment_date": "2024-12-25T10:00:00",
  "status": "Scheduled"
}
```

### Get All Appointments for a Patient

**Request:**
```bash
curl "http://localhost:8000/appointments/patient/1"
```

### Update Patient Information

**Request:**
```bash
curl -X PUT "http://localhost:8000/patients/1" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 31,
    "phone": "9999999999"
  }'
```

### Cancel an Appointment

**Request:**
```bash
curl -X DELETE "http://localhost:8000/appointments/1"
```

## Python Concepts Demonstrated

This project naturally demonstrates several Python fundamentals:

- **Classes**: Service classes and Pydantic models
- **Type Hints**: Function parameters and return types
- **Lists**: Data storage and iteration
- **Dictionaries**: Data manipulation with dict operations
- **Control Flow**: if-else conditions, for loops, continue, break
- **List Comprehension**: Filtering and transforming data
- **Functions**: Organizing code into reusable functions
- **Exception Handling**: HTTPException for error responses
- **isinstance()**: Type checking in helper functions
- **dir()**: Educational example in helper.py
- **Modular Programming**: Separation of concerns (models, services, routers)

## Code Quality

- **PEP8 Compliant**: Follows Python style guidelines
- **Type Safe**: Full type annotations throughout
- **Well-Documented**: Docstrings and inline comments
- **Clean Code**: Small functions, meaningful names, no deep nesting
- **Error Handling**: Proper validation and HTTP error responses

## Learning Path

1. **Start here**: Review `app/main.py` to understand the app structure
2. **Explore models**: Check `app/models/` to see Pydantic validation
3. **Study services**: Look at `app/services/` to understand business logic
4. **Learn routers**: Review `app/routers/` to see API design
5. **Read tests**: Check `tests/` to understand testing patterns
6. **Try it out**: Make API requests to see it in action

## Common Issues

**Issue**: Port 8000 already in use
```bash
# Use a different port
python -m uvicorn app.main:app --reload --port 8001
```

**Issue**: Module not found errors
```bash
# Make sure you're in the project root directory
# and have installed requirements
pip install -r requirements.txt
```

**Issue**: Tests fail
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt
# Run tests from project root
pytest
```

## Next Steps

To extend this project:
- Add email notifications
- Implement appointment reminders
- Add doctor availability slots
- Create admin dashboard
- Add user authentication
- Connect to a real database (PostgreSQL, MongoDB)
- Deploy to cloud (AWS, Azure, GCP)

## Author Notes

This project is designed for beginners to understand:
- How modern APIs are structured
- Why separation of concerns matters
- How to write testable code
- Python best practices

Feel free to modify and extend it for learning purposes!

---

**Happy Learning! 🚀**
