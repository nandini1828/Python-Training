# Set Comprehension

---

# Learning Objectives

After completing this chapter, you will be able to:

- Build sets using comprehension syntax.
- Use set comprehensions for uniqueness.
- Filter values while creating sets.
- Extract unique characters or tags.
- Understand why output order is not guaranteed.
- Avoid confusing set comprehensions with dictionary comprehensions.

---

# Introduction

Set comprehensions create sets from iterable data.

Basic syntax

```python
{expression for item in iterable}
```

Example

```python
numbers = [1, 2, 2, 3]
squares = {number * number for number in numbers}
```

Output

```text
{1, 4, 9}
```

Duplicate results are automatically removed.

---

# Why Use Set Comprehensions?

Use set comprehensions when uniqueness matters.

Example

```python
words = ["Python", "python", "SQL"]
normalized = {word.lower() for word in words}
```

Output

```text
{'python', 'sql'}
```

The two Python spellings become one value after normalization.

---

# Filtering Values

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = {number for number in numbers if number % 2 == 0}
```

Output

```text
{2, 4, 6}
```

---

# Extracting Unique Characters

```python
words = ["hello", "world"]
characters = {char for word in words for char in word}
```

Possible result

```python
{'h', 'e', 'l', 'o', 'w', 'r', 'd'}
```

The order is not important. The uniqueness is important.

---

# Set Comprehension vs List Comprehension

List comprehension:

```python
[word.lower() for word in words]
```

Set comprehension:

```python
{word.lower() for word in words}
```

The list keeps duplicates and order.

The set removes duplicates and does not preserve meaningful output order.

---

# Real-World Example: Unique Tags

```python
posts = [
    {"tags": ["python", "beginner"]},
    {"tags": ["python", "testing"]},
    {"tags": ["automation"]},
]

all_tags = {
    tag
    for post in posts
    for tag in post["tags"]
}
```

Result

```python
{"python", "beginner", "testing", "automation"}
```

This is common in blogs, product filters, dashboards, and search systems.

---

# Real-World Example: Shared Letters

```python
first = "iteration"
second = "generator"

common = {char for char in first if char in second}
```

This finds unique characters that appear in both strings.

---

# Common Mistakes

## Mistake 1: Expecting order

```python
result = {3, 1, 2}
```

Do not assume it displays as `{1, 2, 3}`.

Use `sorted(result)` for ordered output.

## Mistake 2: Creating a dictionary accidentally

```python
{}
```

This is an empty dictionary, not an empty set.

Use:

```python
set()
```

## Mistake 3: Forgetting uniqueness

If duplicates matter, use a list comprehension instead of a set comprehension.

---

# Best Practices

- Use set comprehensions when duplicates should be removed.
- Sort the result before displaying it if order matters.
- Use meaningful expression names.
- Avoid set comprehensions when duplicate counts are important.
- Remember that `{key: value ...}` is a dictionary comprehension.

---

# Summary

Set comprehensions are ideal for unique transformed values.

They are especially useful for tags, permissions, categories, and membership
checks where order is less important than uniqueness.
