# 05_comprehensions

## What this project is about
This project introduces comprehensions, which are compact ways to create and transform data in Python. They are often shorter than writing a full loop.

## Why this topic matters
Comprehensions help you write cleaner code when you want to:
- build a list from another list
- create a dictionary from values
- keep only certain items

## Topic notes

### 1. List comprehensions
A list comprehension creates a list in one short expression.

```python
squares = [x * x for x in range(5)]
```

It is a compact way to say: “create a list of squares.”

### 2. Dictionary comprehensions
A dictionary comprehension creates a dictionary from a loop-like expression.

```python
square_map = {x: x * x for x in range(5)}
```

This creates keys and values at the same time.

### 3. Set comprehensions
A set comprehension creates a set of unique values.

```python
unique_even = {x for x in range(10) if x % 2 == 0}
```

This is useful when you want to remove duplicates.

### 4. Nested comprehensions
You can also use comprehensions with nested structures such as a matrix.

```python
matrix = [[1, 2], [3, 4]]
flat = [value for row in matrix for value in row]
```

This flattens the nested structure into one list.

## What this project demonstrates
- A shorter way to create lists
- A shorter way to create dictionaries and sets
- How to filter and transform values in one line

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Understand when comprehensions are useful
- Practice writing compact but readable expressions
- Learn how comprehensions compare with normal loops
