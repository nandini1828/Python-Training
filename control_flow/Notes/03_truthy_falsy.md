# Truthy and Falsy Values

---

# What is Truthiness?

Every object in Python has a Boolean value.

Python automatically converts objects into either

```
True

or

False
```

using

```python
bool()
```

Example

```python
bool(10)
```

Output

```
True
```

---

# Truthy Values

Examples

```python
1

-5

3.14

"Python"

[1]

{"name":"Alice"}

(1,)

{1}

True
```

All of these evaluate to

```
True
```

---

# Falsy Values

Python has only a few falsy values.

```python
0

0.0

None

False

""

[]

()

{}

set()
```

Everything else is Truthy.

---

# Examples

```python
if []:
    print("Executed")

else:
    print("Skipped")
```

Output

```
Skipped
```

---

```python
if [1]:
    print("Executed")
```

Output

```
Executed
```

---

# Why?

An empty collection means

"There is nothing inside."

Python treats empty collections as False.

---

# Custom Truthiness

Objects can define

```python
__bool__()
```

or

```python
__len__()
```

Example

```python
class Cart:

    def __bool__(self):
        return False
```

Now

```python
bool(Cart())
```

returns

```
False
```

---

# Enterprise Examples

Instead of

```python
if len(users) > 0:
```

Prefer

```python
if users:
```

Instead of

```python
if response is not None and len(response) > 0:
```

Prefer

```python
if response:
```

Cleaner.

More Pythonic.

---

# Best Practices

✔ Use

```python
if collection:
```

instead of

```python
if len(collection) > 0:
```

✔ Avoid comparing with True.

Instead of

```python
if flag == True:
```

Use

```python
if flag:
```

---

# Summary

Python automatically determines whether an object is True or False.

Understanding Truthy and Falsy values allows you to write cleaner and more idiomatic Python code.