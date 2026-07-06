# Short-Circuit Evaluation in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Short-Circuit Evaluation.
- Learn how Python evaluates logical expressions.
- Improve program efficiency using short-circuiting.
- Prevent common runtime errors.

---

# Introduction

Python evaluates logical expressions from **left to right**.

If the final result can already be determined, Python **does not evaluate the remaining conditions**.

This behavior is called **Short-Circuit Evaluation**.

It improves performance and prevents unnecessary computations.

---

# Short-Circuit with `and`

For the `and` operator, if the first condition is **False**, Python immediately stops evaluating the remaining conditions.

Syntax

```python
condition1 and condition2
```

Example

```python
age = 15

if age >= 18 and age < 60:
    print("Eligible")
```

Since `age >= 18` is `False`, Python never checks the second condition.

---

# Short-Circuit with `or`

For the `or` operator, if the first condition is **True**, Python immediately stops evaluating the remaining conditions.

Example

```python
is_admin = True
is_manager = False

if is_admin or is_manager:
    print("Access Granted")
```

Python does not evaluate `is_manager`.

---

# Why Short-Circuit Evaluation is Useful

It prevents unnecessary computations.

Example

```python
def expensive_operation():
    print("Executing...")
    return True

if True or expensive_operation():
    print("Done")
```

Output

```
Done
```

`expensive_operation()` is never executed.

---

# Preventing Runtime Errors

Without Short-Circuit

```python
numbers = []

if len(numbers) > 0 and numbers[0] > 10:
    print("Valid")
```

Safe version

```python
if numbers and numbers[0] > 10:
    print("Valid")
```

Python first checks whether the list is empty.

---

# Real-World Examples

### Login Check

```python
user = None

if user and user.is_active:
    print("Access Granted")
```

---

### API Response

```python
response = {}

if response and "data" in response:
    print(response["data"])
```

---

### File Handling

```python
file = None

if file and not file.closed:
    print("File Ready")
```

---

# Best Practices

- Place inexpensive conditions first.
- Place conditions likely to fail first when using `and`.
- Place conditions likely to succeed first when using `or`.
- Use short-circuiting to avoid runtime errors.

---

# Common Mistakes

Wrong

```python
if numbers[0] > 10 and numbers:
```

Correct

```python
if numbers and numbers[0] > 10:
```

---

# Interview Questions

1. What is Short-Circuit Evaluation?
2. How does `and` short-circuit?
3. How does `or` short-circuit?
4. Why is Short-Circuit Evaluation important?
5. How can it prevent runtime errors?

---

# Practice Exercises

1. Check whether a list is empty before accessing its first element.
2. Validate user login using short-circuiting.
3. Prevent division by zero using short-circuit evaluation.
4. Write examples using both `and` and `or`.

---

# Summary

- Python evaluates logical expressions from left to right.
- `and` stops at the first False.
- `or` stops at the first True.
- Short-Circuit Evaluation improves performance and prevents errors.