# Dictionary Key Protection

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why missing dictionary keys cause `KeyError`.
- Use `.get()` for optional dictionary values.
- Use `.setdefault()` to add defaults safely.
- Remove keys without crashing.
- Decide when direct indexing is better than safe access.
- Write dictionary helpers that avoid unwanted mutation.

---

# Introduction

Dictionaries are used everywhere in Python.

Examples:

- User profiles
- API responses
- Configuration files
- Database records
- Form data

But dictionaries are only safe when the keys you access actually exist.

---

# The KeyError Problem

Example

```python
profile = {
    "name": "Asha",
    "email": "asha@example.com",
}

print(profile["city"])
```

Output

```text
KeyError: 'city'
```

Python raises `KeyError` because `"city"` is not present.

---

# Direct Access

Direct access is useful when a key must exist.

```python
name = profile["name"]
```

This is clear and strict.

If `"name"` is missing, the program should fail because the data is invalid.

Use direct access for required fields.

---

# Safe Access with get

Use `.get()` when missing data is normal.

```python
city = profile.get("city", "Unknown")
print(city)
```

Output

```text
Unknown
```

Syntax

```python
dictionary.get(key, default)
```

If the key exists, its value is returned. Otherwise, the default is returned.

---

# Checking Key Existence

Use the `in` operator when behavior depends on whether a key exists.

```python
if "email" in profile:
    print("Email is available")
else:
    print("Email is missing")
```

This is readable and avoids exceptions.

---

# Adding Defaults with setdefault

`setdefault` returns an existing value if the key exists.

If the key does not exist, it adds the default value.

```python
settings = {"theme": "dark"}

language = settings.setdefault("language", "en")

print(settings)
```

Output

```text
{'theme': 'dark', 'language': 'en'}
```

Be careful: `setdefault` mutates the dictionary.

In reusable helpers, copy first when mutation is not intended.

---

# Safe Removal with pop

Direct deletion fails when a key is missing.

```python
del profile["city"]
```

If `"city"` is missing, this raises `KeyError`.

Safe removal:

```python
profile.pop("city", None)
```

The second argument is the default returned when the key does not exist.

---

# Copy-Based Dictionary Updates

Reusable functions should often avoid mutating caller data.

```python
def update_dictionary(data, updates):
    result = data.copy()
    result.update(updates)
    return result
```

Usage

```python
original = {"city": "Pune"}
updated = update_dictionary(original, {"city": "Mumbai"})

print(original)
print(updated)
```

Output

```text
{'city': 'Pune'}
{'city': 'Mumbai'}
```

---

# Real-World Example: API Response

```python
response = {
    "name": "Asha",
    "subscription": "premium",
}

city = response.get("city", "Not provided")
subscription = response["subscription"]
```

`city` is optional, so `.get()` is appropriate.

`subscription` is required, so direct indexing is appropriate.

---

# Choosing the Right Pattern

| Situation | Pattern |
|---|---|
| Key must exist | `data["key"]` |
| Key may be missing | `data.get("key", default)` |
| Need to check before action | `"key" in data` |
| Add default if missing | `data.setdefault("key", value)` |
| Remove if present | `data.pop("key", None)` |

---

# Common Mistakes

## Mistake 1: Using `.get()` for required data

```python
user_id = user.get("id")
```

If `id` is required, this can hide a data bug.

Prefer:

```python
user_id = user["id"]
```

## Mistake 2: Forgetting that setdefault mutates

```python
settings.setdefault("language", "en")
```

This changes `settings`.

## Mistake 3: Removing keys without a default

```python
data.pop("temporary")
```

This raises `KeyError` when the key is missing.

---

# Best Practices

- Use direct access for required keys.
- Use `.get()` for optional keys.
- Use clear defaults such as `"Unknown"` or `0`.
- Copy dictionaries inside helper functions when mutation is not intended.
- Use `.items()` when validating multiple keys and values.

---

# Summary

Dictionary key protection is about communicating intent.

Direct indexing says "this key must exist." Safe access says "this key may be
missing." Good Python code makes that difference clear.
