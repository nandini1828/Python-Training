# List Iteration

---

# Learning Objectives

After completing this chapter, you will be able to:

- Iterate over list values directly.
- Use `enumerate` when indexes are required.
- Search, filter, transform, and summarize list data.
- Understand why list order matters.
- Avoid unnecessary index-based loops.

---

# Introduction

A list is an ordered collection of values.

Because lists preserve order, iteration happens from the first element to the
last element.

Example

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Output

```text
10
20
30
```

---

# Basic List Iteration

Syntax

```python
for item in list_name:
    statements
```

Example

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit.upper())
```

Output

```text
APPLE
BANANA
CHERRY
```

The variable `fruit` receives one list item during each loop cycle.

---

# Iteration Flow

```text
fruits = ["apple", "banana", "cherry"]

        Start
          |
          v
      fruit = apple
          |
          v
      print apple
          |
          v
      fruit = banana
          |
          v
      print banana
          |
          v
      fruit = cherry
          |
          v
      print cherry
          |
          v
         End
```

---

# Using enumerate

Use `enumerate` when both index and value are needed.

```python
students = ["Asha", "Ravi", "Mira"]

for index, student in enumerate(students):
    print(index, student)
```

Output

```text
0 Asha
1 Ravi
2 Mira
```

Custom start value:

```python
for roll_number, student in enumerate(students, start=1):
    print(roll_number, student)
```

Output

```text
1 Asha
2 Ravi
3 Mira
```

---

# Filtering a List

Filtering means keeping only values that satisfy a condition.

```python
numbers = [-2, -1, 0, 1, 2, 3]
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)

print(positive)
```

Output

```text
[1, 2, 3]
```

---

# Transforming a List

Transformation means creating a new value from each item.

```python
words = ["python", "sql", "git"]
uppercase_words = []

for word in words:
    uppercase_words.append(word.upper())

print(uppercase_words)
```

Output

```text
['PYTHON', 'SQL', 'GIT']
```

---

# Finding Indexes

Sometimes the same value appears multiple times.

```python
values = ["a", "b", "a", "c", "a"]
target = "a"
indexes = []

for index, value in enumerate(values):
    if value == target:
        indexes.append(index)

print(indexes)
```

Output

```text
[0, 2, 4]
```

---

# Real-World Example: Billing Total

```python
cart_prices = [1200, 700, 9000]
total = 0

for price in cart_prices:
    total += price

print(total)
```

Output

```text
10900
```

This pattern appears in billing systems, reports, dashboards, and analytics.

---

# Common Mistakes

## Mistake 1: Using range when direct iteration is enough

Avoid:

```python
for index in range(len(names)):
    print(names[index])
```

Prefer:

```python
for name in names:
    print(name)
```

## Mistake 2: Ignoring empty lists

```python
values = []

for value in values:
    print(value)
```

This loop runs zero times. That is normal behavior.

## Mistake 3: Mixing index and value names

Use meaningful names.

```python
for index, product in enumerate(products):
    print(index, product)
```

---

# Best Practices

- Use direct iteration when only values are needed.
- Use `enumerate` when indexes are needed.
- Build a new list for filtered or transformed values.
- Use clear variable names.
- Keep loop bodies small.
- Write helper functions for repeated list processing.

---

# Summary

List iteration is predictable because lists are ordered.

Use simple `for` loops for values, `enumerate` for index/value pairs, and helper
functions when the logic should be reused or tested.
