# Class 1: What is Django?

## Learning Objectives

After this class, you will understand:

- What Django is and why it is used
- How the internet works at a high level
- HTTP request and response basics
- MVC vs MVT architecture
- The Django project folder structure
- How to create and activate a virtual environment
- How to install Django

## What is Django?

Django is a high-level Python web framework.
It helps developers build web applications quickly with clean, reusable code.

Django is designed for:

- rapid development
- clean architecture
- built-in security
- scalable applications

## How the Internet Works

When you open a website in a browser:

1. The browser sends an HTTP request to a server.
2. The server processes the request.
3. The server sends an HTTP response back.
4. The browser renders the response.

This is the basic internet request-response cycle.

## HTTP Basics

HTTP is the protocol used by browsers and web servers.

Common HTTP methods:

- `GET` — request data from the server
- `POST` — send data to the server
- `PUT` — update data
- `DELETE` — delete data

A request includes:

- URL
- method
- headers
- body (optional)

A response includes:

- status code
- headers
- body

## Request & Response in Django

Django receives an HTTP request and returns an HTTP response.
A view is the code that handles the request and creates the response.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, Django!')
```

## MVC vs MVT

Django uses the Model-View-Template (MVT) pattern.

### MVC

- Model — data layer
- View — UI layer
- Controller — business logic and request routing

### MVT

- Model — data layer
- View — logic that handles requests and responses
- Template — HTML presentation layer

In Django, the view acts like the controller.

## Django Project Structure

A Django project contains:

- `manage.py` — command utility
- `config/` — settings and URL configuration
- apps — reusable modules for features
- `requirements.txt` — dependencies

## Virtual Environment

A virtual environment isolates project packages.

Create one:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Install Django

Install Django with pip:

```bash
pip install django
```

Verify installation:

```bash
django-admin --version
```

## Summary

Class 1 covered:

- Django basics
- how the internet works
- HTTP
- request/response
- MVC vs MVT
- project structure
- virtual env
- installing Django

## Interview Questions

1. What is Django?
2. What is HTTP?
3. What is the difference between MVC and MVT?
4. Why use a virtual environment?
5. What does `manage.py` do?

## Exercises

1. Create and activate a virtual environment.
2. Install Django.
3. Write the difference between `GET` and `POST` in your own words.
