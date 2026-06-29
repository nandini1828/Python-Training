# Django Bootcamp - Class 4

# Chapter 15 - Django Models

---

# Learning Objectives

After completing this chapter, you will understand:

* What is a Model?
* Why Models exist
* Model to Table mapping
* Model lifecycle
* Why Django uses Models
* Enterprise Model design

---

# What is a Model?

A Model is a Python class that represents a database table.

Instead of writing SQL manually,

we define Python classes.

Django automatically creates the database table.

---

# Simple Definition

Python Class

↓

Database Table

---

# Example

```python
from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()
```

Automatically becomes

Student Table

| id | first_name | age |
| -- | ---------- | --- |
| 1  | Sagar      | 22  |

---

# Why Models?

Without Django

You write SQL

```sql
CREATE TABLE student(
    id INTEGER,
    first_name VARCHAR(100)
);
```

With Django

```python
class Student(models.Model):
```

Django writes SQL automatically.

---

# Every Model Represents One Table

Examples

Student Model

↓

Student Table

Teacher Model

↓

Teacher Table

Course Model

↓

Course Table

Attendance Model

↓

Attendance Table

---

# Understanding models.Model

```python
class Student(models.Model):
```

Every Django model must inherit from

```python
models.Model
```

This gives the class powerful database features.

---

# Model Fields

Each field becomes a database column.

Example

```python
first_name = models.CharField(max_length=100)
```

Database

| first_name |

---

```python
age = models.PositiveIntegerField()
```

Database

| age |

---

```python
email = models.EmailField(unique=True)
```

Database

| email |

---

# Automatic ID Field

If you don't create an ID,

Django creates

```python
id
```

automatically.

This becomes the Primary Key.

---

# **str**()

Example

Without

```
Student object (1)
```

With

```
Sagar Nunugonda
```

```python
def __str__(self):
    return f"{self.first_name} {self.last_name}"
```

Always implement `__str__()`.

---

# Model Lifecycle

Write Model

↓

Create Migration

↓

Apply Migration

↓

Database Table Created

↓

Insert Data

↓

Retrieve Data

↓

Update Data

↓

Delete Data

---

# Real World Example

Instagram

User Model

↓

users table

Post Model

↓

posts table

Comment Model

↓

comments table

Like Model

↓

likes table

Everything begins with Models.

---

# Why Models Are Powerful

* No SQL required
* Automatic validation
* Database abstraction
* Easy maintenance
* Database portability

---

# Enterprise Best Practices

One model = One responsibility.

Use meaningful names.

Always implement `__str__()`.

Use appropriate field types.

Keep models clean.

Business logic should be minimal in models unless it directly belongs to the data.

---

# Common Beginner Mistakes

❌ Forgetting to inherit from `models.Model`

❌ Using wrong field types

❌ Forgetting `max_length`

❌ Forgetting `__str__()`

❌ Mixing unrelated data into one model

---

# Model Naming Convention

Good

Student

Teacher

Course

Attendance

Bad

StudentTable

StudentData

student123

---

# Summary

You learned:

* What a Model is
* Model to Table mapping
* Model lifecycle
* Automatic ID field
* Why `models.Model` is important
* Importance of `__str__()`

---

# Interview Questions

1. What is a Django Model?
2. How is a Model related to a database table?
3. Why do Models inherit from `models.Model`?
4. What happens if you don't define an ID field?
5. Why should every model implement `__str__()`?
6. What is the lifecycle of a Django Model?
7. Why are Models important in Django?
8. What are some best practices when designing Models?
