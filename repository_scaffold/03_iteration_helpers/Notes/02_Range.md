# range() in Python

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what `range()` produces.
- Use `range(stop)`, `range(start, stop)`, and `range(start, stop, step)`.
- Use `range()` in `for` loops.
- Understand why the stop value is excluded.
- Use positive and negative step values.
- Avoid common off-by-one mistakes.

---

# Introduction

`range()` is a built-in Python function used to produce a sequence of integers.

It is most commonly used with `for` loops.

Example

```python
for number in range(5):
    print(number)
```

Output

```text
0
1
2
3
4
```

Notice that `5` is not included.

---

# Why range() Exists

Many loops need to run a fixed number of times.

Examples:

- Print numbers from 1 to 10.
- Repeat a task 5 times.
- Generate indexes.
- Build test data.
- Create numeric sequences.

Instead of manually creating a list of numbers, Python uses `range()`.

---

# Syntax

`range()` has three common forms.

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

| Form | Meaning |
|---|---|
| `range(stop)` | Start at 0, stop before `stop` |
| `range(start, stop)` | Start at `start`, stop before `stop` |
| `range(start, stop, step)` | Move by `step` each time |

---

# range(stop)

```python
for number in range(4):
    print(number)
```

Output

```text
0
1
2
3
```

The sequence starts at `0` by default.

---

# range(start, stop)

```python
for number in range(2, 6):
    print(number)
```

Output

```text
2
3
4
5
```

The start value is included.

The stop value is excluded.

---

# range(start, stop, step)

```python
for number in range(2, 11, 2):
    print(number)
```

Output

```text
2
4
6
8
10
```

The step controls how much the value changes each time.

---

# Negative Step

Use a negative step to count backward.

```python
for number in range(5, 0, -1):
    print(number)
```

Output

```text
5
4
3
2
1
```

The stop value is still excluded.

---

# range() is Lazy

`range()` does not create a full list immediately.

```python
numbers = range(1_000_000)
```

This is memory efficient because Python stores the rule for producing numbers,
not every number as a separate list element.

Convert to a list only when needed:

```python
print(list(range(5)))
```

Output

```text
[0, 1, 2, 3, 4]
```

---

# Real-World Example: Repeating a Task

```python
for attempt in range(1, 4):
    print(f"Login attempt {attempt}")
```

Output

```text
Login attempt 1
Login attempt 2
Login attempt 3
```

---

# Real-World Example: Index-Based Access

Direct iteration is usually better, but indexes are sometimes needed.

```python
students = ["Asha", "Ravi", "Mira"]

for index in range(len(students)):
    print(index, students[index])
```

Output

```text
0 Asha
1 Ravi
2 Mira
```

When both index and value are needed, `enumerate()` is usually cleaner.

---

# Common Mistakes

## Mistake 1: Expecting stop to be included

```python
range(1, 5)
```

Produces:

```text
1, 2, 3, 4
```

Not `5`.

## Mistake 2: Using step 0

```python
range(1, 10, 0)
```

This raises `ValueError`.

## Mistake 3: Using range when direct iteration is clearer

Avoid:

```python
for index in range(len(names)):
    print(names[index])
```

Prefer:

```python
for name in names:
    print(name)
```

---

# Best Practices

- Use `range()` for numeric sequences.
- Remember that the stop value is excluded.
- Use negative steps for countdowns.
- Use `enumerate()` when you need both index and value.
- Avoid converting large ranges to lists unless necessary.

---

# Summary

`range()` creates efficient integer sequences for loops.

It is simple, memory-friendly, and especially useful when code needs to repeat a
known number of times.
