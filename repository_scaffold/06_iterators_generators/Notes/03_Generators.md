# Generators

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand generator functions.
- Use `yield` to produce values lazily.
- Explain how generators pause and resume.
- Build finite generator sequences.
- Filter and batch values with generators.
- Avoid common generator exhaustion mistakes.

---

# Introduction

A generator function is a function that uses `yield`.

Instead of returning one final value, it produces a sequence of values one at a
time.

Example

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Usage

```python
for number in numbers():
    print(number)
```

Output

```text
1
2
3
```

---

# return vs yield

`return` ends a function.

`yield` pauses a function and sends a value to the caller.

```python
def normal_function():
    return 10
```

```python
def generator_function():
    yield 10
```

Calling a generator function does not run the body immediately.

It returns a generator object.

---

# Generator Execution Flow

```text
Call generator function
        |
        v
Generator object created
        |
        v
Call next()
        |
        v
Run until yield
        |
        v
Pause and return value
        |
        v
Call next() again
        |
        v
Resume after previous yield
```

---

# Natural Numbers

```python
def natural_numbers(limit):
    value = 0

    while value < limit:
        yield value
        value += 1
```

Usage

```python
print(list(natural_numbers(5)))
```

Output

```text
[0, 1, 2, 3, 4]
```

---

# Fibonacci Generator

```python
def fibonacci(limit):
    a, b = 0, 1

    for _ in range(limit):
        yield a
        a, b = b, a + b
```

Usage

```python
print(list(fibonacci(6)))
```

Output

```text
[0, 1, 1, 2, 3, 5]
```

The generator keeps only the current two values in memory.

---

# Filtering with Generators

```python
def filtered_numbers(values, threshold):
    for number in values:
        if number > threshold:
            yield number
```

Usage

```python
values = [1, 5, 2, 8]
print(list(filtered_numbers(values, 4)))
```

Output

```text
[5, 8]
```

---

# Batching Values

```python
def batched(values, size):
    batch = []

    for value in values:
        batch.append(value)

        if len(batch) == size:
            yield batch
            batch = []

    if batch:
        yield batch
```

Usage

```python
print(list(batched([1, 2, 3, 4, 5], 2)))
```

Output

```text
[[1, 2], [3, 4], [5]]
```

This pattern is useful for database inserts, API requests, and report chunks.

---

# Real-World Example: Reading Lines

```python
def clean_lines(lines):
    for line in lines:
        yield line.strip()
```

Usage

```python
raw_lines = ["hello\n", "world\n"]
print(list(clean_lines(raw_lines)))
```

Output

```text
['hello', 'world']
```

In real projects, `lines` could be a file object.

---

# Generator Exhaustion

Generators can be consumed only once.

```python
values = natural_numbers(3)

print(list(values))
print(list(values))
```

Output

```text
[0, 1, 2]
[]
```

Create a new generator if values are needed again.

---

# Common Mistakes

## Mistake 1: Expecting immediate execution

```python
values = natural_numbers(5)
```

The function body has not fully run yet.

## Mistake 2: Reusing an exhausted generator

Once consumed, the generator is empty.

## Mistake 3: Yielding mutable state accidentally

When yielding lists or dictionaries, make sure later mutations do not surprise
the caller.

---

# Best Practices

- Use generators for large or streaming data.
- Keep generator functions focused.
- Validate inputs before yielding values.
- Convert to `list()` only for display, testing, or when all values are needed.
- Document whether a function returns a list or a generator.

---

# Summary

Generators are a clean way to create lazy sequences.

They pause at each `yield`, resume when the next value is requested, and help
programs work efficiently with large or unknown amounts of data.
