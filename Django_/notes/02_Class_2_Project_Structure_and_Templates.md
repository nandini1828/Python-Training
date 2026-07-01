# Class 2: Create First Django Project

## Learning Objectives

After this class, you will understand:

- How to create a Django project
- How to run the development server
- The role of `urls.py` and `views.py`
- How templates work
- How static files work

## Create a Django Project

Run:

```bash
django-admin startproject config .
```

This creates:

- `manage.py`
- `config/`
- `config/settings.py`
- `config/urls.py`
- `config/wsgi.py`
- `config/asgi.py`

## Run the development server

From the project root, run:

```bash
python manage.py runserver
```

Open:

`http://127.0.0.1:8000/`

## `urls.py`

This file maps URLs to views.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## `views.py`

A view receives a request and returns a response.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Django!')
```

## Templates

Templates are HTML files that Django renders.

Create a template folder and add a file:

- `booking/templates/booking/home.html`

Example template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hotel Management</title>
</head>
<body>
    <h1>Welcome to Hotel Management</h1>
</body>
</html>
```

Render the template in a view:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'booking/home.html')
```

## Static Files

Static files are CSS, JavaScript, and images.

Example setting in `settings.py`:

```python
STATIC_URL = '/static/'
```

Put files in a `static/` folder and load them in templates.

## Summary

Class 2 covered:

- creating a project
- running the server
- `urls.py`
- `views.py`
- templates
- static files

## Interview Questions

1. How do you start a Django development server?
2. What is `urls.py` used for?
3. What does `render()` do?
4. Where do you put templates?
5. How does Django serve static files in development?

## Exercises

1. Create a `home` view and URL.
2. Create a template for the home page.
3. Display the template in your browser.
