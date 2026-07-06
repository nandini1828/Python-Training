# Chapter 6: Introduction to Iterators and Generators

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what iterable objects are.
- Understand what iterator objects are.
- Explain how Python's `for` loop works internally.
- Understand lazy evaluation.
- Use generator functions to produce values one at a time.
- Understand why generators save memory.
- Recognize when iterators and generators are useful in real programs.

---

# Introduction

Python programs often work with many values.

Examples:

- Lines in a file
- Rows from a database
- API results
- Numbers in a sequence
- Events from a log stream
- Search results

Sometimes it is wasteful to load everything into memory at once.

Python solves this with **iterators** and **generators**.

They allow programs to produce values one at a time.

---

# Iterable vs Iterator

An **iterable** is an object that can be looped over.

Examples:

- List
- Tuple
- String
- Dictionary
- Set
- File object

An **iterator** is the object that actually produces the next value.

```python
values = [10, 20, 30]
iterator = iter(values)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output

```text
10
20
30
```

---

# How a for Loop Works

When Python sees this:

```python
for value in values:
    print(value)
```

It behaves roughly like this:

```python
iterator = iter(values)

while True:
    try:
        value = next(iterator)
    except StopIteration:
        break

    print(value)
```

The `for` loop hides the `iter`, `next`, and `StopIteration` details.

---

# Execution Flow

```text
Iterable object
      |
      v
iter(iterable)
      |
      v
Iterator object
      |
      v
next(iterator)
      |
      v
Value produced
      |
      v
Repeat until StopIteration
```

---

# What is Lazy Evaluation?

Lazy evaluation means values are produced only when requested.

List example:

```python
values = [number * number for number in range(5)]
```

All values are created immediately.

Generator example:

```python
values = (number * number for number in range(5))
```

Values are created one at a time.

---

# Why Lazy Evaluation Matters

Imagine processing a file with one million lines.

Eager approach:

```python
lines = file.readlines()
```

This loads every line into memory.

Lazy approach:

```python
for line in file:
    process(line)
```

This processes one line at a time.

Lazy evaluation helps with large data, streams, pipelines, and long-running
programs.

---

# What is a Generator?

A generator is a special kind of iterator.

Generator functions use `yield`.

```python
def countdown(start):
    while start >= 0:
        yield start
        start -= 1
```

Usage

```python
for number in countdown(3):
    print(number)
```

Output

```text
3
2
1
0
```

---

# Generator State

When a generator yields a value, it pauses.

When `next` is called again, it resumes from the same place.

```text
Call next
   |
   v
Run until yield
   |
   v
Return value and pause
   |
   v
Call next again
   |
   v
Resume after yield
```

---

# Real-World Example: Pagination

```python
def page_numbers(total_pages):
    page = 1

    while page <= total_pages:
        yield page
        page += 1
```

Usage

```python
for page in page_numbers(3):
    print(f"Fetching page {page}")
```

Output

```text
Fetching page 1
Fetching page 2
Fetching page 3
```

---

# Common Mistake: Reusing an Exhausted Iterator

```python
numbers = iter([1, 2, 3])

print(list(numbers))
print(list(numbers))
```

Output

```text
[1, 2, 3]
[]
```

The iterator is exhausted after the first `list` call.

Create a new iterator if you need to loop again.

---

# Best Practices

- Use lists when you need all values in memory.
- Use generators when values can be processed one at a time.
- Remember that iterators can be exhausted.
- Use clear generator function names.
- Keep generator logic simple and focused.
- Convert to `list()` only when you truly need all values.

---

# Summary

Iterators and generators are the foundation of Python's lazy iteration model.

They allow programs to process data one value at a time, which improves memory
usage and supports streaming workflows.
