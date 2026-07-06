# break, continue and pass

---

# Learning Objectives

After completing this chapter, you will understand:

- What `break` does
- What `continue` does
- What `pass` does
- When to use each statement
- Enterprise use cases
- Common mistakes

---

# Loop Control Statements

Python provides three statements that modify loop execution.

- break
- continue
- pass

---

# break Statement

The `break` statement immediately terminates the loop.

General Syntax

```python
for item in items:

    if condition:
        break
```

---

# Example

```python
numbers = [1, 3, 5, 8, 10]

for number in numbers:

    if number % 2 == 0:
        print(number)
        break
```

Output

```
8
```

The loop stops immediately after finding the first even number.

---

# How break Works

```
Loop

↓

Condition

↓

True

↓

break

↓

Loop Ends
```

---

# continue Statement

The `continue` statement skips the current iteration and moves to the next iteration.

Example

```python
numbers = [1, -2, 3, -4, 5]

for number in numbers:

    if number < 0:
        continue

    print(number)
```

Output

```
1
3
5
```

Negative numbers are skipped.

---

# How continue Works

```
Loop

↓

Condition

↓

True

↓

Skip Current Iteration

↓

Next Iteration
```

---

# pass Statement

The `pass` statement performs no operation.

It is used as a placeholder.

Example

```python
for _ in range(5):
    pass
```

The loop executes, but nothing happens.

---

# Why pass Exists

Sometimes you want to write the structure first.

```python
def process_orders():

    pass
```

You can implement the logic later.

---

# Enterprise Examples

## Searching

```python
for employee in employees:

    if employee.id == target:
        break
```

---

## Data Validation

```python
for score in scores:

    if score < 0:
        continue

    process(score)
```

---

## Future Development

```python
class PaymentGateway:

    pass
```

---

# Common Mistakes

Using `break` instead of `continue`

Incorrect

```python
for number in numbers:

    if number < 0:
        break
```

This stops processing completely.

Correct

```python
continue
```

---

# Best Practices

✔ Use `break` to stop searching.

✔ Use `continue` to skip invalid data.

✔ Use `pass` only as a temporary placeholder.

✔ Avoid unnecessary `break` statements.

---

# Summary

`break`

Stops the loop.

`continue`

Skips one iteration.

`pass`

Does nothing.