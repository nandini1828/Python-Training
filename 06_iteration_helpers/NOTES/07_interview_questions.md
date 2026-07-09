# any() and all()

---

# Learning Objectives

After completing this chapter, you will understand:

- any()
- all()
- Boolean evaluation
- Validation
- Membership testing

---

# any()

`any()` returns True if at least one element is truthy.

Example

```python
numbers = [1, 3, 4]

any(
    number % 2 == 0
    for number in numbers
)
```

Output

```
True
```

---

# all()

`all()` returns True only if every element is truthy.

Example

```python
numbers = [2, 4, 6]

all(
    number % 2 == 0
    for number in numbers
)
```

Output

```
True
```

---

# Membership Check

```python
users = [
    "guest",
    "admin",
]

any(
    user == "admin"
    for user in users
)
```

---

# Validation Example

```python
scores = [95, 80, 72]

all(
    0 <= score <= 100
    for score in scores
)
```

---

# Empty Strings

```python
names = [
    "Alice",
    "",
    "Bob",
]

any(name == "" for name in names)
```

Output

```
True
```

---

# File Validation

```python
status = [
    True,
    True,
    False,
]

all(status)
```

Output

```
False
```

---

# Enterprise Examples

- Input validation
- User authorization
- Permission checks
- File existence checks
- Data quality validation

---

# Best Practices

✔ Use `any()` when only one matching item is required.

✔ Use `all()` when every item must satisfy a condition.

✔ Prefer generator expressions for efficiency.

---

# Summary

`any()` and `all()` simplify validation and boolean checks, making code shorter, more expressive, and easier to maintain.