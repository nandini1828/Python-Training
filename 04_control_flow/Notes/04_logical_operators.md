# Logical Operators in Python

---

# Learning Objectives

After completing this chapter, you will understand:

- Why logical operators exist
- The difference between `and`, `or`, and `not`
- Operator precedence
- Combining multiple conditions
- Membership testing
- Identity testing
- Enterprise use cases

---

# What are Logical Operators?

Logical operators allow us to combine multiple conditions into a single expression.

Python provides three logical operators:

- `and`
- `or`
- `not`

Example

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can Drive")
```

Output

```
Can Drive
```

---

# AND Operator

The `and` operator returns **True only if every condition is True**.

Truth Table

| A | B | A and B |
|---|---|----------|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

Example

```python
salary = 70000
credit_score = 760

if salary >= 50000 and credit_score >= 700:
    print("Loan Approved")
```

---

# OR Operator

The `or` operator returns True if **at least one condition is True**.

Truth Table

| A | B | A or B |
|---|---|---------|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

Example

```python
role = "developer"

if role == "admin" or role == "developer":
    print("Access Granted")
```

---

# NOT Operator

The `not` operator reverses the Boolean value.

Truth Table

| A | not A |
|---|-------|
| True | False |
| False | True |

Example

```python
is_deleted = False

if not is_deleted:
    print("User is Active")
```

---

# Combining Operators

Python allows multiple logical operators.

Example

```python
if age >= 18 and is_verified or is_admin:
    print("Access Granted")
```

Although valid, this is difficult to read.

Better

```python
if (age >= 18 and is_verified) or is_admin:
    print("Access Granted")
```

---

# Operator Precedence

Python evaluates operators in this order

```
()

↓

not

↓

and

↓

or
```

Example

```python
True or False and False
```

Python evaluates

```python
True or (False and False)
```

Result

```
True
```

---

# Membership Operator

Often combined with logical operators.

Example

```python
permissions = {"read", "write"}

if "write" in permissions:
    print("Can Edit")
```

---

# Identity Operator

Python also provides

```
is

is not
```

Example

```python
user = None

if user is None:
    print("No User")
```

---

# Enterprise Example

Authentication

```python
if (
    is_authenticated
    and is_verified
    and not is_blocked
):
    grant_access()
```

---

# Best Practices

✔ Use parentheses when expressions become complex.

✔ Split large conditions across multiple lines.

✔ Use descriptive variable names.

✔ Avoid unnecessary comparisons with `True`.

Good

```python
if is_admin:
```

Bad

```python
if is_admin == True:
```

---

# Summary

Logical operators allow multiple conditions to work together.

Python provides

- and
- or
- not

Understanding these operators is essential for writing real-world business logic.
