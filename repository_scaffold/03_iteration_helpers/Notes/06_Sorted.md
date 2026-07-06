# sorted() in Python

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what `sorted()` returns.
- Sort lists, tuples, strings, and other iterables.
- Sort in ascending and descending order.
- Use the `key` parameter for custom sorting.
- Compare `sorted()` with `list.sort()`.
- Avoid common mutation mistakes.

---

# Introduction

`sorted()` is a built-in function that returns a new sorted list.

Example

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(result)
```

Output

```text
[1, 2, 3]
```

The original list is not changed.

---

# Syntax

```python
sorted(iterable, key=None, reverse=False)
```

| Parameter | Meaning |
|---|---|
| `iterable` | Values to sort |
| `key` | Function used to calculate sort value |
| `reverse` | Sort descending when `True` |

---

# Basic Sorting

```python
numbers = [5, 2, 9, 1]

print(sorted(numbers))
```

Output

```text
[1, 2, 5, 9]
```

---

# Original Data is Not Modified

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(numbers)
print(result)
```

Output

```text
[3, 1, 2]
[1, 2, 3]
```

This makes `sorted()` safe when the original order is still needed.

---

# Descending Sort

```python
numbers = [3, 1, 2]
result = sorted(numbers, reverse=True)
```

Output

```text
[3, 2, 1]
```

---

# Sorting Strings

```python
words = ["banana", "apple", "cherry"]

print(sorted(words))
```

Output

```text
['apple', 'banana', 'cherry']
```

Strings are sorted alphabetically by default.

---

# Sorting with key

The `key` parameter controls what Python uses for comparison.

Sort by length:

```python
words = ["apple", "kiwi", "banana"]
result = sorted(words, key=len)
```

Output

```text
['kiwi', 'apple', 'banana']
```

---

# Sorting Dictionaries in a List

```python
students = [
    {"name": "Asha", "marks": 92},
    {"name": "Ravi", "marks": 84},
    {"name": "Mira", "marks": 96},
]

ranked = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True,
)
```

Result

```python
[
    {"name": "Mira", "marks": 96},
    {"name": "Asha", "marks": 92},
    {"name": "Ravi", "marks": 84},
]
```

---

# sorted() vs list.sort()

| Feature | `sorted()` | `list.sort()` |
|---|---|---|
| Returns a value | Yes | No |
| Modifies original list | No | Yes |
| Works with any iterable | Yes | No, lists only |
| Good for | Sorted copy | In-place sorting |

Example:

```python
numbers = [3, 1, 2]

result = numbers.sort()
print(result)
print(numbers)
```

Output

```text
None
[1, 2, 3]
```

`list.sort()` returns `None` because it changes the list directly.

---

# Stable Sorting

Python sorting is stable.

This means values with equal sort keys keep their original relative order.

```python
students = [
    ("Asha", 90),
    ("Ravi", 80),
    ("Mira", 90),
]

result = sorted(students, key=lambda student: student[1])
```

`Asha` remains before `Mira` because both have the same score.

---

# Real-World Example: Leaderboard

```python
players = [
    {"name": "Asha", "score": 120},
    {"name": "Ravi", "score": 150},
    {"name": "Mira", "score": 130},
]

leaderboard = sorted(
    players,
    key=lambda player: player["score"],
    reverse=True,
)
```

This pattern appears in dashboards, games, reports, and analytics.

---

# Common Mistakes

## Mistake 1: Expecting sorted() to modify the original

```python
numbers = [3, 1, 2]
sorted(numbers)
print(numbers)
```

Output remains:

```text
[3, 1, 2]
```

## Mistake 2: Assigning list.sort()

```python
numbers = [3, 1, 2]
result = numbers.sort()
```

`result` is `None`.

## Mistake 3: Sorting mixed incompatible types

```python
sorted([1, "two", 3])
```

This raises `TypeError` in modern Python.

---

# Best Practices

- Use `sorted()` when you need a sorted copy.
- Use `.sort()` when in-place mutation is intended.
- Use `key` for custom sorting.
- Use `reverse=True` for descending order.
- Keep lambda expressions simple.

---

# Summary

`sorted()` is a safe and flexible way to sort iterable data.

It returns a new list, supports custom sort keys, and avoids accidental mutation
of the original collection.
