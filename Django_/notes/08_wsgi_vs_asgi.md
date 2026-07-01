# Django Class 2

# WSGI vs ASGI

## Learning Objectives

After reading this document, you will understand:

- What WSGI is
- What ASGI is
- How they differ
- When Django uses each one
- Why both exist in a Django project

## What is WSGI?

WSGI stands for Web Server Gateway Interface.
It is the standard interface between a web server and a Python web application.

Examples:

- Gunicorn
- uWSGI
- Apache

WSGI handles traditional synchronous HTTP requests.

## What is ASGI?

ASGI stands for Asynchronous Server Gateway Interface.
It is the modern standard for asynchronous Python applications.

ASGI supports:

- async views
- WebSockets
- real-time chat
- notifications
- live streaming

## WSGI Flow

Browser
↓
Web Server
↓
WSGI
↓
Django
↓
Response

## ASGI Flow

Browser
↓
ASGI Server
↓
ASGI
↓
Django
↓
WebSocket / HTTP Response

## WSGI vs ASGI

| Feature | WSGI | ASGI |
| --- | --- | --- |
| Type | Synchronous | Asynchronous |
| HTTP | Yes | Yes |
| WebSockets | No | Yes |
| Async Views | No | Yes |
| Real-time Apps | No | Yes |

## Which One Should You Learn?

As a beginner, focus on the basics first.
Django generates both `wsgi.py` and `asgi.py` for you.

You should know:

- `wsgi.py` is used by traditional servers
- `asgi.py` enables modern asynchronous features

## Summary

You learned:

- What WSGI and ASGI are
- The difference between synchronous and asynchronous execution
- When each interface is used

## Interview Questions

1. What is WSGI?
2. What is ASGI?
3. What is the difference between WSGI and ASGI?
4. When would you use ASGI?

## Exercises

1. Open `projects/hotel_management/config/wsgi.py`.
2. Open `projects/hotel_management/config/asgi.py` if it exists or create a note explaining why it would be generated.
3. Explain the difference between `wsgi.py` and `asgi.py` in one sentence.
