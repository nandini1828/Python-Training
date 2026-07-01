# Django Class 3

# URL Routing

## Learning Objectives

After reading this document, you will understand:

- How Django maps URLs to views
- The role of `urls.py`
- How to use `path()`
- How `include()` helps organize routes
- What `urlpatterns` contains

## What is `urls.py`?

`urls.py` maps URL paths to views.
It acts like a traffic director for web requests.

## How URL Routing Works

Example:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
```

Django checks each route from top to bottom.
The first match is used.

## What is `path()`?

`path()` defines a URL pattern.

Syntax:

```python
path('route/', view, name='route-name')
```

Example:

```python
path('about/', about, name='about')
```

This means when the browser requests `/about/`, Django calls `about()`.

## What is `include()`?

`include()` lets a project delegate URL routing to an app.
It keeps the project URL file clean.

Example:

```python
path('', include('booking.urls')),
```

The project forwards root URL requests to the booking app.

## Request Flow

Browser
↓
`config/urls.py`
↓
app `urls.py`
↓
view
↓
response

## Why URL Routing Matters

Without URL routing, Django would not know which view should handle a request.
It is the core of how web requests are processed.

## Summary

You learned:

- How Django routes URLs
- What `path()` and `include()` do
- How `urlpatterns` works

## Interview Questions

1. What is `urls.py`?
2. What is `path()`?
3. What does `include()` do?
4. What is `urlpatterns`?

## Exercises

1. Add a `contact/` URL to `booking/urls.py`.
2. Create a `contact()` view in `booking/views.py`.
3. Visit `/contact/` and verify the response.
