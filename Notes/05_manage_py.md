# Django Class 2

# Understanding manage.py

---

# What is manage.py?

manage.py is the command-line utility provided by Django.

It acts as the control center of your Django project.

Every management command starts with:

```bash
python manage.py
```

---

# Why do we need manage.py?

Instead of writing Python code to control Django manually,

we simply execute commands like:

```bash
python manage.py runserver
```

Django automatically loads the project configuration and performs the requested task.

---

# Real-Life Analogy

Think of manage.py as the remote control of your television.

Without the remote:

You must manually operate every button.

With the remote:

You simply press:

* Power
* Volume
* Channel

Similarly,

manage.py allows you to:

* Run Server
* Create App
* Run Migrations
* Create Superuser
* Collect Static Files

---

# How manage.py Works

When executed:

```bash
python manage.py runserver
```

The following happens:

1. Python starts.
2. manage.py executes.
3. Django loads settings.py.
4. Django initializes the project.
5. Requested command executes.

---

# Important Commands

Run Server

```bash
python manage.py runserver
```

Create App

```bash
python manage.py startapp students
```

Run Migrations

```bash
python manage.py migrate
```

Create Migration

```bash
python manage.py makemigrations
```

Create Superuser

```bash
python manage.py createsuperuser
```

Check Project

```bash
python manage.py check
```

List Commands

```bash
python manage.py help
```

---

# Why Every Command Starts with manage.py

Because manage.py knows:

* Project Settings
* Installed Apps
* Database Configuration
* Environment Variables

Without manage.py, Django doesn't know which project to use.

---

# Summary

You learned:

* Purpose of manage.py
* Startup process
* Common management commands
* Why every Django command uses manage.py

---

# Interview Questions

1. What is manage.py?
2. Why is manage.py required?
3. What happens when we execute runserver?
4. Can Django work without manage.py?
