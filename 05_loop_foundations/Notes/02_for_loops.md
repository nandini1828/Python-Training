# for Loops

---

# What is a for Loop?

A `for` loop iterates over every element of an iterable.

General Syntax

```python
for item in iterable:
    statement
```

---

# Example

```python
languages = [
    "Python",
    "Java",
    "Go",
]

for language in languages:
    print(language)
```

---

# Using range()

```python
for number in range(5):
    print(number)
```

Output

```
0
1
2
3
4
```

---

# range(start, stop)

```python
for number in range(5, 10):
    print(number)
```

---

# range(start, stop, step)

```python
for number in range(0, 20, 2):
    print(number)
```

Output

```
0
2
4
6
...
```

---

# Iterating Strings

```python
for character in "Python":
    print(character)
```

---

# Iterating Lists

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

---

# Iterating Tuples

```python
colors = (
    "Red",
    "Green",
)

for color in colors:
    print(color)
```

---

# Iterating Sets

```python
items = {
    "A",
    "B",
    "C",
}

for item in items:
    print(item)
```

Note

Sets are unordered.

---

# Iterating Dictionaries

Keys

```python
for key in data:
```

Values

```python
for value in data.values():
```

Key-Value

```python
for key, value in data.items():
```

---

# Nested Loops

```python
for row in range(3):

    for column in range(3):

        print(row, column)
```

---

# Common Mistakes

❌

```python
for i in 5:
```

Correct

```python
for i in range(5):
```

---

# Best Practices

✔ Use meaningful variable names.

✔ Prefer iterating directly over collections.

Instead of

```python
for i in range(len(names)):
```

Prefer

```python
for name in names:
```

---

# Summary

The `for` loop is the preferred choice whenever Python can iterate over an iterable.