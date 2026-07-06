# Dictionary Iteration

---

# Learning Objectives

After completing this chapter, you will be able to:

- Iterate over dictionary keys, values, and items.
- Choose the correct dictionary view method.
- Merge, invert, and search dictionaries.
- Count frequencies using dictionary updates.
- Avoid repeated lookups when key/value pairs are needed.

---

# Introduction

A dictionary stores data as key/value pairs.

Example

```python
student = {
    "name": "Asha",
    "marks": 92,
    "city": "Pune",
}
```

Here:

- `"name"` is a key.
- `"Asha"` is a value.
- `"name": "Asha"` is an item.

---

# Iterating Over Keys

By default, iterating over a dictionary gives keys.

```python
for key in student:
    print(key)
```

Output

```text
name
marks
city
```

This is the same as:

```python
for key in student.keys():
    print(key)
```

---

# Iterating Over Values

Use `.values()` when only values are needed.

```python
for value in student.values():
    print(value)
```

Output

```text
Asha
92
Pune
```

---

# Iterating Over Items

Use `.items()` when both key and value are needed.

```python
for key, value in student.items():
    print(key, value)
```

Output

```text
name Asha
marks 92
city Pune
```

This is one of the most common dictionary patterns in Python.

---

# Dictionary View Methods

| Method | Returns | Use When |
|---|---|---|
| `.keys()` | Dictionary keys | You only need field names |
| `.values()` | Dictionary values | You only need stored values |
| `.items()` | Key/value pairs | You need both |

Dictionary views are dynamic. They reflect changes made to the dictionary.

---

# Real-World Example: Report Formatting

```python
sales = {
    "January": 120000,
    "February": 98000,
    "March": 143000,
}

for month, amount in sales.items():
    print(f"{month}: Rs. {amount}")
```

Output

```text
January: Rs. 120000
February: Rs. 98000
March: Rs. 143000
```

---

# Counting Frequency

Dictionaries are excellent for counting.

```python
words = ["python", "sql", "python", "git", "sql"]
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

Output

```text
{'python': 2, 'sql': 2, 'git': 1}
```

The `get` method prevents a `KeyError` when the word appears for the first time.

---

# Merging Dictionaries

```python
defaults = {"theme": "light", "language": "en"}
user_settings = {"theme": "dark"}

settings = defaults.copy()
settings.update(user_settings)

print(settings)
```

Output

```text
{'theme': 'dark', 'language': 'en'}
```

Values from `user_settings` override matching keys from `defaults`.

---

# Inverting a Dictionary

```python
status_codes = {
    "success": 200,
    "not_found": 404,
}

inverted = {value: key for key, value in status_codes.items()}
```

Result

```python
{200: "success", 404: "not_found"}
```

Only invert dictionaries when values are unique and hashable.

---

# Common Mistakes

## Mistake 1: Looking up values repeatedly

Avoid:

```python
for key in data:
    print(key, data[key])
```

Prefer:

```python
for key, value in data.items():
    print(key, value)
```

## Mistake 2: Assuming missing keys return None

```python
student["grade"]
```

This raises `KeyError` if `"grade"` does not exist.

Use `.get()` when missing keys are normal.

## Mistake 3: Changing dictionary size while iterating

Avoid adding or removing keys while looping over the same dictionary view.

---

# Best Practices

- Use `.items()` for key/value loops.
- Use `.get()` for optional keys.
- Copy a dictionary before applying safe modifications.
- Be careful when inverting dictionaries.
- Keep dictionary keys consistent in type and naming.

---

# Summary

Dictionary iteration is about choosing the correct view of the data.

Keys, values, and items all answer different questions. Clean Python code makes
that choice explicit.
