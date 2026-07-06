# Iterator Protocol

---

# Learning Objectives

After completing this chapter, you will understand:

- What an iterator is
- The Iterator Protocol
- `iter()`
- `next()`
- `StopIteration`
- Custom iterators

---

# Iterable vs Iterator

## Iterable

An object that can produce an iterator.

Examples

- list
- tuple
- string
- dictionary
- set

---

## Iterator

An object that returns one value at a time.

---

# iter()

Convert an iterable into an iterator.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)
```

---

# next()

Retrieve the next value.

```python
next(iterator)
```

Output

```
1
```

Calling `next()` repeatedly returns subsequent values.

---

# StopIteration

When no more values are available, Python raises

```
StopIteration
```

This signals that iteration has completed.

---

# Custom Iterator

```python
class Counter:

    def __iter__(self):
        return self

    def __next__(self):
        ...
```

Python's `for` loop automatically calls these methods.

---

# Iterator Protocol

An iterator must implement:

- `__iter__()`
- `__next__()`

This protocol powers all `for` loops in Python.

---

# Enterprise Examples

- Reading large files
- Streaming API responses
- Database cursors
- Log processing
- Network packet processing

---

# Best Practices

✔ Use iterators for sequential access.

✔ Raise `StopIteration` correctly.

✔ Prefer generators when a custom iterator only yields values.

---

# Summary

Understanding the Iterator Protocol explains how Python's iteration model works and forms the foundation for generators.