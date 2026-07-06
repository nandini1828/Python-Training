# List Comprehension

---

# Learning Objectives

After completing this chapter, you will be able to:

- Build lists using list comprehensions.
- Transform values while iterating.
- Filter values using conditions.
- Flatten simple nested lists.
- Compare list comprehensions with normal loops.
- Avoid unreadable comprehension expressions.

---

# Introduction

List comprehension is used to create a new list from an iterable.

Basic syntax

```python
[expression for item in iterable]
```

Example

```python
numbers = [1, 2, 3]
squares = [number * number for number in numbers]
```

Output

```text
[1, 4, 9]
```

---

# Normal Loop vs List Comprehension

Normal loop:

```python
numbers = [1, 2, 3]
squares = []

for number in numbers:
    squares.append(number * number)
```

List comprehension:

```python
squares = [number * number for number in numbers]
```

Both produce the same result.

The comprehension is shorter because creating a list is the main purpose.

---

# Filtering Values

Add an `if` condition at the end.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
```

Output

```text
[2, 4, 6]
```

The condition controls which values are included.

---

# Transforming Strings

```python
words = ["python", "sql", "git"]
uppercase_words = [word.upper() for word in words]
```

Output

```text
['PYTHON', 'SQL', 'GIT']
```

Transformation happens before the `for` keyword.

---

# Combining Transformation and Filtering

```python
words = ["python", "sql", "git", "javascript"]
short_uppercase = [
    word.upper()
    for word in words
    if len(word) <= 3
]
```

Output

```text
['SQL', 'GIT']
```

This pattern is common in data cleanup.

---

# Flattening a Nested List

```python
matrix = [[1, 2], [3, 4], [5]]
flat = [item for row in matrix for item in row]
```

Output

```text
[1, 2, 3, 4, 5]
```

Read it in loop order:

```python
for row in matrix:
    for item in row:
        ...
```

---

# Real-World Example: Discounted Prices

```python
prices = [1000, 2500, 4000]
discounted = [price * 0.9 for price in prices]
```

Output

```text
[900.0, 2250.0, 3600.0]
```

In real applications, this can be used for invoices, shopping carts, and reports.

---

# Real-World Example: Form Validation

```python
fields = ["name", "", "email", ""]
missing_indexes = [
    index
    for index, value in enumerate(fields)
    if value == ""
]
```

Output

```text
[1, 3]
```

Here the comprehension collects indexes where the input is missing.

---

# Common Mistakes

## Mistake 1: Confusing expression and condition

Correct:

```python
[number for number in numbers if number > 0]
```

Incorrect:

```python
[if number > 0 for number in numbers]
```

## Mistake 2: Using print inside a comprehension

```python
[print(word) for word in words]
```

Use a normal loop for actions.

## Mistake 3: Making the expression too long

If the expression has many method calls or conditions, use a normal loop.

---

# Best Practices

- Use list comprehensions for new lists.
- Keep transformation logic simple.
- Use clear variable names.
- Split long comprehensions across multiple lines.
- Prefer loops when readability suffers.

---

# Summary

List comprehension is one of Python's most useful tools.

It is best used for simple transformations and filters where the goal is to
produce a new list.
