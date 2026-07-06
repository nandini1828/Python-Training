# for-else and while-else

---

# Learning Objectives

After completing this chapter, you will understand:

- What loop `else` means
- When the `else` block executes
- Searching patterns
- Retry patterns
- Prime number examples

---

# Introduction

Many developers misunderstand Python's loop `else`.

The `else` block executes **only if the loop finishes normally**.

If the loop executes a `break`, the `else` block is skipped.

---

# for-else

Example

```python
numbers = [1, 3, 5]

for number in numbers:

    if number == 4:
        break

else:
    print("Not Found")
```

Output

```
Not Found
```

The loop completed normally.

---

# Example with break

```python
numbers = [1, 3, 4, 5]

for number in numbers:

    if number == 4:
        print("Found")
        break

else:
    print("Not Found")
```

Output

```
Found
```

The `else` block never executes.

---

# Search Pattern

```python
for employee in employees:

    if employee.id == target:
        break

else:
    print("Employee Not Found")
```

---

# Prime Number Example

```python
number = 17

for divisor in range(2, number):

    if number % divisor == 0:
        break

else:
    print("Prime")
```

---

# while-else

Example

```python
count = 1

while count <= 3:

    print(count)

    count += 1

else:

    print("Completed")
```

Output

```
1
2
3
Completed
```

---

# Retry Logic

```python
attempt = 1

while attempt <= 3:

    if connect():
        break

    attempt += 1

else:

    print("Connection Failed")
```

---

# Enterprise Examples

API Retry

Database Connection

Authentication Attempts

Queue Processing

Inventory Validation

---

# Best Practices

✔ Use loop `else` mainly for searching.

✔ Don't overuse it.

✔ Prefer readability over cleverness.

---

# Summary

Loop `else`

Runs only when

```
No break occurred
```

This makes it ideal for

- Searches
- Validation
- Retry logic