# Logical Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand logical operators in Python.
- Combine multiple conditions effectively.
- Differentiate between `and`, `or`, and `not`.
- Write cleaner conditional statements.
- Avoid common logical mistakes.

---

# Introduction

In many real-world applications, a single condition is not sufficient to make a decision.

For example:

- A student must have **attendance greater than 75% AND marks above 40** to pass.
- A user can log in using **email OR phone number**.
- Access should be denied if the user is **NOT authenticated**.

Python provides **logical operators** to combine multiple conditions.

---

# Types of Logical Operators

| Operator | Meaning |
|----------|----------|
| `and` | Returns True if all conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the Boolean value |

---

# The `and` Operator

The `and` operator returns `True` only if **all conditions are True**.

Syntax

```python
condition1 and condition2
```

Example

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
```

Output

```
Eligible to Vote
```

---

### Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

# The `or` Operator

The `or` operator returns `True` if **at least one condition is True**.

Syntax

```python
condition1 or condition2
```

Example

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")
```

Output

```
Access Granted
```

---

### Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

# The `not` Operator

The `not` operator reverses the Boolean value.

Syntax

```python
not condition
```

Example

```python
is_logged_in = False

if not is_logged_in:
    print("Please Login")
```

Output

```
Please Login
```

---

### Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

---

# Combining Multiple Operators

Example

```python
age = 25
citizen = True
criminal_record = False

if age >= 18 and citizen and not criminal_record:
    print("Eligible")
```

---

# Real-World Examples

### Login System

```python
username = "admin"
password = "python"

if username == "admin" and password == "python":
    print("Login Successful")
```

---

### Employee Access

```python
is_manager = False
is_admin = True

if is_manager or is_admin:
    print("Access Granted")
```

---

### Online Shopping

```python
stock = True
payment_done = True

if stock and payment_done:
    print("Order Confirmed")
```

---

### Scholarship Eligibility

```python
marks = 88
income = 180000

if marks >= 85 and income < 300000:
    print("Eligible for Scholarship")
```

---

# Operator Precedence

Python evaluates logical operators in this order:

1. `not`
2. `and`
3. `or`

Example

```python
result = True or False and False
print(result)
```

Output

```
True
```

Explanation

```
False and False → False

True or False → True
```

---

# Using Parentheses

Parentheses improve readability.

Good

```python
if (age >= 18 and citizen) or is_admin:
    print("Access")
```

---

# Best Practices

✅ Keep conditions readable.

Good

```python
if is_logged_in and is_verified:
```

Avoid

```python
if is_logged_in == True and is_verified == True:
```

---

Use meaningful variable names.

Good

```python
has_permission = True
```

Bad

```python
x = True
```

---

Break complex conditions into variables.

Good

```python
eligible = age >= 18 and citizen

if eligible:
    print("Allowed")
```

---

# Common Mistakes

### Comparing with True

Wrong

```python
if is_admin == True:
```

Correct

```python
if is_admin:
```

---

### Incorrect Use of `or`

Wrong

```python
if role == "Admin" or "Manager":
```

Correct

```python
if role == "Admin" or role == "Manager":
```

Better

```python
if role in ("Admin", "Manager"):
```

---

### Forgetting Parentheses

Complex expressions become difficult to read without grouping.

---

# Interview Questions

1. What are logical operators?
2. Explain `and`, `or`, and `not`.
3. What is operator precedence?
4. Difference between `and` and `or`.
5. What does `not` do?
6. How can logical operators improve code readability?
7. When should parentheses be used?

---

# Practice Exercises

1. Check whether a person is eligible to vote.
2. Validate username and password.
3. Determine scholarship eligibility.
4. Grant access to admin or manager.
5. Build a simple login system using logical operators.
6. Write conditions using `and`, `or`, and `not`.

---

# Summary

- `and` returns `True` only if all conditions are True.
- `or` returns `True` if at least one condition is True.
- `not` reverses the Boolean value.
- Parentheses improve readability.
- Use meaningful variable names and avoid unnecessary comparisons with `True` or `False`.