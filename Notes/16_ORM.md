# Django Bootcamp - Class 4

# Chapter 16 - Django ORM (Object Relational Mapper)

---

# Learning Objectives

After completing this chapter, you will understand:

* What is an ORM?
* Why Django uses an ORM
* How ORM works internally
* ORM vs SQL
* CRUD operations using ORM
* QuerySets
* Manager (`objects`)
* Advantages and disadvantages of ORM
* Enterprise best practices

---

# What is ORM?

ORM stands for **Object Relational Mapper**.

It is a technology that allows Python objects to communicate with relational databases **without writing SQL manually**.

Simple definition:

```text
Python Objects

↓

Django ORM

↓

SQL Queries

↓

Database
```

---

# Why Do We Need an ORM?

Without an ORM, you would write SQL directly.

Example

```sql
SELECT * FROM students_student;
```

With Django ORM

```python
Student.objects.all()
```

Same result.

Much easier.

---

# ORM Analogy

Imagine you speak only English.

The database understands only SQL.

ORM acts as a translator.

```text
Python

↓

Translator (ORM)

↓

SQL

↓

Database
```

---

# ORM Internals

When you write

```python
Student.objects.all()
```

Django internally generates SQL similar to:

```sql
SELECT * FROM students_student;
```

You never write SQL yourself.

---

# CRUD with ORM

## Create

```python
Student.objects.create(
    first_name="Sagar",
    last_name="Nunugonda",
    age=22,
    email="sagar@example.com",
    course="Python"
)
```

---

## Read

Fetch all students

```python
Student.objects.all()
```

Fetch one student

```python
Student.objects.get(id=1)
```

Filter students

```python
Student.objects.filter(course="Python")
```

---

## Update

```python
student = Student.objects.get(id=1)

student.age = 23

student.save()
```

---

## Delete

```python
student = Student.objects.get(id=1)

student.delete()
```

---

# Understanding `objects`

Every model automatically gets a Manager called:

```python
Student.objects
```

The Manager is responsible for communicating with the database.

Example

```python
Student.objects.create(...)
Student.objects.filter(...)
Student.objects.get(...)
Student.objects.all()
```

Think of `objects` as the **gateway** to the database.

---

# What is a QuerySet?

A QuerySet is a collection of objects returned from the database.

Example

```python
students = Student.objects.all()
```

`students` is **not** a list.

It is a **QuerySet**.

---

# QuerySet Example

```python
students = Student.objects.filter(age__gte=18)
```

This returns all students whose age is greater than or equal to 18.

---

# QuerySet is Lazy

This is an important Django concept.

When you write:

```python
students = Student.objects.all()
```

Django does **not** immediately query the database.

The query is executed only when the data is needed.

Example

```python
for student in students:
    print(student.first_name)
```

At this point, Django executes the SQL.

This behavior is called **Lazy Evaluation**.

---

# Common ORM Methods

| Method   | Purpose              |
| -------- | -------------------- |
| all()    | Fetch all records    |
| get()    | Fetch one record     |
| filter() | Filter records       |
| create() | Create a record      |
| update() | Update records       |
| delete() | Delete records       |
| exists() | Check if data exists |
| count()  | Count records        |
| first()  | First record         |
| last()   | Last record          |

---

# ORM Execution Flow

```text
Developer

↓

Student.objects.filter(...)

↓

ORM

↓

SQL Generated

↓

SQLite

↓

Results Returned

↓

Python Objects
```

---

# Advantages of ORM

✅ No SQL required

✅ Safer (helps prevent SQL injection)

✅ Database independent

✅ Easier to read

✅ Easier to maintain

✅ Portable between databases

---

# Disadvantages

* Very complex queries may require raw SQL.
* Understanding generated SQL is still useful.
* Performance tuning may be needed for large applications.

---

# Enterprise Best Practices

* Prefer ORM over raw SQL.
* Use `filter()` instead of `get()` unless exactly one object is expected.
* Avoid unnecessary queries.
* Learn lazy evaluation.
* Use indexes for frequently searched fields.

---

# Common Beginner Mistakes

❌ Thinking `objects` is a Python list

❌ Confusing QuerySet with List

❌ Forgetting `.save()` after updating an object

❌ Assuming queries execute immediately

---

# Summary

You learned:

* What ORM is
* ORM vs SQL
* CRUD using ORM
* Managers
* QuerySets
* Lazy Evaluation
* Common ORM methods

---

# Interview Questions

1. What is ORM?
2. Why does Django use ORM?
3. What is a QuerySet?
4. What is `objects`?
5. Difference between `get()` and `filter()`?
6. What is Lazy Evaluation?
7. Advantages of ORM?
8. When would you use raw SQL?
