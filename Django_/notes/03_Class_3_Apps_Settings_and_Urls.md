# Class 3: Apps, settings.py, and URL Routing

## Learning Objectives

After this class, you will understand:

- What a Django app is
- How to create and register an app
- What `settings.py` does
- How to work with `manage.py`
- How to route URLs using `include()`

## What is a Django App?

A Django app is a self-contained module that provides a feature.

Example:

- `booking`
- `customers`
- `rooms`

Apps make projects modular and reusable.

## Creating an App

Run:

```bash
python manage.py startapp booking
```

A new app folder contains:

- `admin.py`
- `apps.py`
- `models.py`
- `views.py`
- `tests.py`
- `migrations/`
- `__init__.py`

## Registering the App

Open `config/settings.py` and add the app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'booking',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

If the app is not registered, Django will not load it.

## Understanding `settings.py`

`settings.py` contains project configuration such as:

- installed apps
- database settings
- middleware
- templates
- static files
- timezone
- security settings

## `manage.py`

`manage.py` is the command utility for Django.
It loads the project settings and executes commands.

Examples:

- `python manage.py runserver`
- `python manage.py migrate`
- `python manage.py startapp booking`
- `python manage.py createsuperuser`

## URL Routing

Create `booking/urls.py` with:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

Then include it in `config/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
]
```

## Summary

Class 3 covered:

- apps and app registration
- `settings.py`
- `manage.py`
- URL routing

## Interview Questions

1. What is a Django app?
2. Why register an app in `INSTALLED_APPS`?
3. What does `include()` do?
4. What is the purpose of `manage.py`?
5. How do you organize URLs in a Django project?

## Exercises

1. Create a new app named `customers`.
2. Register `customers` in `INSTALLED_APPS`.
3. Create a simple view and URL in `customers`.
