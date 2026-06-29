# Django Bootcamp - Class 3

# Chapter 11 - Django Views

---

# Learning Objectives

After this chapter you will understand:

* What is a View?
* Why Views exist
* Request Object
* Response Object
* HttpResponse
* View lifecycle

---

# What is a View?

A View is a Python function or class that receives an HTTP request and returns an HTTP response.

It contains the business logic of your application.

---

# Request Flow

Browser

↓

URL

↓

urls.py

↓

View

↓

Database

↓

Response

↓

Browser

---

# Our First View

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Student Management System")
```

---

# Understanding the Code

Import HttpResponse

Allows Django to send data back to the browser.

---

# request

Whenever a user visits your website,

Django creates a request object.

It contains

* HTTP Method
* Headers
* Cookies
* User
* Query Parameters
* Form Data

---

# Response

The View must always return a response.

Examples

HttpResponse

JsonResponse

TemplateResponse

FileResponse

StreamingHttpResponse

---

# HttpResponse

Simplest response.

Example

```python
return HttpResponse("Hello Django")
```

Browser displays

Hello Django

---

# Multiple Views

Example

```python
def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")
```

Each URL points to one View.

---

# Why Views Exist

Views contain business logic.

Examples

Fetch students

Calculate marks

Store attendance

Authenticate users

Return API responses

---

# Function-Based View (FBV)

Simple Python function.

Easy to understand.

Good for beginners.

---

# Class-Based View (CBV)

Python class.

Reusable.

Supports inheritance.

Used in enterprise applications.

Later we'll learn

APIView

GenericAPIView

ModelViewSet

---

# Common Mistakes

Returning plain strings.

Forgetting HttpResponse.

Writing database logic everywhere.

Putting unrelated code inside one View.

---

# Summary

A View is the heart of a Django application.

Every request reaches a View.

The View processes the request and returns a response.

---

# Interview Questions

1. What is a View?

2. Difference between Request and Response?

3. What is HttpResponse?

4. Function-Based View vs Class-Based View?

5. What information does the request object contain?
