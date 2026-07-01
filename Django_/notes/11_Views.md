# Django Class 3

# Understanding Views

## Learning Objectives

After reading this document, you will understand:

- What a view is in Django
- The difference between function-based views and class-based views
- How views receive requests and return responses
- How to write a simple view
- How views connect to URLs

## What is a View?

A view is the code that runs when Django receives a request.
It contains the logic needed to build a response.

In Django, views are usually defined in `views.py`.

## Function-Based Views

Example:

```python
from django.http import HttpResponse


def home(request):
    return HttpResponse('Welcome')
```

This is the simplest form of a view.

### What happens in a function-based view?

1. The URL router finds the view.
2. Django creates a `request` object.
3. The view runs.
4. The view returns an `HttpResponse`.

## Class-Based Views

Class-based views are more powerful and reusable.
They use classes instead of functions.

Example:

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse('Welcome')
```

## Request Object

The `request` object contains:

- headers
- method (`GET`, `POST`, etc.)
- user information
- cookies
- query parameters
- request body

## Response Object

The simplest response is `HttpResponse`.

Example:

```python
return HttpResponse('Hello World')
```

Django also provides other response types:

- `JsonResponse`
- `HttpResponseRedirect`
- `TemplateResponse`

## Connecting Views to URLs

Open `booking/urls.py` and add routes:

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```

## Summary

You learned:

- What a Django view is
- How to write a function-based view
- How a view receives a request and returns a response
- The role of the `request` object

## Interview Questions

1. What is a view in Django?
2. What is `HttpResponse`?
3. What is the `request` object?
4. What is the difference between function-based and class-based views?

## Exercises

1. Create an `about()` view in `booking/views.py`.
2. Return a different message in the `about()` view.
3. Add a URL for `/about/` and test it in your browser.
