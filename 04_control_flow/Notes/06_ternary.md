# Ternary Operator

---

# Learning Objectives

After completing this chapter you will understand:

- What the ternary operator is
- Its syntax
- Practical usage
- When to avoid it
- Best practices

---

# What is a Ternary Operator?

A ternary operator is a compact way to write an `if-else` statement.

General Syntax

```python
value_if_true if condition else value_if_false
```

---

# Traditional if-else

```python
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

---

# Ternary Version

```python
status = "Adult" if age >= 18 else "Minor"
```

Both produce exactly the same result.

---

# Example

```python
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

Output

```
Even
```

---

# Returning Values

```python
def maximum(a, b):
    return a if a > b else b
```

---

# Function Arguments

```python
message = (
    "Welcome"
    if logged_in
    else "Login Required"
)
```

---

# Nested Ternary

Python allows nesting.

Example

```python
grade = (
    "A"
    if marks >= 90
    else "B"
    if marks >= 80
    else "C"
)
```

Although valid,

this becomes difficult to read.

---

# When NOT to Use

Avoid

```python
result = (
    "Excellent"
    if score >= 90
    else "Good"
    if score >= 75
    else "Average"
    if score >= 50
    else "Poor"
)
```

Instead

```python
if score >= 90:
    result = "Excellent"

elif score >= 75:
    result = "Good"

elif score >= 50:
    result = "Average"

else:
    result = "Poor"
```

Readability is far better.

---

# Enterprise Examples

Shipping

```python
shipping = 0 if amount >= 1000 else 99
```

Discount

```python
discount = 20 if premium else 5
```

Authentication

```python
message = (
    "Welcome"
    if authenticated
    else "Access Denied"
)
```

---

# Best Practices

✔ Use ternary operators only for simple decisions.

✔ Prefer standard `if-elif-else` for complex logic.

✔ Keep readability above brevity.

---

# Summary

The ternary operator provides a concise way to assign values based on a condition.

Use it when it improves readability, but avoid deeply nested ternary expressions.