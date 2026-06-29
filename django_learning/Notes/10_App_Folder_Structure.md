# Django Bootcamp - Class 3

# Chapter 10 - App Folder Structure

---

# Learning Objectives

After this chapter you will understand:

* Every file inside a Django App
* Purpose of each file
* Which files you will edit frequently
* Which files Django uses internally

---

# Default App Structure

When we run

python manage.py startapp students

Django creates

```text
students/

│
├── migrations/
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# migrations/

Stores database migration files.

Every database change generates a migration.

Example

0001_initial.py

Never delete migrations casually.

---

# **init**.py

Makes the folder a Python package.

Usually remains empty.

---

# admin.py

Registers models inside Django Admin.

Example

```python
admin.site.register(Student)
```

---

# apps.py

Contains application configuration.

Example

```python
class StudentsConfig(AppConfig):
```

Usually unchanged.

---

# models.py

Defines database tables.

Example

```python
class Student(models.Model):
```

One of the most important files.

---

# tests.py

Contains automated tests.

Used heavily in enterprise projects.

Testing ensures code quality.

---

# views.py

Contains business logic.

Every HTTP request eventually reaches a View.

Example

```python
def home(request):
```

---

# Additional Files We Will Create

urls.py

serializers.py

permissions.py

validators.py

services.py

signals.py

tasks.py

These are not generated automatically but are commonly used in real projects.

---

# Files You Will Use Most

views.py

models.py

urls.py

serializers.py

admin.py

---

# Summary

Each file has a specific responsibility.

Keeping responsibilities separate makes projects clean and maintainable.

---

# Interview Questions

1. Purpose of models.py?

2. Purpose of views.py?

3. Purpose of admin.py?

4. Why do migrations exist?

5. What is apps.py?
