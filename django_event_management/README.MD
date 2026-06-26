# Django REST Framework Learning Notes

## Project Overview

Built an Event Management System using Django and Django REST Framework (DRF).

### Models

- Organizer
- Event
- Registration

Relationships:

text Organizer     │     │ 1     ▼ Event     │     │ 1     ▼ Registration 

---

# 1. Project Setup

## Create Project

bash mkdir django_event_management cd django_event_management 

## Create Virtual Environment

bash python3 -m venv venv 

Activate Virtual Environment

bash source venv/bin/activate 

## Install Packages

bash pip install django pip install djangorestframework pip install pytest pip install pytest-django 

## Create Django Project

bash django-admin startproject config . 

## Create Django App

bash python manage.py startapp events 

---

# 2. Register Applications

Inside config/settings.py

python INSTALLED_APPS = [     ...     "rest_framework",     "events", ] 

---

# 3. Models

Created three models.

## Organizer

Fields

- name
- email
- phone
- company
- created_at

Used Data Types

- CharField
- EmailField
- DateTimeField

---

## Event

Fields

- title
- description
- date
- venue
- price
- is_active
- organizer

Used Data Types

- CharField
- TextField
- DateField
- DecimalField
- BooleanField
- ForeignKey

Relationship

text One Organizer       │       ▼ Many Events 

---

## Registration

Fields

- attendee_name
- attendee_email
- tickets
- payment_done
- registered_at
- event

Used Data Types

- CharField
- EmailField
- IntegerField
- BooleanField
- DateTimeField
- ForeignKey

Relationship

text One Event       │       ▼ Many Registrations 

---

# 4. str() Method

Added string representation for all models.

Example

python def __str__(self):     return self.name 

Purpose

Instead of

text Organizer object (1) 

Django Admin displays

text OpenAI 

---

# 5. Migrations

## Generate Migration

bash python manage.py makemigrations 

Purpose

Creates migration files based on changes in models.

Generated

text events/migrations/0001_initial.py 

---

## Apply Migration

bash python manage.py migrate 

Purpose

Creates actual tables inside the database.

Database

text db.sqlite3 

Created tables

- events_organizer
- events_event
- events_registration

---

# 6. Django Admin

Registered models.

python admin.site.register(Organizer) admin.site.register(Event) admin.site.register(Registration) 

Created Admin User

bash python manage.py createsuperuser 

Run Server

bash python manage.py runserver 

Admin URL

text http://127.0.0.1:8000/admin/ 

Capabilities

- Add Records
- Update Records
- Delete Records
- View Records

---

# 7. Serializers

Created

text events/serializers.py 

Serializers

- OrganizerSerializer
- EventSerializer
- RegistrationSerializer

Example

python class OrganizerSerializer(serializers.ModelSerializer):      class Meta:         model = Organizer         fields = "__all__" 

Purpose

Converts

text Python Object       ⇅ JSON 

---

# 8. ViewSets

Created

text events/views.py 

ViewSets

- OrganizerViewSet
- EventViewSet
- RegistrationViewSet

Example

python class OrganizerViewSet(viewsets.ModelViewSet):     queryset = Organizer.objects.all()     serializer_class = OrganizerSerializer 

Purpose

Automatically provides CRUD operations.

---

# 9. Router

Created

text events/urls.py 

Router

python router = DefaultRouter()  router.register("organizers", OrganizerViewSet) router.register("events", EventViewSet) router.register("registrations", RegistrationViewSet) 

Connected to project URLs

python path("api/", include("events.urls")) 

---

# 10. CRUD APIs

Automatically generated endpoints.

## Organizer

text GET     /api/organizers/ GET     /api/organizers/1/ POST    /api/organizers/ PUT     /api/organizers/1/ PATCH   /api/organizers/1/ DELETE  /api/organizers/1/ 

Same for

- Events
- Registrations

---

# 11. HTTP Methods

## GET

Retrieve data.

Example

http GET /api/events/ 

---

## POST

Create new data.

Example

http POST /api/events/ 

---

## PUT

Replace the entire object.

Example

http PUT /api/events/1/ 

---

## PATCH

Update only selected fields.

Example

http PATCH /api/events/1/ 

---

## DELETE

Delete a record.

Example

http DELETE /api/events/1/ 

---

# 12. Request Flow

text Client    │ HTTP Request (GET, POST, PUT, PATCH, DELETE)    │ URL Router    │ ViewSet    │ Serializer    │ Model    │ SQLite Database    │ JSON Response 

---

# 13. Data Types Used

| Field Type | Usage |
|------------|-------|
| CharField | Name, Title |
| TextField | Description |
| EmailField | Email |
| IntegerField | Tickets |
| DecimalField | Price |
| BooleanField | Payment Status |
| DateField | Event Date |
| DateTimeField | Created Date |
| ForeignKey | Relationships |

---

# 14. Basic Pytest

Installed

bash pip install pytest pip install pytest-django 

Created

text pytest.ini 

Configuration

ini [pytest] DJANGO_SETTINGS_MODULE = config.settings python_files = tests.py test_*.py *_tests.py 

---

# 15. Model Tests

Created

text tests/test_models.py 

Tested

- Organizer creation
- Event creation
- ForeignKey relationship

Used

python assert 

Example

python assert organizer.name == "OpenAI" 

---

# 16. API Tests

Created

text tests/test_api.py 

Used

python APIClient() 

Tested

### GET API

python response = client.get("/api/organizers/") assert response.status_code == 200 

---

### POST API

python response = client.post(...) assert response.status_code == 201 

---

# 17. HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content (Deleted Successfully) |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# 18. Run Tests

Execute

bash python -m pytest 

Result

text ============================= 4 passed in 0.12s ============================= 

Meaning

- Django configured successfully
- Models working
- APIs working
- Tests passed successfully

---

# Project Folder Structure

text django_event_management/  config/     settings.py     urls.py  events/     migrations/     admin.py     models.py     serializers.py     urls.py     views.py  tests/     test_models.py     test_api.py  db.sqlite3 manage.py pytest.ini venv/ 

---

# Key Concepts Learned

- Django Project Structure
- Django Apps
- Models
- Model Relationships
- Django ORM
- Migrations
- Django Admin
- Django REST Framework
- Serializers
- ModelViewSet
- Routers
- URL Configuration
- CRUD Operations
- REST APIs
- HTTP Methods
- HTTP Status Codes
- JSON Serialization
- SQLite Database
- Basic Pytest
- API Testing
- Model Testing

---

# Final Outcome

Successfully built an Event Management REST API with:

- 3 related database models
- Full CRUD APIs using ModelViewSet
- Automatic URL routing using DefaultRouter
- SQLite database integration
- Django Admin support
- REST API testing
- Model testing using pytest
- All tests passing successfully