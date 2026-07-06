# Dictionary Comprehension

---

# Learning Objectives

After completing this chapter, you will be able to:

- Build dictionaries using comprehension syntax.
- Create key/value mappings from lists.
- Transform dictionary keys and values.
- Filter dictionary items.
- Understand key collision behavior.
- Avoid unsafe dictionary inversion.

---

# Introduction

Dictionary comprehensions create dictionaries from iterable data.

Basic syntax

```python
{key_expression: value_expression for item in iterable}
```

Example

```python
numbers = [1, 2, 3]
squares = {number: number * number for number in numbers}
```

Output

```text
{1: 1, 2: 4, 3: 9}
```

---

# Normal Loop vs Dictionary Comprehension

Normal loop:

```python
numbers = [1, 2, 3]
squares = {}

for number in numbers:
    squares[number] = number * number
```

Dictionary comprehension:

```python
squares = {number: number * number for number in numbers}
```

The comprehension is clear because the goal is to build a dictionary.

---

# Creating a Dictionary from Two Lists

```python
keys = ["name", "city", "role"]
values = ["Asha", "Pune", "Developer"]

profile = {key: value for key, value in zip(keys, values)}
```

Output

```python
{
    "name": "Asha",
    "city": "Pune",
    "role": "Developer",
}
```

This is useful when data arrives in parallel lists.

---

# Transforming Keys

```python
headers = {
    "content-type": "application/json",
    "authorization": "token",
}

normalized = {
    key.upper(): value
    for key, value in headers.items()
}
```

Output

```python
{
    "CONTENT-TYPE": "application/json",
    "AUTHORIZATION": "token",
}
```

---

# Transforming Values

```python
scores = {
    "Asha": 45,
    "Ravi": 40,
}

percentages = {
    name: (score / 50) * 100
    for name, score in scores.items()
}
```

Output

```python
{
    "Asha": 90.0,
    "Ravi": 80.0,
}
```

---

# Filtering Dictionary Items

```python
inventory = {
    "laptop": 5,
    "mouse": 0,
    "keyboard": 3,
}

available = {
    item: quantity
    for item, quantity in inventory.items()
    if quantity > 0
}
```

Output

```python
{
    "laptop": 5,
    "keyboard": 3,
}
```

---

# Inverting a Dictionary

```python
status_codes = {
    "ok": 200,
    "not_found": 404,
}

inverted = {
    value: key
    for key, value in status_codes.items()
}
```

Output

```python
{
    200: "ok",
    404: "not_found",
}
```

Only invert dictionaries when values are unique.

If two keys have the same value, one result will overwrite the other.

---

# Key Collision

```python
words = ["hi", "to", "python"]
length_map = {len(word): word for word in words}
```

Result

```python
{
    2: "to",
    6: "python",
}
```

`"hi"` was overwritten because `"to"` produced the same key.

---

# Real-World Example: User Lookup

```python
users = [
    {"id": 101, "name": "Asha"},
    {"id": 102, "name": "Ravi"},
]

users_by_id = {
    user["id"]: user
    for user in users
}
```

Now records can be accessed quickly:

```python
print(users_by_id[101]["name"])
```

Output

```text
Asha
```

---

# Common Mistakes

## Mistake 1: Forgetting key/value syntax

Incorrect:

```python
{number * number for number in numbers}
```

This creates a set.

Correct:

```python
{number: number * number for number in numbers}
```

## Mistake 2: Ignoring duplicate keys

Dictionary keys must be unique. Later values overwrite earlier values.

## Mistake 3: Inverting non-unique values

Do not invert dictionaries unless values are unique and hashable.

---

# Best Practices

- Use dictionary comprehensions for lookup tables.
- Keep key and value expressions readable.
- Use `.items()` when transforming existing dictionaries.
- Be careful with duplicate generated keys.
- Validate inputs when calculations can fail, such as division by zero.

---

# Summary

Dictionary comprehensions are excellent for building mappings.

They clearly show how each key and value is produced, but they require care when
generated keys may collide.
