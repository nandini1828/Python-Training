# zip() in Python

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand how `zip()` combines iterables.
- Iterate over multiple sequences in parallel.
- Build dictionaries from paired lists.
- Understand what happens when lengths differ.
- Unzip paired data.
- Avoid common mistakes with exhausted zip objects.

---

# Introduction

Sometimes related data is stored in separate collections.

Example:

```python
names = ["Asha", "Ravi", "Mira"]
marks = [92, 84, 76]
```

The first name belongs with the first mark.

The second name belongs with the second mark.

Python provides `zip()` to combine these values pair by pair.

---

# What is zip()?

`zip()` combines multiple iterables into tuples.

Syntax

```python
zip(iterable1, iterable2, ...)
```

Example

```python
names = ["Asha", "Ravi"]
marks = [92, 84]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output

```text
Asha 92
Ravi 84
```

---

# zip() Produces an Iterator

```python
result = zip(["a", "b"], [1, 2])
print(result)
```

This prints a zip object.

Convert to a list when needed:

```python
print(list(zip(["a", "b"], [1, 2])))
```

Output

```text
[('a', 1), ('b', 2)]
```

---

# Combining Three Iterables

```python
names = ["Asha", "Ravi"]
marks = [92, 84]
cities = ["Pune", "Delhi"]

for name, mark, city in zip(names, marks, cities):
    print(name, mark, city)
```

Output

```text
Asha 92 Pune
Ravi 84 Delhi
```

---

# Different Length Iterables

`zip()` stops when the shortest iterable is exhausted.

```python
names = ["Asha", "Ravi", "Mira"]
marks = [92, 84]

print(list(zip(names, marks)))
```

Output

```text
[('Asha', 92), ('Ravi', 84)]
```

`"Mira"` is ignored because there is no matching mark.

---

# Building a Dictionary

```python
keys = ["name", "city", "role"]
values = ["Asha", "Pune", "Developer"]

profile = dict(zip(keys, values))
```

Output

```python
{
    "name": "Asha",
    "city": "Pune",
    "role": "Developer",
}
```

This is one of the most common uses of `zip()`.

---

# Unzipping Data

Use `*` to unpack paired data.

```python
pairs = [("Asha", 92), ("Ravi", 84)]

names, marks = zip(*pairs)

print(names)
print(marks)
```

Output

```text
('Asha', 'Ravi')
(92, 84)
```

---

# Real-World Example: Report Rows

```python
products = ["Keyboard", "Mouse", "Monitor"]
prices = [1200, 700, 9000]

for product, price in zip(products, prices):
    print(f"{product}: Rs. {price}")
```

Output

```text
Keyboard: Rs. 1200
Mouse: Rs. 700
Monitor: Rs. 9000
```

---

# Common Mistakes

## Mistake 1: Forgetting shortest-length behavior

If inputs have different lengths, extra values are ignored.

Validate lengths when missing data would be a bug.

## Mistake 2: Reusing a consumed zip object

```python
pairs = zip(["a", "b"], [1, 2])

print(list(pairs))
print(list(pairs))
```

Output

```text
[('a', 1), ('b', 2)]
[]
```

The zip object is an iterator and can be exhausted.

## Mistake 3: Using zip when data should be a dictionary already

If values are naturally key/value data, a dictionary may be clearer from the
start.

---

# Best Practices

- Use `zip()` for parallel iteration.
- Use `dict(zip(keys, values))` to build simple mappings.
- Check lengths when missing paired data is not acceptable.
- Convert to `list()` only when you need to inspect or reuse the pairs.
- Use meaningful variable names while unpacking pairs.

---

# Summary

`zip()` is the clean Python tool for combining iterables position by position.

It is useful for reports, mappings, paired data, and parallel iteration.
