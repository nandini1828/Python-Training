# Student Course Management API

This project is a simple Django REST Framework (DRF) application for managing students, courses, and enrollments.

It demonstrates CRUD operations using:

- Django
- Django REST Framework
- SQLite
- ModelViewSet
- ModelSerializer
- DefaultRouter

---

## What this project does

This application allows you to:

- create, read, update, and delete students
- create, read, update, and delete courses
- create, read, update, and delete enrollments

The data is stored in a SQLite database, and the project exposes REST APIs through DRF.

---

## Project structure

```text
Django/
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── student_course_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── manage.py
```

---

## Main files

### 1. api/models.py
This file contains the database models:

- Student
  - name
  - email
  - age

- Course
  - title
  - duration
  - fee

- Enrollment
  - student
  - course
  - enrollment_date

These models define the data structure used by the application.

### 2. api/serializers.py
This file contains serializers for each model.

Serializers convert model data into JSON format and help validate incoming API data.

### 3. api/views.py
This file contains ViewSets for each resource.

Each viewset inherits from ModelViewSet, which provides built-in CRUD operations automatically.

### 4. api/urls.py
This file uses DefaultRouter to create API routes for:

- /api/students/
- /api/courses/
- /api/enrollments/

### 5. student_course_management/urls.py
This is the main URL configuration file for the project.

It includes the API routes under the /api/ prefix.

---

## API endpoints

### Students

- GET /api/students/
- POST /api/students/
- GET /api/students/<id>/
- PUT /api/students/<id>/
- PATCH /api/students/<id>/
- DELETE /api/students/<id>/

### Courses

- GET /api/courses/
- POST /api/courses/
- GET /api/courses/<id>/
- PUT /api/courses/<id>/
- PATCH /api/courses/<id>/
- DELETE /api/courses/<id>/

### Enrollments

- GET /api/enrollments/
- POST /api/enrollments/
- GET /api/enrollments/<id>/
- PUT /api/enrollments/<id>/
- PATCH /api/enrollments/<id>/
- DELETE /api/enrollments/<id>/

---

## Sample JSON examples

### Student

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 21
}
```

### Course

```json
{
  "title": "Python Programming",
  "duration": "3 Months",
  "fee": 4999.00
}
```

### Enrollment

```json
{
  "student": 1,
  "course": 1,
  "enrollment_date": "2026-06-26"
}
```

---

## Installation

From the project root, run:

```bash
cd /Users/msig4/Desktop/Vishnu_py/Django
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework
```

---

## Run the project

Apply migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/api/
- http://127.0.0.1:8000/admin/

---

## Create superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

---

## Summary

This project is a complete beginner-friendly example of a Django REST Framework API that manages students, courses, and enrollments with CRUD support.
