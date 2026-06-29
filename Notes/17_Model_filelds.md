# Django Bootcamp - Class 4

# Chapter 17 - Django Model Fields

---

# Learning Objectives

After completing this chapter, you will understand:

* What are Model Fields?
* Common Django field types
* Field options
* Choosing the correct field
* Field validation
* Enterprise best practices

---

# What is a Model Field?

Every attribute inside a Django Model becomes a **column** in the database.

Example

```python
class Student(models.Model):

    first_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()
```

Database Table

| id | first_name | age |
| -- | ---------- | --- |

---

# How Fields Become Columns

```text
Python Field

↓

Migration

↓

Database Column
```

---

# CharField

Stores short text.

Example

```python
first_name = models.CharField(max_length=100)
```

Used for:

* Names
* Cities
* Courses
* Departments

---

# TextField

Stores long text.

Example

```python
description = models.TextField()
```

Used for:

* Blog content
* Notes
* Comments
* Descriptions

---

# IntegerField

Stores integers.

```python
marks = models.IntegerField()
```

---

# PositiveIntegerField

Stores only positive numbers.

```python
age = models.PositiveIntegerField()
```

---

# FloatField

Stores decimal numbers.

```python
price = models.FloatField()
```

---

# DecimalField

Recommended for money.

```python
salary = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

Why?

Float values can lose precision.

---

# BooleanField

Stores True or False.

```python
is_active = models.BooleanField(default=True)
```

---

# EmailField

Stores emails.

```python
email = models.EmailField(unique=True)
```

Provides email validation.

---

# URLField

Stores website URLs.

```python
website = models.URLField()
```

---

# DateField

Stores dates.

```python
birth_date = models.DateField()
```

---

# DateTimeField

Stores date and time.

```python
created_at = models.DateTimeField(auto_now_add=True)
```

---

# TimeField

Stores time only.

```python
start_time = models.TimeField()
```

---

# FileField

Stores uploaded files.

```python
resume = models.FileField(upload_to="resumes/")
```

---

# ImageField

Stores images.

```python
profile_photo = models.ImageField(
    upload_to="photos/"
)
```

Requires the Pillow library.

---

# JSONField

Stores JSON data.

```python
preferences = models.JSONField()
```

Useful for dynamic configurations.

---

# UUIDField

Stores universally unique identifiers.

```python
import uuid

id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)
```

Often used in enterprise APIs instead of integer IDs.

---

# Common Field Options

## max_length

Maximum number of characters.

```python
models.CharField(max_length=100)
```

---

## default

Default value.

```python
is_active = models.BooleanField(default=True)
```

---

## null

Allows NULL in the database.

```python
phone = models.CharField(
    max_length=15,
    null=True
)
```

---

## blank

Allows empty values in forms.

```python
phone = models.CharField(
    max_length=15,
    blank=True
)
```

---

## unique

Prevents duplicate values.

```python
email = models.EmailField(unique=True)
```

---

## db_index

Creates a database index.

```python
email = models.EmailField(
    db_index=True
)
```

Useful for frequently searched fields.

---

## auto_now_add

Automatically sets creation time.

```python
created_at = models.DateTimeField(
    auto_now_add=True
)
```

---

## auto_now

Automatically updates on every save.

```python
updated_at = models.DateTimeField(
    auto_now=True
)
```

---

# Choosing the Right Field

| Requirement   | Field                |
| ------------- | -------------------- |
| Name          | CharField            |
| Description   | TextField            |
| Age           | PositiveIntegerField |
| Salary        | DecimalField         |
| Email         | EmailField           |
| Website       | URLField             |
| Active Status | BooleanField         |
| Date of Birth | DateField            |
| Timestamp     | DateTimeField        |
| Image         | ImageField           |

---

# Enterprise Best Practices

* Use `EmailField` instead of `CharField` for emails.
* Use `DecimalField` for financial values.
* Use `PositiveIntegerField` where negative values are invalid.
* Add `db_index=True` for frequently queried columns.
* Use meaningful field names.
* Avoid unnecessary `null=True` on string fields.

---

# Common Beginner Mistakes

❌ Using `CharField` for everything

❌ Forgetting `max_length`

❌ Using `FloatField` for money

❌ Confusing `null` and `blank`

❌ Forgetting `unique=True` where required

---

# Summary

You learned:

* What Model Fields are
* Common field types
* Field options
* Validation
* Best practices for designing models

---

# Interview Questions

1. What is a Model Field?
2. Difference between `CharField` and `TextField`?
3. Why use `DecimalField` instead of `FloatField`?
4. Difference between `null` and `blank`?
5. What does `unique=True` do?
6. Difference between `auto_now` and `auto_now_add`?
7. When would you use `UUIDField`?
8. Why should frequently searched fields use `db_index=True`?
