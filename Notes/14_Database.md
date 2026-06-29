# Django Bootcamp - Class 4

# Chapter 14 - Database Fundamentals

---

# Learning Objectives

After completing this chapter, you will understand:

* What is a Database?
* Why databases are required
* Types of databases
* Tables, Rows and Columns
* Primary Keys
* Relationships
* Why Django uses databases
* Enterprise database concepts

---

# What is a Database?

A Database is an organized collection of data that allows us to:

* Store data
* Retrieve data
* Update data
* Delete data
* Manage large amounts of information efficiently

Without a database, every time the application restarted, all information would be lost.

---

# Why Do We Need a Database?

Imagine building a Student Management System.

We need to store:

* Student Name
* Age
* Email
* Course
* Attendance
* Marks

If we stored this in Python variables:

```python
students = [
    {"name": "Sagar", "age": 22}
]
```

the data would disappear whenever the program stops.

A database stores information permanently.

---

# Real World Examples

Instagram stores:

* Users
* Posts
* Followers
* Likes
* Comments

Amazon stores:

* Products
* Customers
* Orders
* Payments

Netflix stores:

* Movies
* Users
* Watch History

Everything is stored inside databases.

---

# Database Terminology

| Database Term | Similar To     |
| ------------- | -------------- |
| Database      | Excel Workbook |
| Table         | Excel Sheet    |
| Row           | Record         |
| Column        | Field          |

---

# Example Table

Students

| ID | Name  | Age | Course |
| -- | ----- | --- | ------ |
| 1  | Sagar | 22  | Python |
| 2  | Rahul | 21  | Django |
| 3  | Priya | 23  | React  |

---

# What is a Table?

A Table stores similar types of information.

Example:

Student Table

Teacher Table

Course Table

Attendance Table

Each table stores one type of information.

---

# What is a Row?

One complete record.

Example

| ID | Name  | Age |
| -- | ----- | --- |
| 1  | Sagar | 22  |

This complete line is called a Row.

---

# What is a Column?

A column stores one specific property.

Example

Name

Age

Email

Course

Every student has these columns.

---

# Primary Key

Every table should uniquely identify each row.

Example

| ID | Name  |
| -- | ----- |
| 1  | Sagar |
| 2  | Rahul |

ID is the Primary Key.

In Django,

every model automatically gets:

```python
id
```

unless you define another primary key.

---

# Relationships

Real-world data is connected.

Example

Student

↓

Course

↓

Teacher

A Student belongs to a Course.

A Course belongs to a Teacher.

Databases represent these relationships efficiently.

---

# Types of Databases

## SQLite

* Lightweight
* File-based
* Default in Django
* Best for learning

---

## PostgreSQL

* Enterprise-grade
* Open source
* Fast
* Reliable
* Recommended for Django production projects

---

## MySQL

* Popular
* Easy to use
* Common for websites

---

## Oracle

* Banking
* Government
* Large enterprises

---

## MongoDB

* NoSQL Database
* Stores JSON-like documents
* Good for flexible schemas

---

# SQL vs NoSQL

| SQL          | NoSQL           |
| ------------ | --------------- |
| Tables       | Documents       |
| Fixed Schema | Flexible Schema |
| Structured   | Semi-Structured |
| PostgreSQL   | MongoDB         |
| SQLite       | CouchDB         |

---

# Why Django Uses Databases

Django applications usually manage large amounts of structured data.

Examples:

Students

Teachers

Products

Orders

Invoices

Databases make these operations efficient and reliable.

---

# Enterprise Architecture

Frontend

↓

Django Views / APIs

↓

Django ORM

↓

Database

Users never communicate directly with the database.

---

# Common Beginner Mistakes

❌ Thinking a database is only an Excel sheet

❌ Forgetting that data persists after restarting the application

❌ Confusing tables with databases

❌ Thinking Python variables are permanent storage

---

# Best Practices

* Store structured data in databases.
* Use meaningful table names.
* Keep related data in separate tables.
* Always use primary keys.
* Avoid duplicate data.

---

# Summary

You learned:

* What a database is
* Why databases are required
* Tables, rows, and columns
* Primary keys
* Database types
* SQL vs NoSQL
* Why Django uses databases

---

# Interview Questions

1. What is a database?
2. Why do applications use databases?
3. Difference between a table and a database?
4. What is a row?
5. What is a column?
6. What is a primary key?
7. SQL vs NoSQL?
8. Which database does Django use by default?
9. Why is PostgreSQL recommended for production?
10. Why are relationships important?
