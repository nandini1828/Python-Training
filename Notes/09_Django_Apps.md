# Django Bootcamp - Class 3

# Chapter 09 - Django Apps

---

# Learning Objectives

After completing this chapter, you will understand:

* What is a Django App?
* Why Django uses Apps
* Difference between Project and App
* Real-world examples
* Enterprise architecture
* Best practices

---

# What is a Django App?

A Django App is a **self-contained Python module** that provides a specific feature or functionality within a Django project.

Think of an app as a **building block**.

Multiple apps together form a complete Django project.

---

# Simple Definition

Project = Entire Application

App = One Feature inside the Application

---

# Real-Life Example

Suppose you are building a Hospital Management System.

The complete project is:

Hospital Management System

Inside it you have different departments.

Each department becomes a Django App.

```text
Hospital Management System

│
├── Patients
├── Doctors
├── Billing
├── Pharmacy
├── Authentication
├── Reports
└── Notifications
```

Each app focuses on only one responsibility.

---

# Another Example

Amazon

Project

Apps

* Authentication
* Products
* Orders
* Cart
* Payments
* Delivery
* Reviews

Each app works independently.

---

# Why Django Uses Apps

Imagine putting 100,000 lines of code into one file.

Problems:

* Difficult to maintain
* Difficult to debug
* Difficult to test
* Difficult to understand

Instead,

Django divides everything into apps.

Benefits:

✔ Better organization

✔ Reusable code

✔ Easier testing

✔ Easier teamwork

✔ Better scalability

---

# Project vs App

| Project                | App                            |
| ---------------------- | ------------------------------ |
| Complete website       | One module                     |
| Contains multiple apps | Contains related functionality |
| Global settings        | Local functionality            |
| One per website        | Many inside a project          |

---

# Enterprise Example

Student Management System

Apps:

students

teachers

courses

attendance

authentication

payments

notifications

Each team in a company can work on one app.

---

# Creating an App

Command:

python manage.py startapp students

Django automatically creates the app structure.

---

# Registering an App

Creating an app is not enough.

You must register it.

settings.py

INSTALLED_APPS

```python
INSTALLED_APPS = [
    "students",
]
```

Without registration,

Django ignores the app.

---

# App Lifecycle

Create App

↓

Register App

↓

Create Models

↓

Create Views

↓

Create URLs

↓

Connect URLs

↓

Run Server

---

# Naming Convention

Good

students

teachers

payments

inventory

Bad

studentApp

test123

abc

mydjangoapp

Always use meaningful lowercase names.

---

# Best Practices

One responsibility per app.

Don't mix unrelated features.

Keep apps small and maintainable.

Use plural names when appropriate.

Keep reusable code inside apps.

---

# Common Beginner Mistakes

Creating too many apps.

Putting everything inside one app.

Forgetting to register the app.

Using confusing names.

---

# Summary

A Django App is a reusable module that performs one responsibility.

Multiple apps together form one Django project.

Apps help organize, scale, and maintain applications efficiently.

---

# Interview Questions

1. What is a Django App?

2. Difference between Project and App?

3. Why do enterprise applications have multiple apps?

4. Why should apps have a single responsibility?

5. Why must we register apps in INSTALLED_APPS?
