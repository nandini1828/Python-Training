# Django Bootcamp

# Django App Commands

> This file contains all commands related to creating and managing Django Apps.
>
> **Tip:** Run all commands from the directory where `manage.py` exists.

---

# 1. Check Current Directory

Before running Django commands, make sure you are in the project root.

```bash
pwd
```

Example:

```text
.../student_management
```

You should see:

```text
manage.py
config/
students/
```

---

# 2. List Files

macOS / Linux

```bash
ls
```

Windows

```cmd
dir
```

Expected:

```text
config/
manage.py
requirements.txt
students/
```

---

# 3. Activate Virtual Environment

macOS/Linux

```bash
source .venv/bin/activate
```

Windows CMD

```cmd
.venv\Scripts\activate
```

Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Verify

```text
(.venv)
```

appears in your terminal.

---

# 4. Create a New Django App

Syntax

```bash
python manage.py startapp <app_name>
```

Example

```bash
python manage.py startapp students
```

Generated Structure

```text
students/

├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# 5. Register the App

Open

```text
config/settings.py
```

Add the app inside

```python
INSTALLED_APPS = [
]
```

Example

```python
INSTALLED_APPS = [
    "students",
]
```

Without registering the app, Django will ignore it.

---

# 6. Create urls.py

Django does NOT create this file automatically.

Create manually

```text
students/

urls.py
```

Basic template

```python
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
```

---

# 7. Create Your First View

Open

```text
students/views.py
```

Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Student Management System")
```

---

# 8. Connect App URLs to Project URLs

Open

```text
config/urls.py
```

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

# 9. Run Development Server

```bash
python manage.py runserver
```

Default URL

```text
http://127.0.0.1:8000/
```

---

# 10. Run Server on a Custom Port

```bash
python manage.py runserver 9000
```

Open

```text
http://127.0.0.1:9000/
```

---

# 11. Run Server on All Network Interfaces

Useful for testing on another device.

```bash
python manage.py runserver 0.0.0.0:8000
```

---

# 12. Stop Development Server

Press

```text
CTRL + C
```

---

# 13. Check Django Project

```bash
python manage.py check
```

Expected Output

```text
System check identified no issues (0 silenced).
```

---

# 14. Display Help

```bash
python manage.py help
```

Shows all available Django management commands.

---

# 15. Display Django Version

```bash
python manage.py version
```

or

```bash
django-admin --version
```

---

# Complete Workflow

## Step 1

Create App

```bash
python manage.py startapp students
```

↓

## Step 2

Register App

```python
INSTALLED_APPS = [
    "students",
]
```

↓

## Step 3

Create

```text
students/urls.py
```

↓

## Step 4

Create Views

```python
def home(request):
```

↓

## Step 5

Connect URLs

```python
include("students.urls")
```

↓

## Step 6

Run Server

```bash
python manage.py runserver
```

↓

Visit

```text
http://127.0.0.1:8000/
```

---

# Common Errors

## Error

```text
ModuleNotFoundError: No module named 'students'
```

Reason

* Wrong directory
* App not created
* Import typo

Solution

* Go to project root
* Verify app exists
* Restart server

---

## Error

```text
No module named 'students.urls'
```

Reason

You forgot to create

```text
students/urls.py
```

---

## Error

```text
Page not found (404)
```

Possible Causes

* URL not defined
* include() missing
* Wrong path
* Wrong URL typed in browser

---

## Error

```text
AppRegistryNotReady: Apps aren't loaded yet.
```

Reason

App is not registered in

```python
INSTALLED_APPS
```

---

## Error

```text
ImportError
```

Reason

Incorrect import statement.

Example

Wrong

```python
from views import home
```

Correct

```python
from .views import home
```

---

# Best Practices

* Create one app for one responsibility.
* Always register the app in `INSTALLED_APPS`.
* Create a separate `urls.py` for every app.
* Keep project-level `urls.py` clean by using `include()`.
* Name apps with meaningful, lowercase names (e.g., `students`, `teachers`, `payments`).
* Keep business logic inside `views.py` or service layers, not in `urls.py`.
* Always activate the virtual environment before running Django commands.
* Run commands from the project root (where `manage.py` exists).

---

# Commands Learned So Far

| Command                                   | Purpose                                |
| ----------------------------------------- | -------------------------------------- |
| `python manage.py startapp students`      | Create a new Django app                |
| `python manage.py runserver`              | Start the development server           |
| `python manage.py runserver 9000`         | Run server on port 9000                |
| `python manage.py runserver 0.0.0.0:8000` | Allow access from other devices        |
| `python manage.py check`                  | Check project configuration            |
| `python manage.py help`                   | Display all Django management commands |
| `python manage.py version`                | Show Django version                    |

---

# Interview Questions

1. What command is used to create a Django App?
2. Why must an app be added to `INSTALLED_APPS`?
3. Does Django automatically create `urls.py` inside an app?
4. What does `include()` do?
5. Where should Django management commands be executed from?
6. What happens if you forget to register an app?
7. Why should every app have its own `urls.py`?
8. Explain the typical workflow after creating a new Django app.

---

# Summary

You have learned how to:

* Create a Django App.
* Register it with the project.
* Create a basic View.
* Configure URL routing.
* Run and verify the application.
* Troubleshoot common errors.

These commands form the foundation for every Django project you'll build.
