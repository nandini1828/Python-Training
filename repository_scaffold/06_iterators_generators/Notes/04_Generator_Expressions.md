# Generator Expressions

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand generator expression syntax.
- Compare generator expressions with list comprehensions.
- Use generator expressions for lazy transformations.
- Pass generator expressions to functions like `sum`, `any`, and `all`.
- Understand generator exhaustion.
- Choose between list comprehensions and generator expressions.

---

# Introduction

A generator expression is a compact way to create a generator.

It looks similar to a list comprehension, but uses parentheses.

List comprehension:

```python
squares = [number * number for number in range(5)]
```

Generator expression:

```python
squares = (number * number for number in range(5))
```

The list comprehension creates all values immediately.

The generator expression creates values one at a time.

---

# Basic Syntax

```python
(expression for item in iterable)
```

Example

```python
numbers = [1, 2, 3]
squares = (number * number for number in numbers)

print(next(squares))
print(next(squares))
```

Output

```text
1
4
```

---

# Generator Expression Flow

```text
Generator expression created
        |
        v
No values produced yet
        |
        v
next() requested
        |
        v
Compute one value
        |
        v
Pause
```

---

# Filtering Values

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = (number for number in numbers if number % 2 == 0)

print(list(evens))
```

Output

```text
[2, 4, 6]
```

The filter works like it does in list comprehensions.

---

# Using with sum

Generator expressions are often passed directly to functions.

```python
total = sum(number * number for number in range(5))
```

Output

```text
30
```

No list is created.

This saves memory.

---

# Using with any and all

```python
scores = [82, 91, 77]

has_distinction = any(score >= 90 for score in scores)
all_passed = all(score >= 40 for score in scores)
```

`any` stops when it finds the first `True`.

`all` stops when it finds the first `False`.

This short-circuit behavior works well with generator expressions.

---

# Running Totals

Some lazy operations require a generator function instead of a generator
expression.

```python
def running_total(numbers):
    total = 0

    for number in numbers:
        total += number
        yield total
```

Usage

```python
print(list(running_total([2, 4, 6])))
```

Output

```text
[2, 6, 12]
```

Use generator functions when state must be updated across iterations.

---

# Generator Expression vs List Comprehension

| Feature | List Comprehension | Generator Expression |
|---|---|---|
| Brackets | `[]` | `()` |
| Evaluation | Immediate | Lazy |
| Memory | Stores all values | Produces one value at a time |
| Reusable | Yes | No, once exhausted |
| Good for | Small/needed lists | Streams and reductions |

---

# Real-World Example: Large File Check

```python
has_error = any(
    "ERROR" in line
    for line in log_file
)
```

Python can stop reading as soon as an error line is found.

This is more efficient than building a list of all checks.

---

# Common Mistakes

## Mistake 1: Expecting a list

```python
values = (x * x for x in range(3))
print(values)
```

This prints a generator object, not `[0, 1, 4]`.

Use `list(values)` only when all values are needed.

## Mistake 2: Reusing an exhausted generator

```python
values = (x for x in range(3))

print(list(values))
print(list(values))
```

Second output is empty.

## Mistake 3: Using generator expressions for complex state

If state must be updated step by step, use a generator function.

---

# Best Practices

- Use generator expressions for simple lazy transformations.
- Use them with `sum`, `any`, `all`, `min`, and `max`.
- Use list comprehensions when the result must be reused.
- Do not convert to a list unless necessary.
- Use generator functions for complex logic or state.

---

# Summary

Generator expressions are the lazy version of comprehensions.

They are excellent for streaming values into another operation and avoiding
unnecessary memory usage.
