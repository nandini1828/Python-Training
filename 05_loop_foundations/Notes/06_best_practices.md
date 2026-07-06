# Best Practices for Loops

---

# Write Readable Loops

Readable code is maintainable code.

Good

```python
for employee in employees:
```

Poor

```python
for x in data:
```

---

# Choose the Right Loop

Use `for`

- Lists
- Tuples
- Dictionaries
- Strings

Use `while`

- Retry logic
- Polling
- Waiting
- User input

---

# Avoid Infinite Loops

Incorrect

```python
count = 1

while count <= 10:

    print(count)
```

The loop never updates `count`.

Correct

```python
count += 1
```

---

# Avoid Modifying Collections While Iterating

Incorrect

```python
for number in numbers:

    if number < 0:
        numbers.remove(number)
```

This can skip elements.

Better

```python
result = []

for number in numbers:

    if number >= 0:
        result.append(number)
```

---

# Keep Loop Bodies Small

Avoid very large loops.

Extract logic into helper functions.

Good

```python
for order in orders:

    process_order(order)
```

---

# Prefer Early Exit

Instead of unnecessary work,

use

```python
break
```

when the result is already known.

---

# Skip Invalid Data

Instead of nested conditions,

use

```python
continue
```

---

# Avoid Deep Nesting

Bad

```
for

↓

if

↓

if

↓

if
```

Prefer helper functions.

---

# Use enumerate()

Instead of

```python
for i in range(len(names)):
```

Prefer

```python
for index, name in enumerate(names):
```

---

# Don't Abuse while

Many beginners write

```python
while True:
```

without an exit condition.

Always ensure the loop can terminate.

---

# Follow PEP 8

✔ Meaningful names

✔ Four-space indentation

✔ Small functions

✔ Type hints

✔ Docstrings

---

# Enterprise Checklist

Before writing a loop ask

- Can this be a for loop?
- Can this be simplified?
- Is break required?
- Is continue required?
- Can the loop body become a function?

---

# Summary

Professional Python code favors

- readability
- maintainability
- correctness

over writing the shortest possible loop.