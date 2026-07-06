# List Modification Trap

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why modifying a list during iteration is risky.
- Explain how index shifting causes skipped values.
- Use copy-based and new-list approaches safely.
- Choose between mutation and transformation.
- Write predictable list modification helpers.

---

# Introduction

Lists are mutable.

This means their contents can be changed after creation.

```python
numbers = [1, 2, 3]
numbers.append(4)
```

The list now becomes:

```text
[1, 2, 3, 4]
```

Mutation is useful, but it becomes dangerous when the list is changed while a
loop is still iterating over it.

---

# The Problem

Consider this code:

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
```

Many beginners expect:

```text
[1, 3, 5]
```

But modifying a list during iteration can skip values because positions shift
after removal.

---

# Why Values Get Skipped

Original list:

```text
Index:   0  1  2  3  4  5
Value:   1  2  3  4  5  6
```

When `2` is removed:

```text
Index:   0  1  2  3  4
Value:   1  3  4  5  6
```

The loop moves to the next index, but the values have shifted.

This is why the result can be surprising.

---

# Safe Approach 1: Build a New List

The safest beginner-friendly approach is to build a new list.

```python
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)
```

Output

```text
[1, 3, 5]
```

The original list is not changed while the loop runs.

---

# Safe Approach 2: Iterate Over a Copy

If the original list must be modified, iterate over a copy.

```python
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
```

Output

```text
[1, 3, 5]
```

The loop reads from the copy while removal happens on the original.

---

# Safe Approach 3: Use a Comprehension

```python
numbers = [1, 2, 3, 4, 5, 6]
numbers = [number for number in numbers if number % 2 != 0]

print(numbers)
```

Output

```text
[1, 3, 5]
```

This is concise and common in production Python.

---

# Copy-Based Helper Functions

In utility functions, returning a modified copy is often safer.

```python
def append_item(values, item):
    result = values.copy()
    result.append(item)
    return result
```

Usage

```python
original = [1, 2]
updated = append_item(original, 3)

print(original)
print(updated)
```

Output

```text
[1, 2]
[1, 2, 3]
```

This avoids accidental side effects.

---

# Real-World Example: Removing Invalid Records

Unsafe:

```python
for user in users:
    if not user["email"]:
        users.remove(user)
```

Safe:

```python
valid_users = []

for user in users:
    if user["email"]:
        valid_users.append(user)
```

Or:

```python
valid_users = [user for user in users if user["email"]]
```

---

# When Mutation is Acceptable

Mutation is not always wrong.

It is acceptable when:

- The code is simple and local.
- No loop is currently reading the same list.
- The caller expects the list to change.
- The function name clearly communicates mutation.

Example:

```python
tasks.append("send report")
```

This is clear and safe.

---

# Common Mistakes

## Mistake 1: Removing while looping over the same list

```python
for item in items:
    items.remove(item)
```

## Mistake 2: Forgetting that `.sort()` mutates

```python
numbers = [3, 1, 2]
result = numbers.sort()
```

`result` becomes `None`.

Use:

```python
result = sorted(numbers)
```

## Mistake 3: Returning the original list accidentally

```python
def add_item(values, item):
    values.append(item)
    return values
```

This mutates the caller's list.

---

# Best Practices

- Do not remove items from a list while looping over the same list.
- Build a new list for filtering.
- Return copies from reusable helper functions unless mutation is intended.
- Use `sorted(values)` when a sorted copy is needed.
- Use clear function names such as `append_item` or `remove_item_safely`.

---

# Summary

List mutation is powerful but can create subtle bugs.

When iterating, prefer building a new list or iterating over a copy. This keeps
program behavior predictable and makes utility functions easier to test.
