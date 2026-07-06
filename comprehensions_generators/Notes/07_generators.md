# Generators

---

# Learning Objectives

After completing this chapter, you will understand:

- What generators are
- The yield keyword
- Lazy evaluation
- Infinite generators
- Memory efficiency
- Enterprise use cases

---

# What is a Generator?

A generator is a function that returns values one at a time using the
`yield` keyword.

Unlike normal functions, generators pause after producing a value and
resume from the same point when the next value is requested.

---

# yield

```python
def countdown(start):
    while start >= 0:
        yield start
        start -= 1
```

Example

```python
for number in countdown(5):
    print(number)
```

Output

```
5
4
3
2
1
0
```

---

# Generator vs Return

return

- Ends the function.
- Returns a single value.

yield

- Pauses execution.
- Produces multiple values over time.

---

# Fibonacci Generator

```python
def fibonacci(count):
    previous = 0
    current = 1

    for _ in range(count):
        yield previous
        previous, current = (
            current,
            previous + current,
        )
```

---

# Infinite Generator

```python
def counter():
    value = 0

    while True:
        yield value
        value += 1
```

Use carefully because the sequence never ends.

---

# Reading Files Lazily

```python
def read_lines(path):

    with open(path) as file:

        for line in file:
            yield line
```

Large files can be processed one line at a time without loading the
entire file into memory.

---

# Enterprise Examples

- Log processing
- Streaming APIs
- ETL pipelines
- File processing
- Sensor data
- Real-time analytics

---

# Best Practices

✔ Prefer generators for large datasets.

✔ Use descriptive generator names.

✔ Avoid storing all generated values unless necessary.

---

# Summary

Generators produce values lazily, making Python applications more memory
efficient and scalable.