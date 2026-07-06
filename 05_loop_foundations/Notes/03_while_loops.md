# while Loops

---

# What is a while Loop?

A `while` loop executes repeatedly while a condition remains True.

General Syntax

```python
while condition:
    statement
```

---

# Example

```python
count = 1

while count <= 5:
    print(count)

    count += 1
```

Output

```
1
2
3
4
5
```

---

# Execution Flow

```
Condition

↓

True

↓

Execute Body

↓

Update

↓

Condition

↓

False

↓

Exit
```

---

# Infinite Loop

```python
while True:
    ...
```

Useful for

- Servers
- Games
- Event loops

Always ensure there is an exit condition.

---

# Countdown

```python
count = 10

while count > 0:
    print(count)

    count -= 1
```

---

# User Input

```python
password = ""

while password != "python":
    password = input()
```

---

# Validation

```python
number = -1

while number < 0:
    number = int(input())
```

---

# Common Mistakes

Forgetting to update the condition.

Example

```python
count = 1

while count <= 5:
    print(count)
```

This creates an infinite loop.

Correct

```python
count += 1
```

---

# while vs for

Use `for`

- Collections
- Known iterations

Use `while`

- Unknown iterations
- Retry logic
- Waiting
- Polling
- User input

---

# Enterprise Examples

Retry API

```python
while retries < 3:
```

Authentication

```python
while attempts < 5:
```

Monitoring

```python
while server_running:
```

---

# Best Practices

✔ Always update the loop variable.

✔ Avoid unnecessary infinite loops.

✔ Prefer `for` when iterating over collections.

---

# Summary

Use `while` when repetition depends on a condition rather than a fixed number of iterations.