# Django Bootcamp - Class 4

# Chapter 19 - SQLite

---

# Learning Objectives

After completing this chapter, you will understand:

* What is SQLite?
* Why Django uses SQLite by default
* Advantages and limitations
* The `db.sqlite3` file
* SQLite vs PostgreSQL
* When to switch databases
* Enterprise recommendations

---

# What is SQLite?

SQLite is a lightweight relational database.

Unlike PostgreSQL or MySQL,

SQLite stores the entire database in a **single file**.

In Django, that file is:

```text
db.sqlite3
```

---

# Where is the Database Stored?

Project Structure

```text
student_management/

manage.py

config/

students/

db.sqlite3
```

The entire database lives inside this single file.

---

# How Django Uses SQLite

When you create a Django project,

`settings.py` already contains:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

No installation is required.

---

# How Data is Stored

Suppose you create this model:

```python
class Student(models.Model):

    first_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()
```

After migrations,

SQLite creates a table similar to:

```text
students_student

-----------------------

id

first_name

age
```

---

# Advantages of SQLite

✅ Built into Python

✅ No installation

✅ Lightweight

✅ Fast for development

✅ Easy to back up (copy one file)

✅ Perfect for learning Django

---

# Limitations of SQLite

* Not designed for heavy concurrent writes
* Limited scalability
* Fewer advanced database features
* Not recommended for high-traffic production systems

---

# SQLite vs PostgreSQL

| SQLite          | PostgreSQL            |
| --------------- | --------------------- |
| File-based      | Server-based          |
| No setup        | Requires installation |
| Lightweight     | Enterprise-grade      |
| Development     | Production            |
| Simple projects | Large applications    |

---

# When Should You Use SQLite?

Use SQLite for:

* Learning Django
* Personal projects
* Small internal tools
* Rapid prototyping
* Development

---

# When Should You Use PostgreSQL?

Use PostgreSQL for:

* Production applications
* Large teams
* Enterprise software
* High traffic APIs
* Financial systems
* Healthcare systems

---

# Enterprise Workflow

During development

```text
Developer

↓

SQLite

↓

Fast development
```

Before deployment

```text
SQLite

↓

PostgreSQL

↓

Production
```

Most Django teams follow this workflow.

---

# Backing Up SQLite

Since the database is just one file,

backup is simple.

Copy:

```text
db.sqlite3
```

to another location.

---

# Viewing SQLite Data

You can inspect SQLite using:

* DB Browser for SQLite
* VS Code SQLite extensions
* Python's sqlite3 module

This helps visualize tables and records.

---

# Common Beginner Mistakes

❌ Deleting `db.sqlite3` accidentally

❌ Editing the database manually without understanding the impact

❌ Thinking SQLite is suitable for every production system

❌ Forgetting that deleting `db.sqlite3` removes all stored data

---

# Enterprise Best Practices

* Use SQLite during development.
* Use PostgreSQL in production.
* Keep regular backups.
* Never commit sensitive production databases to Git.
* Run migrations instead of modifying tables manually.

---

# Summary

You learned:

* What SQLite is
* Why Django uses it
* Advantages and limitations
* SQLite vs PostgreSQL
* When to use each database
* Enterprise recommendations

---

# Interview Questions

1. What is SQLite?
2. Why does Django use SQLite by default?
3. Where is the SQLite database stored?
4. What are the advantages of SQLite?
5. What are its limitations?
6. Difference between SQLite and PostgreSQL?
7. Why do most production Django applications use PostgreSQL?
8. How do you back up an SQLite database?
