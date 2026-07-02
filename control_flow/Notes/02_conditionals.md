# Conditional Statements in Python

---

# What is a Conditional Statement?

A conditional statement allows Python to execute code only when a specific condition is True.

Syntax

```python
if condition:
    statement
```

---

# if Statement

Example

```python
age = 20

if age >= 18:
    print("Adult")
```

Output

```
Adult
```

Flow

```
Condition

↓

True

↓

Execute Block
```

---

# if-else

Used when there are exactly two possible outcomes.

Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output

```
Minor
```

Flow

```
          Condition
         /         \
      True         False
       |              |
       ▼              ▼
 Adult Block     Minor Block
```

---

# if-elif-else

Used when there are multiple conditions.

Example

```python
marks = 82

if marks >= 90:
    grade = "A"

elif marks >= 80:
    grade = "B"

elif marks >= 70:
    grade = "C"

else:
    grade = "Fail"
```

---

# Nested if

Example

```python
age = 25

has_license = True

if age >= 18:
    if has_license:
        print("Can Drive")
```

---

# Guard Clauses

Instead of deeply nested conditions,

Prefer

```python
if age < 18:
    return

process_user()
```

instead of

```python
if age >= 18:
    process_user()
```

Guard Clauses improve readability.

---

# Common Mistakes

❌

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

❌

```python
if x > 10
```

Missing colon.

Correct

```python
if x > 10:
```

---

# Best Practices

✔ Prefer simple conditions.

✔ Avoid nested if statements whenever possible.

✔ Use Guard Clauses.

✔ Keep conditions readable.

✔ Use descriptive variable names.

Instead of

```python
if x:
```

Prefer

```python
if is_authenticated:
```

---

# Summary

Conditional statements allow Python to make decisions based on conditions.

Python provides

- if
- if else
- if elif else
- nested if
- guard clauses