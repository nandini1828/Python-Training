# Short-Circuit Evaluation

---

# Learning Objectives

After this chapter you will understand:

- What short-circuit evaluation is
- Why Python uses it
- Performance benefits
- Lazy evaluation
- Enterprise examples

---

# What is Short-Circuit Evaluation?

Python stops evaluating an expression as soon as the final result is already known.

This optimization is called **Short-Circuit Evaluation**.

---

# Example 1

```python
True or expensive_function()
```

Python immediately returns

```
True
```

because the second expression cannot change the result.

The function is never executed.

---

# Example 2

```python
False and expensive_function()
```

Result

```
False
```

Again,

Python never calls

```
expensive_function()
```

---

# Why?

Suppose

```
A or B
```

If A is already True,

the answer is guaranteed.

No reason to evaluate B.

---

# Visualization

```
        OR

A=True

↓

Result=True

↓

Skip B
```

---

```
        AND

A=False

↓

Result=False

↓

Skip B
```

---

# Cache Example

Instead of

```python
if cache:
    data = cache
else:
    data = database_query()
```

Pythonic way

```python
data = cache or database_query()
```

---

# Configuration Loading

```python
config = (
    env_config
    or file_config
    or default_config
)
```

Python returns the first available value.

---

# Safe Attribute Access

```python
username = user and user.username
```

If

```
user is None
```

Python never tries

```
user.username
```

avoiding an exception.

---

# Performance Benefits

Imagine

```
Database Query

↓

2 seconds
```

If a cached value exists,

Python never performs the expensive query.

```
Cache

↓

Immediate Result
```

---

# Enterprise Examples

Authentication

```python
is_logged_in and has_permission()
```

Permission checking happens only after successful login.

---

API Calls

```python
cached_response or fetch_from_api()
```

The API is called only when required.

---

# Best Practices

✔ Use short-circuit evaluation for lazy execution.

✔ Avoid unnecessary function calls.

✔ Keep expressions readable.

---

# Summary

Short-circuit evaluation is both

- a performance optimization
- a safety mechanism

It is used heavily in enterprise Python applications.