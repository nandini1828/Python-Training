# Django Bootcamp - Class 4

# Chapter 18 - Migrations

---

# Learning Objectives

After completing this chapter, you will understand:

* What are Migrations?
* Why Migrations are required
* Migration workflow
* Difference between `makemigrations` and `migrate`
* Migration files
* Django migration internals
* Enterprise migration practices

---

# What are Migrations?

A Migration is a Python file that records changes made to your Django Models.

Think of it as a **version history for your database schema**.

Whenever you modify a Model, Django needs to know how to update the database.

Instead of modifying the database directly, Django creates a migration file.

---

# Why Do We Need Migrations?

Imagine you have this model:

```python
class Student(models.Model):
    first_name = models.CharField(max_length=100)
```

Later, you add:

```python
email = models.EmailField(unique=True)
```

Your Python code changed.

But your database table still has only:

```text
id
first_name
```

The database doesn't know about the new `email` field.

Migrations tell Django how to update the database.

---

# Migration Workflow

```text
Modify Model

↓

python manage.py makemigrations

↓

Migration File Created

↓

python manage.py migrate

↓

Database Updated
```

---

# Step 1 - Modify the Model

Example

```python
class Student(models.Model):

    first_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()
```

---

# Step 2 - Create Migration

Command

```bash
python manage.py makemigrations
```

Output

```text
Migrations for 'students':
    students/migrations/0001_initial.py
```

This file contains instructions for creating the database table.

---

# Step 3 - Apply Migration

Command

```bash
python manage.py migrate
```

Output

```text
Applying students.0001_initial... OK
```

Now the database is updated.

---

# What Does `makemigrations` Do?

It compares:

* Current Models
* Previous Migrations

If differences exist,

it creates a new migration file.

It **does not** modify the database.

---

# What Does `migrate` Do?

Reads migration files.

Generates SQL.

Executes SQL against the database.

Updates the database schema.

---

# Migration Folder

Every app has a migrations folder.

```text
students/

migrations/

    __init__.py

    0001_initial.py

    0002_add_email.py

    0003_update_course.py
```

Each file represents one database change.

---

# Migration Naming

Typical migration names

```text
0001_initial.py

0002_add_email.py

0003_remove_phone.py

0004_alter_age.py
```

Numbers show the migration order.

---

# Migration File Example

```python
operations = [
    migrations.CreateModel(
        name="Student",
        fields=[
            ...
        ],
    ),
]
```

Django generates this automatically.

You usually don't edit migration files manually.

---

# Internal Working

```text
Developer

↓

Modify Model

↓

makemigrations

↓

Migration File

↓

migrate

↓

SQL Generated

↓

SQLite / PostgreSQL

↓

Database Updated
```

---

# Common Migration Commands

Create migration

```bash
python manage.py makemigrations
```

Apply migrations

```bash
python manage.py migrate
```

Show migration status

```bash
python manage.py showmigrations
```

Display SQL generated

```bash
python manage.py sqlmigrate students 0001
```

---

# Common Beginner Mistakes

❌ Forgetting `makemigrations`

❌ Forgetting `migrate`

❌ Editing migration files manually

❌ Deleting migration files without understanding the consequences

❌ Deleting the database while keeping old migrations

---

# Enterprise Best Practices

* Commit migration files to Git.
* Never edit applied migration files.
* Review migrations before deploying.
* Run migrations in staging before production.
* Keep migrations small and focused.

---

# Summary

You learned:

* What migrations are
* Why they are required
* Migration workflow
* `makemigrations` vs `migrate`
* Migration folder
* Enterprise migration practices

---

# Interview Questions

1. What is a migration?
2. Why are migrations needed?
3. Difference between `makemigrations` and `migrate`?
4. What does `showmigrations` do?
5. Why shouldn't you edit migration files manually?
6. What happens if you modify a Model but don't run migrations?
7. Where are migration files stored?
8. Are migration files committed to Git?
