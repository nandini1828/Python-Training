# For Loop

## Overview

A `for` loop is one of Python's most commonly used control flow statements. It allows you to iterate over the elements of an iterable object such as lists, tuples, dictionaries, sets, strings, ranges, generators, and files.

Unlike many programming languages, Python's `for` loop does **not** rely on an index variable. Instead, it directly retrieves elements from an iterable using the **iterator protocol**.

The `for` loop is simple, readable, and highly efficient, making it the preferred choice whenever the number of iterations is known or when traversing a collection.

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the purpose of a `for` loop.
- Iterate over different iterable objects.
- Use `range()` effectively.
- Iterate using indices.
- Iterate over dictionaries.
- Iterate over strings.
- Write nested loops.
- Apply `for` loops to real-world scenarios.

---

# Prerequisites

- Variables
- Data Types
- Collections
- Conditional Statements

---

# Folder Structure

```text
for_loop/
│
├── README.md
├── demo.py
├── utils.py
└── __init__.py
```

---

# Syntax

```python
for variable in iterable:
    # code block
```

---

# Execution Flow

```text
           Iterable
               │
               ▼
      Get Next Element
               │
               ▼
      Execute Loop Body
               │
               ▼
     More Elements?
        │      │
       Yes     No
        │       │
        └──────►End
```

---

# Examples

## Iterate over a List

```python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```

---

## Iterate over a String

```python
for character in "Python":
    print(character)
```

---

## Iterate using range()

```python
for number in range(5):
    print(number)
```

Output

```
0
1
2
3
4
```

---

## Iterate over Dictionary

```python
student = {
    "name": "Ganesh",
    "age": 22
}

for key, value in student.items():
    print(key, value)
```

---

## Nested Loop

```python
for row in range(3):
    for column in range(3):
        print(row, column)
```

---

# Enterprise Applications

- Reading CSV files
- Processing database records
- Sending emails
- Data migration
- Report generation
- Batch processing
- Machine Learning datasets
- Log analysis

---

# Advantages

- Simple syntax
- Highly readable
- Works with every iterable
- Less error-prone than index-based loops
- Efficient

---

# Best Practices

✔ Prefer direct iteration over indexing.

✔ Use meaningful variable names.

✔ Keep loop bodies small.

✔ Avoid unnecessary nesting.

✔ Use helper functions for complex logic.

---

# Common Mistakes

❌ Modifying a collection while iterating.

❌ Using indices unnecessarily.

❌ Deeply nested loops.

❌ Writing duplicate code inside loops.

---

# Interview Questions

1. What is an iterable?
2. How does Python's `for` loop work internally?
3. Difference between `for` and `while`.
4. Can dictionaries be iterated?
5. Can sets be iterated?
6. What is the iterator protocol?

---

# Practice Exercises

1. Print numbers from 1 to 100.
2. Find the sum of a list.
3. Count vowels in a string.
4. Print multiplication tables.
5. Reverse a string using a loop.
6. Find the maximum element in a list.

---

# Summary

The `for` loop is the primary iteration mechanism in Python. It is concise, efficient, and widely used in both beginner and enterprise-level Python applications for traversing collections and automating repetitive tasks.