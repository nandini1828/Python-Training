# Django Bootcamp - Class 3

# Chapter 13 - Request Response Cycle

---

# Learning Objectives

After this chapter you will understand:

* What is an HTTP Request?
* What is an HTTP Response?
* Complete Django Request Flow
* Request Object
* Response Object
* Browser to Database communication

---

# What is a Request?

A Request is a message sent by the client (browser, mobile app, Postman, frontend) asking the server to perform an action.

Examples

Open homepage

Login

Fetch students

Create student

Delete student

---

# Example Request

Browser requests

GET /

Server receives

Request Object

---

# What is a Response?

A Response is the data returned by the server.

Examples

HTML

JSON

Image

PDF

Error Message

---

# Complete Request Flow

Step 1

User enters URL

↓

Browser sends HTTP Request

↓

Django receives request

↓

manage.py

↓

settings.py

↓

Middleware

↓

config/urls.py

↓

students/urls.py

↓

View

↓

Business Logic

↓

Database (optional)

↓

Response Object

↓

Browser displays response

---

# Visual Diagram

```text
User

↓

Browser

↓

HTTP Request

↓

Web Server

↓

Django

↓

URL Routing

↓

View

↓

Database

↓

View

↓

HTTP Response

↓

Browser

↓

User
```

---

# Request Object

Django automatically creates a request object.

Example

```python
def home(request):
```

The request object contains

* Method
* Headers
* Cookies
* Query Parameters
* User
* Session
* Files

Later we'll explore these in detail.

---

# Response Object

Every View must return a Response.

Examples

HttpResponse

JsonResponse

FileResponse

StreamingHttpResponse

TemplateResponse

---

# Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

Browser receives

Hello Django

---

# Database Interaction

Sometimes Views need data.

Flow

Browser

↓

Request

↓

View

↓

Database

↓

Student Records

↓

View

↓

JSON Response

↓

Browser

---

# Why Understanding This Flow is Important

Everything in Django follows this cycle.

Whether you build

* Websites
* REST APIs
* Authentication
* Admin Panel
* AI Backend

The request-response cycle remains the same.

---

# Common Mistakes

Returning plain strings.

Not returning any response.

Writing logic outside Views.

Ignoring request data.

---

# Best Practices

Keep Views small.

Move complex logic to services.

Validate request data.

Return proper status codes.

---

# Summary

Every interaction with Django starts with a Request and ends with a Response.

Understanding this flow is the foundation for learning Django REST Framework.

---

# Interview Questions

1. What is an HTTP Request?

2. What is an HTTP Response?

3. Explain the Django Request Response Cycle.

4. What does the request object contain?

5. What are different types of Response objects?

6. Why must every View return a Response?
