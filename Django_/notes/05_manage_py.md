# Django Class 2

# Understanding manage.py

## Learning Objectives

After reading this document, you will understand:

- What `manage.py` is
- Why it is required in every Django project
- How Django commands work
- Common management commands
- Why you should run commands from the project root

## What is `manage.py`?

`manage.py` is the command-line utility provided by Django.
It acts as the control center for your Django project.

Every Django management command starts with:

```bash
python manage.py <command>
```

## Why do we need `manage.py`?

Instead of writing Python code manually to configure Django,
we use `manage.py` to load the project settings and execute tasks.

Examples:

- Run development server
- Create a new app
- Run migrations
- Create a superuser

## Real-Life Analogy

Think of `manage.py` as the remote control for your television.
Without the remote, you would have to manually operate every button.
With the remote, you can instantly run commands.

Similarly, `manage.py` allows you to:

- run the server
- create apps
- migrate databases
- create users
- collect static files

## How `manage.py` Works

When executed:

```bash
python manage.py runserver
```

The following happens:

1. Python starts
2. `manage.py` executes
3. Django loads `settings.py`
4. Django initializes the project
5. The requested command executes

## Important Commands

Run server:

```bash
python manage.py runserver
```

Create app:

```bash
python manage.py startapp booking
```

Run migrations:

```bash
python manage.py migrate
```

Create migration files:

```bash
python manage.py makemigrations
```

Create superuser:

```bash
python manage.py createsuperuser
```

Check project for issues:

```bash
python manage.py check
```

List commands:

```bash
python manage.py help
```

## Why Every Command Starts with `manage.py`

Because `manage.py` knows:

- project settings
- installed apps
- database configuration
- environment variables

Without `manage.py`, Django would not know which project to use.

## Summary

You learned:

- The purpose of `manage.py`
- How it starts Django
- Common management commands
- Why `manage.py` is essential

## Interview Questions

1. What is `manage.py`?
2. Why is `manage.py` required?
3. What happens when you run `runserver`?
4. Can Django work without `manage.py`?

## Exercises

1. Run `python manage.py help` in `projects/hotel_management`.
2. Create a new app called `customers` (you can delete it later).
3. Explain why `manage.py` must be run from the project root.
