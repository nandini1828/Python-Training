# Django Bootcamp - Class 3

# Chapter 12 - URL Routing

---

# Learning Objectives

After this chapter you will understand:

* What is URL Routing?
* Why URL Routing is important
* Project URLs vs App URLs
* include() function
* path() function
* URL naming
* URL request flow
* Best practices

---

# What is URL Routing?

URL Routing is the process of mapping a URL (web address) to a specific Django View.

When a user visits a URL, Django checks its URL configuration and decides which View should execute.

---

# Real Life Analogy

Imagine a hotel.

A guest arrives at reception.

The receptionist asks:

"What room do you want?"

Depending on the room number,

the receptionist sends the guest to the correct room.

Similarly,

Browser

↓

URL

↓

urls.py

↓

Correct View

---

# Example

Suppose a user opens

```text
http://127.0.0.1:8000/
```

Django checks

config/urls.py

↓

students/urls.py

↓

home()

↓

Response

---

# Project URLs

Location

config/urls.py

Purpose

Routes requests to different Django Apps.

Example

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
]
```

---

# App URLs

Location

students/urls.py

Purpose

Routes requests inside the students app.

Example

```python
from django.urls import path
from .views import home, about

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
]
```

---

# Understanding path()

Syntax

```python
path(route, view, kwargs=None, name=None)
```

Parameters

route

The URL pattern.

Example

students/

about/

login/

view

The function or class executed.

name

A unique name for the URL.

Used for URL reversing.

---

# Example

```python
path("", home, name="home")
```

Meaning

If user visits

/

Execute

home()

---

# Another Example

```python
path("about/", about, name="about")
```

If user visits

/about/

Execute

about()

---

# include()

Purpose

Splits URL configuration into multiple files.

Instead of putting every URL in one file,

we delegate URLs to apps.

Example

```python
path("", include("students.urls"))
```

Meaning

"If the URL belongs to the students app,

let students.urls handle it."

---

# URL Flow

Browser

↓

config/urls.py

↓

students/urls.py

↓

View

↓

Business Logic

↓

Response

↓

Browser

---

# URL Naming

Bad

```python
path("about/", about)
```

Good

```python
path("about/", about, name="about")
```

Why?

Later we can refer to URLs using their names instead of hardcoding paths.

---

# Enterprise Example

Project

Student Management

Apps

students

teachers

courses

Each app has its own urls.py

config/urls.py only includes them.

This keeps the project clean.

---

# Common Mistakes

Putting every URL inside config/urls.py

Forgetting include()

Forgetting to create app urls.py

Forgetting URL names

Importing views incorrectly

---

# Best Practices

Every app should have its own urls.py.

Always use URL names.

Keep project URLs clean.

Group related routes together.

---

# Summary

You learned

* URL Routing
* path()
* include()
* Project URLs
* App URLs
* URL Naming
* Request Routing

---

# Interview Questions

1. What is URL Routing?

2. Difference between Project URLs and App URLs?

3. Why do we use include()?

4. Explain path().

5. Why should URLs have names?

6. What happens when a browser requests a URL?
