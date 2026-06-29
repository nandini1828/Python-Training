# Django Class 2

# Understanding urls.py

---

# What is urls.py?

urls.py is responsible for URL routing.

It decides which View should execute when a user requests a URL.

---

# Example

User opens:

```text
http://127.0.0.1:8000/
```

Django checks:

urls.py

↓

Find matching path

↓

Execute View

↓

Return Response

---

# URL Routing

Example:

```python
urlpatterns = [
]
```

Later we'll add routes like:

```text
students/
teachers/
courses/
login/
logout/
```

---

# Real-Life Example

Think of urls.py as a receptionist.

A visitor arrives.

Reception asks:

"Which department do you want?"

Then directs the visitor to the correct room.

Similarly,

urls.py directs requests to the correct view.

---

# Why URL Routing is Important

Without URL routing,

Django would not know which code to execute.

Every request passes through urls.py.

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

# Summary

You learned:

* URL Routing
* Request Flow
* Importance of urlpatterns

Next class we'll start creating our own URLs.

---

# Interview Questions

1. What is urls.py?
2. What is URL routing?
3. Explain the request flow.
4. What is urlpatterns?
