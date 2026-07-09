# reversed() and sorted()

---

# Learning Objectives

After completing this chapter, you will understand:

- reversed()
- sorted()
- Reverse ordering
- Custom sorting
- Sorting with key functions

---

# reversed()

`reversed()` returns an iterator that traverses a sequence in reverse order.

Example

```python
numbers = [1, 2, 3]

for number in reversed(numbers):
    print(number)
```

Output

```
3
2
1
```

---

# Reverse a String

```python
text = "Python"

result = "".join(reversed(text))
```

Output

```
nohtyP
```

---

# sorted()

`sorted()` returns a new sorted list.

Example

```python
numbers = [5, 2, 8, 1]

sorted(numbers)
```

Output

```
[1, 2, 5, 8]
```

---

# Descending Order

```python
sorted(
    numbers,
    reverse=True,
)
```

Output

```
[8, 5, 2, 1]
```

---

# Case-Insensitive Sorting

```python
words = [
    "banana",
    "Apple",
    "cherry",
]

sorted(
    words,
    key=str.lower,
)
```

---

# Sorting by Length

```python
sorted(
    words,
    key=len,
)
```

---

# Sorting Dictionaries

```python
employees = [
    {
        "name": "Bob",
        "age": 30,
    },
    {
        "name": "Alice",
        "age": 25,
    },
]

sorted(
    employees,
    key=lambda employee: employee["age"],
)
```

---

# Enterprise Examples

- Sorting reports
- Leaderboards
- Employee lists
- Inventory reports
- Customer records

---

# Best Practices

✔ Prefer `sorted()` when you need a new list.

✔ Use `key` for custom sorting.

✔ Use `reverse=True` for descending order.

---

# Summary

`reversed()` and `sorted()` provide simple, readable solutions for reversing and ordering data.