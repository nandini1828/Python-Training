# enumerate()

---

# Learning Objectives

After completing this chapter, you will understand:

- Why enumerate() exists
- How it works
- Custom starting indices
- Practical examples
- Best practices

---

# What is enumerate()?

`enumerate()` returns both the index and the value while iterating.

---

# Without enumerate()

```python
languages = [
    "Python",
    "Java",
]

for i in range(len(languages)):
    print(i, languages[i])
```

---

# With enumerate()

```python
for index, language in enumerate(languages):
    print(index, language)
```

Cleaner and easier to read.

---

# Custom Starting Index

```python
students = [
    "Alice",
    "Bob",
]

for rank, student in enumerate(students, start=1):
    print(rank, student)
```

Output

```
1 Alice
2 Bob
```

---

# Enumerating Strings

```python
for index, character in enumerate("Python"):
    print(index, character)
```

---

# Enumerating Dictionary Keys

```python
for index, key in enumerate(data):
    print(index, key)
```

---

# Enterprise Examples

- Report numbering
- Ranking systems
- CSV row numbers
- Log processing
- Progress tracking

---

# Common Mistakes

Avoid

```python
for i in range(len(items)):
```

when you only need the index and value.

Prefer

```python
enumerate(items)
```

---

# Best Practices

✔ Use meaningful variable names.

✔ Start numbering at 1 when displaying data to users.

✔ Use the default start value of 0 for internal processing.

---

# Summary

`enumerate()` is the preferred way to iterate when both the index and the value are required.