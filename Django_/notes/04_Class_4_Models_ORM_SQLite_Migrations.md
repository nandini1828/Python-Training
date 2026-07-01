# Class 4: Models, ORM, SQLite, and Migrations

## Learning Objectives

After this class, you will understand:

- What models are in Django
- How Django ORM maps Python classes to database tables
- Why SQLite is a good default database for learning
- How migrations work
- How to create and apply migrations

## What is a Model?

A model is a Python class that defines the structure of a database table.
Each model field becomes a column.

Example:

```python
from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
```

## Django ORM

ORM stands for Object-Relational Mapping.
Django ORM lets you work with database records using Python code.

Example:

```python
Room.objects.create(room_number='101', room_type='single', price=100.00)
rooms = Room.objects.filter(is_available=True)
```

## Why SQLite?

SQLite is a lightweight database that stores data in a file.
It is perfect for learning because it requires no extra setup.

The default Django database configuration is usually:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Migrations

Migrations are Django’s way of tracking changes to models.
Whenever you change a model, you create a migration file.

Create migration files:

```bash
python manage.py makemigrations
```

Apply migrations to the database:

```bash
python manage.py migrate
```

## How it works

1. Write or change a model.
2. Run `makemigrations`.
3. Django creates migration files.
4. Run `migrate`.
5. Django updates the database schema.

## Common Files

- `models.py` — define data models
- `migrations/` — stores migration files
- `db.sqlite3` — database file created after migrations

## Summary

This class covered:

- Django models
- the ORM
- SQLite
- migrations

## Interview Questions

1. What is a Django model?
2. What is an ORM?
3. Why do we use migrations?
4. Why is SQLite useful for learning?

## Exercises

1. Add a model `Guest` with name and email fields.
2. Run `makemigrations` and `migrate`.
3. Create a `Room` record using the Django shell.
