# Truthy and Falsy Values in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand what Truthy and Falsy values are.
- Identify values that evaluate to `True` or `False`.
- Use Truthy/Falsy values effectively in conditions.
- Write cleaner and more Pythonic code.
- Avoid common mistakes.

---

# Introduction

In Python, conditions are not limited to `True` and `False`.

Almost every object in Python has an associated Boolean value.

When an object is used in a conditional statement, Python automatically determines whether it should be treated as **True** or **False**.

Example

```python
if [1, 2, 3]:
    print("This list is not empty")
```

Output

```
This list is not empty
```

Although the condition is a list and not a Boolean, Python treats it as `True`.

---

# What are Truthy Values?

A **Truthy** value is any value that evaluates to `True` when used in a Boolean context.

Examples

```python
10
-5
3.14
"Python"
[1, 2]
{"name": "Ganesh"}
{1, 2, 3}
(1, 2)
True
```

Example

```python
name = "Ganesh"

if name:
    print("Name is available")
```

Output

```
Name is available
```

---

# What are Falsy Values?

A **Falsy** value is any value that evaluates to `False`.

Python has only a few built-in Falsy values.

| Value | Description |
|--------|-------------|
| False | Boolean False |
| None | Absence of value |
| 0 | Integer zero |
| 0.0 | Floating point zero |
| "" | Empty string |
| '' | Empty string |
| [] | Empty list |
| () | Empty tuple |
| {} | Empty dictionary |
| set() | Empty set |
| range(0) | Empty range |

---

# Examples of Falsy Values

```python
if "":
    print("Hello")
else:
    print("Empty String")
```

Output

```
Empty String
```

---

```python
if []:
    print("List")
else:
    print("Empty List")
```

Output

```
Empty List
```

---

```python
if 0:
    print("Positive")
else:
    print("Zero evaluates to False")
```

Output

```
Zero evaluates to False
```

---

# How Python Evaluates Conditions

Python internally calls the equivalent of `bool()`.

Example

```python
print(bool(10))
print(bool(0))
print(bool("Python"))
print(bool(""))
print(bool([]))
print(bool([1]))
```

Output

```
True
False
True
False
False
True
```

---

# Checking Empty Collections

Instead of writing

```python
numbers = []

if len(numbers) > 0:
    print("Not Empty")
```

Prefer

```python
numbers = []

if numbers:
    print("Not Empty")
else:
    print("Empty")
```

This is more Pythonic and easier to read.

---

# Checking Dictionaries

```python
student = {}

if student:
    print("Dictionary has data")
else:
    print("Dictionary is empty")
```

---

# Checking Strings

```python
message = ""

if message:
    print(message)
else:
    print("No message found")
```

---

# Checking None

```python
data = None

if data:
    print("Available")
else:
    print("No Data")
```

---

# Real-World Examples

### Login Validation

```python
username = input("Username: ")

if username:
    print("Username Accepted")
else:
    print("Username Required")
```

---

### Shopping Cart

```python
cart = []

if cart:
    print("Proceed to Checkout")
else:
    print("Cart is Empty")
```

---

### API Response

```python
response = {}

if response:
    print("Data Received")
else:
    print("No Data Found")
```

---

# Best Practices

✅ Use objects directly in conditions.

Good

```python
if users:
```

Avoid

```python
if len(users) > 0:
```

---

Use `is None` when checking for `None`.

Good

```python
if value is None:
```

Avoid

```python
if value == None:
```

---

Use meaningful variable names.

Good

```python
is_authenticated = True
```

Bad

```python
flag = True
```

---

# Common Mistakes

### Comparing with True

Wrong

```python
if status == True:
```

Correct

```python
if status:
```

---

### Comparing with False

Wrong

```python
if status == False:
```

Correct

```python
if not status:
```

---

### Using len() unnecessarily

Wrong

```python
if len(items) != 0:
```

Correct

```python
if items:
```

---

# Interview Questions

1. What is a Truthy value?
2. What is a Falsy value?
3. Name five Falsy values in Python.
4. Why is an empty list considered False?
5. What does `bool([])` return?
6. Why is `if items:` preferred over `if len(items) > 0:`?
7. Difference between `None` and `False`.

---

# Practice Exercises

1. Check whether a string is empty.
2. Check whether a list contains elements.
3. Validate user input using Truthy values.
4. Determine whether a dictionary has data.
5. Print all Truthy values from a list.
6. Count the number of Falsy values in a collection.

---

# Summary

- Python automatically converts objects to Boolean values.
- Non-empty objects are generally Truthy.
- Empty objects evaluate to False.
- `None` is a Falsy value.
- Use objects directly in conditions for cleaner and more Pythonic code.
- Prefer `is None` when checking for `None`.