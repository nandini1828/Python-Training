# Chapter 5: Introduction to Comprehensions

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what comprehensions are.
- Convert simple loops into comprehensions.
- Choose between list, dictionary, and set comprehensions.
- Use conditions inside comprehensions.
- Understand when comprehensions improve readability.
- Recognize when a normal loop is a better choice.

---

# Introduction

Python programs often build one collection from another collection.

Examples:

- Convert prices into discounted prices.
- Extract usernames from user records.
- Keep only active accounts.
- Create a dictionary lookup from a list of objects.
- Remove duplicate tags from user input.

These tasks can be written with normal loops.

Python also provides a compact syntax called **comprehension**.

---

# What is a Comprehension?

A comprehension is an expression that creates a new collection by iterating over
an existing iterable.

Basic idea:

```text
new collection = transformed values from old collection
```

Example loop:

```python
numbers = [1, 2, 3]
squares = []

for number in numbers:
    squares.append(number * number)
```

Equivalent list comprehension:

```python
squares = [number * number for number in numbers]
```

Output

```text
[1, 4, 9]
```

---

# Types of Comprehensions

Python supports multiple comprehension forms.

| Type | Syntax | Output |
|---|---|---|
| List comprehension | `[expr for item in iterable]` | List |
| Dictionary comprehension | `{key: value for item in iterable}` | Dictionary |
| Set comprehension | `{expr for item in iterable}` | Set |
| Generator expression | `(expr for item in iterable)` | Lazy iterator |

This module focuses on list, dictionary, set, and nested comprehensions.

Generator expressions are covered in the next module.

---

# Why Comprehensions Exist

Comprehensions make common collection-building tasks shorter and clearer.

Loop version:

```python
words = ["python", "sql", "git"]
lengths = []

for word in words:
    lengths.append(len(word))
```

Comprehension version:

```python
lengths = [len(word) for word in words]
```

Both are correct.

The comprehension is preferred when the transformation is simple.

---

# Adding Conditions

Comprehensions can include filtering conditions.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
```

Output

```text
[2, 4, 6]
```

The condition decides which values are included.

---

# Comprehension Flow

```text
Input Iterable
      |
      v
Take one item
      |
      v
Check condition, if any
      |
      v
Transform item
      |
      v
Add to new collection
      |
      v
Repeat until done
```

---

# Real-World Example: Usernames

```python
users = [
    {"name": "Asha", "active": True},
    {"name": "Ravi", "active": False},
    {"name": "Mira", "active": True},
]

active_names = [
    user["name"]
    for user in users
    if user["active"]
]

print(active_names)
```

Output

```text
['Asha', 'Mira']
```

This is common in APIs, dashboards, reports, and data cleaning.

---

# When Comprehensions Are Good

Use comprehensions when:

- You are building a new collection.
- The transformation is short.
- The condition is easy to understand.
- There are no side effects.
- The expression fits naturally on one or a few readable lines.

---

# When to Avoid Comprehensions

Avoid comprehensions when:

- The logic needs several steps.
- You need `try`/`except` inside the loop.
- You are mutating external state.
- The comprehension becomes hard to read.
- You need many nested conditions.

Poor example:

```python
result = [x.process().clean().save() for x in items if x and x.ready()]
```

A normal loop may be clearer.

---

# Common Mistakes

## Mistake 1: Using comprehensions only for side effects

Avoid:

```python
[print(name) for name in names]
```

Use:

```python
for name in names:
    print(name)
```

## Mistake 2: Making expressions too complex

If you need to pause and decode the comprehension, it may be too dense.

## Mistake 3: Forgetting the output type

```python
{number for number in numbers}
```

This creates a set, not a dictionary.

---

# Best Practices

- Use comprehensions to create collections, not to perform actions.
- Keep expressions short.
- Use clear variable names.
- Prefer normal loops for complex logic.
- Split long comprehensions across multiple lines.
- Test helper functions that contain comprehensions.

---

# Summary

Comprehensions are a powerful Python feature for building collections.

They are best when they make code more readable, not merely shorter. A good
comprehension clearly shows the source data, the transformation, and the filter.
