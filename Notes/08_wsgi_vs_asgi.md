# Django Class 2

# WSGI vs ASGI

---

# What is WSGI?

WSGI stands for:

Web Server Gateway Interface

It is the standard interface between a web server and a Python web application.

Examples:

* Gunicorn
* uWSGI
* Apache

WSGI handles traditional synchronous HTTP requests.

---

# What is ASGI?

ASGI stands for:

Asynchronous Server Gateway Interface

It is the modern standard for asynchronous Python applications.

Supports:

* Async Views
* WebSockets
* Real-time Chat
* Notifications
* Live Streaming

---

# WSGI Flow

Browser

↓

Web Server

↓

WSGI

↓

Django

↓

Response

---

# ASGI Flow

Browser

↓

ASGI Server

↓

ASGI

↓

Django

↓

WebSocket / HTTP Response

---

# WSGI vs ASGI

| Feature        | WSGI        | ASGI         |
| -------------- | ----------- | ------------ |
| Type           | Synchronous | Asynchronous |
| HTTP           | Yes         | Yes          |
| WebSockets     | No          | Yes          |
| Async Views    | No          | Yes          |
| Real-time Apps | No          | Yes          |

---

# Which One Should You Learn?

As a beginner,

don't worry about deployment yet.

Just know:

* wsgi.py is used by traditional servers.
* asgi.py enables modern asynchronous features.

You'll use both automatically—Django generates them for you.

---

# Summary

You learned:

* What WSGI is
* What ASGI is
* Difference between synchronous and asynchronous execution
* When each is used

---

# Interview Questions

1. What is WSGI?
2. What is ASGI?
3. Difference between WSGI and ASGI?
4. When would you use ASGI?
