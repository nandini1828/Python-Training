# Django Class 3

# Request / Response Cycle

## Learning Objectives

After reading this document, you will understand:

- How a browser request travels through Django
- What happens inside `urls.py`
- How views generate responses
- The difference between request and response objects
- Why the cycle is important for web development

## Request / Response Flow

When a user visits `http://127.0.0.1:8000/`:

Browser
↓
Django server
↓
`config/urls.py`
↓
`booking/urls.py`
↓
`booking/views.py`
↓
`HttpResponse`
↓
Browser

## Step-by-Step Flow

1. The browser sends an HTTP request.
2. Django receives the request.
3. `config/urls.py` matches the URL.
4. The matching app `urls.py` is loaded.
5. The requested view is executed.
6. The view returns a response.
7. Django sends the response back to the browser.

## What is the Request Object?

The request object contains:

- HTTP method (`GET`, `POST`, etc.)
- headers
- user data
- cookies
- query parameters
- request body

## What is the Response Object?

The response object contains the data sent back to the browser.
The simplest response is `HttpResponse`.

Example:

```python
return HttpResponse('Hello')
```

The browser receives the response and displays it.

## Why the Cycle Matters

Understanding this cycle helps you debug problems.
When a page does not load, the issue is usually in:

- URL routing
- view logic
- templates
- middleware

## Summary

You learned:

- How Django processes requests
- The role of `urls.py` and views
- What request and response objects are

## Interview Questions

1. What is the Django request-response cycle?
2. What is the role of `urls.py`?
3. What does a view return?
4. What information does the request object contain?

## Exercises

1. Draw the request flow for your `home` view.
2. Add a new `contact` page and trace the flow from browser to response.
3. Explain why `include()` is useful in the flow.
