# any() and all() in Python

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what `any()` does.
- Understand what `all()` does.
- Use both functions with lists and generator expressions.
- Explain short-circuit evaluation.
- Handle empty iterable behavior correctly.
- Apply `any()` and `all()` in validation logic.

---

# Introduction

Programs often need to answer yes/no questions about a collection.

Examples:

- Did any test fail?
- Are all required fields filled?
- Is any product out of stock?
- Did all students pass?
- Is any user an admin?

Python provides `any()` and `all()` for these checks.

---

# What is any()?

`any()` returns `True` if at least one value in an iterable is truthy.

Syntax

```python
any(iterable)
```

Example

```python
values = [False, False, True]
print(any(values))
```

Output

```text
True
```

At least one value is `True`.

---

# What is all()?

`all()` returns `True` only if every value in an iterable is truthy.

Syntax

```python
all(iterable)
```

Example

```python
values = [True, True, False]
print(all(values))
```

Output

```text
False
```

One value is `False`, so the result is `False`.

---

# Truthy and Falsy Values

Python does not require values to be exactly `True` or `False`.

| Value | Boolean Meaning |
|---|---|
| `0` | False |
| `""` | False |
| `[]` | False |
| `{}` | False |
| `None` | False |
| Non-empty values | True |

Example

```python
values = [0, "", "hello"]
print(any(values))
```

Output

```text
True
```

`"hello"` is truthy.

---

# Using any() with Conditions

```python
scores = [35, 42, 28]

has_passing_score = any(score >= 40 for score in scores)
print(has_passing_score)
```

Output

```text
True
```

At least one score is greater than or equal to 40.

---

# Using all() with Conditions

```python
scores = [82, 91, 77]

all_passed = all(score >= 40 for score in scores)
print(all_passed)
```

Output

```text
True
```

Every score satisfies the condition.

---

# Short-Circuit Evaluation

`any()` stops as soon as it finds a truthy value.

`all()` stops as soon as it finds a falsy value.

This makes them efficient with generator expressions.

Example:

```python
numbers = [1, 2, 3, 100]

result = any(number > 10 for number in numbers)
```

Python can stop when it reaches `100`.

---

# Empty Iterable Behavior

```python
print(any([]))
print(all([]))
```

Output

```text
False
True
```

This surprises many beginners.

Why?

- `any([])` is `False` because no value is truthy.
- `all([])` is `True` because no value violates the condition.

---

# Real-World Example: Form Validation

```python
required_fields = ["Asha", "asha@example.com", ""]

has_missing_field = any(field == "" for field in required_fields)

if has_missing_field:
    print("Please fill all required fields")
```

Output

```text
Please fill all required fields
```

---

# Real-World Example: Task Completion

```python
tasks = [True, True, True]

if all(tasks):
    print("All tasks completed")
```

Output

```text
All tasks completed
```

---

# any() vs all()

| Function | Returns True When | Empty Iterable |
|---|---|---|
| `any()` | At least one value is true | `False` |
| `all()` | Every value is true | `True` |

---

# Common Mistakes

## Mistake 1: Passing a single boolean expression incorrectly

```python
any(score > 40)
```

`any()` expects an iterable.

Use:

```python
any(score > 40 for score in scores)
```

## Mistake 2: Forgetting empty iterable behavior

`all([])` returns `True`.

Handle empty data separately if that matters.

## Mistake 3: Building a list unnecessarily

Avoid:

```python
any([score >= 40 for score in scores])
```

Prefer:

```python
any(score >= 40 for score in scores)
```

The generator expression supports short-circuiting without building a full list.

---

# Best Practices

- Use `any()` for "at least one" checks.
- Use `all()` for "every item" checks.
- Prefer generator expressions inside `any()` and `all()`.
- Handle empty collections explicitly when business logic requires it.
- Keep conditions readable.

---

# Summary

`any()` and `all()` are powerful helpers for validation and condition checks.

They make intent clear, support short-circuit behavior, and work naturally with
generator expressions.
