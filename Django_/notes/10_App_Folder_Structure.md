# Django Class 3

# App Folder Structure

## Learning Objectives

After reading this document, you will understand:

- What files are created inside a new app
- What each file is used for
- Why app structure is important
- How apps remain reusable

## App Folder Structure

When you create an app using:

```bash
python manage.py startapp booking
```

Django creates:

```
booking/
├── admin.py
├── apps.py
├── __init__.py
├── migrations/
├── models.py
├── tests.py
├── views.py
```

## Understanding Each File

### `admin.py`

Purpose: Register models with Django Admin.

Example:

```python
from django.contrib import admin
from .models import Room

admin.site.register(Room)
```

### `apps.py`

Contains application configuration.
Usually you only change the app name or label.

Example:

```python
from django.apps import AppConfig

class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
```

### `models.py`

Defines database tables.
Each class becomes a table in the database.

Example:

```python
class Room(models.Model):
    room_number = models.CharField(max_length=10)
```

### `views.py`

Contains business logic.
Each view function or class handles one request.

Example:

```python
def home(request):
    return HttpResponse('Hello')
```

### `tests.py`

Used for automated testing.
Enterprise projects rely on tests for quality.

Example:

```python
class BookingTests(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```

### `migrations/`

Stores database migration history.
Each time you change models, Django generates a migration file.
Do not delete migrations casually.

### `__init__.py`

Makes the app a Python package.
Without it, Python cannot import the app.

## Why App Structure Matters

A clear app structure makes it easy to find code.
It also helps teams work together without confusion.

## Best Practices

- Keep each app focused on one area.
- Name apps after functionality.
- Avoid putting unrelated models or views in the same app.
- Use app-level `urls.py` for routing.

## Summary

You learned:

- App folder structure
- Purpose of each file inside an app
- Why apps should stay focused

## Interview Questions

1. What is `models.py`?
2. What is `views.py`?
3. What is `admin.py`?
4. Why should an app be self-contained?
5. What is stored in `migrations/`?

## Exercise

Open `projects/hotel_management/booking` and identify each file.
