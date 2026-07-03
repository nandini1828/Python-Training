# 06_iterators_generators

## What this project is about
This project introduces iterators and generators. These are tools that help Python produce values one at a time instead of creating everything at once.

## Why this topic matters
Generators are useful when you work with large or endless sequences. They save memory because they produce values only when needed.

## Topic notes

### 1. Iterator protocol
An iterator is an object that can be looped over.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
```

`iter()` creates the iterator, and `next()` gets the next value.

### 2. __iter__() and __next__()
These special methods define how an object behaves as an iterator.

```python
class Counter:
    def __iter__(self):
        return self

    def __next__(self):
        return 1
```

This means the object can be used in a loop.

### 3. yield
`yield` turns a function into a generator.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

A generator gives values one by one and pauses between them.

### 4. Generator expressions
A generator expression is a compact way to create a generator.

```python
even_numbers = (x for x in range(10) if x % 2 == 0)
```

It works like a comprehension, but it produces values lazily.

## What this project demonstrates
- How custom iterators work
- How generators produce values step by step
- The difference between a list and a generator

## How to run
From this folder, run:

```bash
python3 main.py
```

## Learning goals
- Understand how iteration works in Python
- Learn the difference between iterators and generators
- Practice writing simple generator-based code
