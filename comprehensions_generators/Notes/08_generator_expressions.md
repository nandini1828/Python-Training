# Generator Expressions

---

# Learning Objectives

After completing this chapter, you will understand:

- Generator expressions
- Lazy evaluation
- Memory efficiency
- Performance considerations

---

# What is a Generator Expression?

A generator expression creates a generator using parentheses instead of
square brackets.

List comprehension

```python
[
    number ** 2
    for number in range(10)
]
```

Generator expression

```python
(
    number ** 2
    for number in range(10)
)
```

---

# Why Use Generator Expressions?

Generator expressions do not create an entire collection.

Values are produced only when needed.

---

# Example

```python
squares = (
    number ** 2
    for number in range(5)
)

for value in squares:
    print(value)
```

---

# Memory Comparison

List comprehension

```
Stores every value in memory.
```

Generator expression

```
Produces one value at a time.
```

---

# Sum Example

```python
total = sum(
    number ** 2
    for number in range(1000)
)
```

No intermediate list is created.

---

# Pipeline Example

```python
numbers = (
    value ** 2
    for value in range(100)
)

evens = (
    value
    for value in numbers
    if value % 2 == 0
)
```

---

# Enterprise Examples

- Data streaming
- Machine learning datasets
- ETL pipelines
- CSV processing
- API pagination

---

# Best Practices

✔ Prefer generator expressions for one-time iteration.

✔ Use list comprehensions when random access is required.

✔ Avoid converting generators into lists unless necessary.

---

# Summary

Generator expressions provide concise, memory-efficient processing for
large datasets.