# Student Management System API

A simple RESTful API built using **Django** and **Django REST Framework
(DRF)** demonstrating CRUD operations using **ModelViewSet**.

## Features

-   Student, Course, Enrollment models
-   Django ORM
-   Django Admin
-   DRF ModelSerializer
-   DRF ModelViewSet
-   DefaultRouter
-   CRUD APIs
-   SQLite

## Project Structure

``` text
student_management_api/
├── manage.py
├── student_management_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── school/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── migrations/
```

## Models

### Student

-   id
-   name
-   email (unique)
-   age

### Course

-   id
-   course_name
-   course_code (unique)
-   duration

### Enrollment

-   id
-   student (ForeignKey)
-   course (ForeignKey)
-   enrolled_on

## DRF Components

### Serializers

-   StudentSerializer
-   CourseSerializer
-   EnrollmentSerializer

### ViewSets

-   StudentViewSet
-   CourseViewSet
-   EnrollmentViewSet

Each ViewSet supports: - GET - POST - PUT - PATCH - DELETE

## API Endpoints

  Method   Endpoint
  -------- -----------------
  GET      /students/
  POST     /students/
  GET      /students/{id}/
  PUT      /students/{id}/
  PATCH    /students/{id}/
  DELETE   /students/{id}/

The same pattern applies to `/courses/` and `/enrollments/`.

## Setup

``` bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs

-   Admin: http://127.0.0.1:8000/admin/
-   Students: http://127.0.0.1:8000/students/
-   Courses: http://127.0.0.1:8000/courses/
-   Enrollments: http://127.0.0.1:8000/enrollments/

## Architecture

``` text
Client
  ↓
Project URLs
  ↓
App URLs
  ↓
DefaultRouter
  ↓
ModelViewSet
  ↓
Serializer
  ↓
Model
  ↓
SQLite Database
```

## Learning Outcomes

-   Django Models
-   Migrations
-   Django Admin
-   Serializers
-   ModelViewSet
-   Routers
-   CRUD APIs
-   Browsable API

## Future Improvements

-   JWT Authentication
-   Permissions
-   Filtering
-   Searching
-   Pagination
-   Swagger/OpenAPI
-   PostgreSQL
-   Docker

## Author

Venkat
