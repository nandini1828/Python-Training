# Django Class 2

# Understanding urls.py

## Learning Objectives

After reading this document, you will understand:

- What `urls.py` is
- How URL routing works in Django
- How Django finds the correct view for a request
- How to use `path()` and `include()`
- Why `urls.py` is critical for every app

## What is `urls.py`?

`urls.py` is responsible for URL routing.
It decides which view should execute when a user visits a URL.

## Example

When a user opens:

```text
http://127.0.0.1:8000/
```

Django checks:

- `config/urls.py`
- app url modules like `booking/urls.py`
- matching route in `urlpatterns`
- executes the matched view
- returns a response

## URL Routing

Example:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

Later we can add routes such as:

- `students/`
- `teachers/`
- `courses/`
- `login/`
- `logout/`

## Real-Life Example

Think of `urls.py` as a receptionist.
A visitor arrives.
The receptionist asks: "Which department do you want?"
Then directs the visitor to the correct room.

Similarly, `urls.py` directs requests to the correct view.

## Why URL Routing is Important

Without URL routing, Django would not know which code to execute.
Every incoming request passes through URL routing.

## Request Flow

Browser
↓
URL
↓
`urls.py`
↓
View
↓
Database
↓
Response
↓
Browser

## Summary

You learned:

- What `urls.py` does
- How Django routes requests
- The importance of `urlpatterns`

## Interview Questions

1. What is `urls.py`?
2. What is URL routing?
3. Explain the request flow.
4. What is `urlpatterns`?
5. What does `include()` do?

## Exercises

1. Open `projects/hotel_management/config/urls.py` and explain each line.
2. Create `booking/urls.py` if it does not exist.
3. Add a new path `about/` and connect it to a simple view.
