# Django Class 2

# Django Project Structure

---

# Learning Objectives

After reading this document, you will understand:

* What a Django Project is
* The folder structure of a Django project
* Purpose of each generated file
* Difference between Project and App
* How Django starts

---

# What is a Django Project?

A Django Project is the complete web application.

Think of it as the **main container** that holds everything required to build a website or an API.

Examples:

* Student Management System
* Hospital Management System
* Banking Application
* E-Commerce Website
* CRM Software

A project can contain one or many Django Apps.

---

# Django Project Structure

When you create a project using

```bash
django-admin startproject config .
```

Django generates:

```text
student_management/

│── .venv/
│── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── manage.py
│── requirements.txt
```

---

# Understanding the Structure

## .venv

Contains the project's isolated Python environment.

Includes:

* Python Interpreter
* pip
* Installed Libraries
* Scripts

Never edit this folder manually.

---

## config/

This is the configuration package of the project.

It contains all important configuration files.

Think of it as the "brain" of the project.

---

## manage.py

The command-line utility used to interact with Django.

Examples:

* Run Server
* Create App
* Run Migrations
* Create Admin User

---

## requirements.txt

Stores all installed Python packages.

Example:

```text
Django==5.x.x
```

Anyone can recreate the same environment using:

```bash
pip install -r requirements.txt
```

---

# Project vs App

Project

A complete website or API.

Example:

Hospital Management

Apps inside it:

* Patient
* Doctor
* Billing
* Authentication
* Reports

App

A small module responsible for one feature.

Apps make projects modular and reusable.

---

# How Django Starts

When we execute:

```bash
python manage.py runserver
```

Django follows this flow:

manage.py

↓

settings.py

↓

urls.py

↓

View

↓

Database (if required)

↓

Response

↓

Browser

---

# Why is this Structure Important?

Benefits:

* Organized code
* Easy maintenance
* Modular design
* Easier debugging
* Better scalability

Large companies may have dozens of Django apps inside one project.

---

# Summary

You learned:

* What a Django Project is
* Project Structure
* Project vs App
* Django Startup Flow
* Importance of Modular Architecture

---

# Interview Questions

1. What is a Django Project?
2. Explain the Django Project Structure.
3. Difference between Project and App?
4. Why do enterprise applications use multiple apps?
5. Explain the startup flow of Django.
