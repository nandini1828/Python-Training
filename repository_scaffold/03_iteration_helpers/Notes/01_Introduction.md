# Chapter 3: Introduction to Iteration Helpers

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand why Python provides iteration helper functions.
- Use helpers to make loops cleaner and safer.
- Choose between `range`, `enumerate`, `zip`, `reversed`, `sorted`, `any`, and `all`.
- Avoid manual counter and indexing mistakes.
- Write loops that are easier to read and test.

---

# Introduction

Iteration means processing values one by one.

Python allows basic loops:

```python
for item in values:
    print(item)
```

But real programs often need more than simple value iteration.

Examples:

- Repeat a task a fixed number of times.
- Track indexes while looping.
- Combine two lists together.
- Read values in reverse.
- Sort values before processing.
- Check whether any value passes a condition.
- Check whether all values pass a condition.

Python provides built-in **iteration helpers** for these patterns.

---

# Why Iteration Helpers Exist

Without helpers, loop code often becomes longer and more error-prone.

Manual counter example:

```python
index = 0
names = ["Asha", "Ravi", "Mira"]

for name in names:
    print(index, name)
    index += 1
```

Cleaner version:

```python
for index, name in enumerate(names):
    print(index, name)
```

The helper communicates intent directly.

---

# Main Iteration Helpers

| Helper | Purpose |
|---|---|
| `range()` | Generate integer sequences |
| `enumerate()` | Loop with index and value |
| `zip()` | Loop over multiple iterables together |
| `reversed()` | Iterate in reverse order |
| `sorted()` | Iterate over sorted values |
| `any()` | Check whether at least one value is true |
| `all()` | Check whether all values are true |

---

# range()

`range()` is used for numeric sequences.

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

Use it when the loop is based on numbers or repetition count.

---

# enumerate()

`enumerate()` is used when both index and value are needed.

```python
names = ["Asha", "Ravi"]

for index, name in enumerate(names):
    print(index, name)
```

Output

```text
0 Asha
1 Ravi
```

Use it instead of manually maintaining a counter.

---

# zip()

`zip()` combines related values from multiple iterables.

```python
names = ["Asha", "Ravi"]
marks = [92, 84]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output

```text
Asha 92
Ravi 84
```

Use it for parallel iteration.

---

# reversed()

`reversed()` iterates over values from the end to the beginning.

```python
values = [1, 2, 3]

for value in reversed(values):
    print(value)
```

Output

```text
3
2
1
```

Use it when reverse traversal is needed without manually managing indexes.

---

# sorted()

`sorted()` returns a new sorted list.

```python
numbers = [3, 1, 2]
result = sorted(numbers)
```

Output

```text
[1, 2, 3]
```

The original list is not modified.

---

# any() and all()

`any()` checks whether at least one value is true.

```python
scores = [35, 42, 28]
has_passed = any(score >= 40 for score in scores)
```

`all()` checks whether every value is true.

```python
all_passed = all(score >= 40 for score in scores)
```

These functions are useful for validations and checks.

---

# Real-World Example: Student Report

```python
names = ["Asha", "Ravi", "Mira"]
marks = [92, 84, 76]

for rank, (name, mark) in enumerate(zip(names, marks), start=1):
    print(rank, name, mark)
```

Output

```text
1 Asha 92
2 Ravi 84
3 Mira 76
```

This combines multiple helpers:

- `zip()` pairs names and marks.
- `enumerate()` adds numbering.

---

# Common Mistakes

## Mistake 1: Using indexes unnecessarily

Avoid:

```python
for index in range(len(values)):
    print(values[index])
```

Prefer:

```python
for value in values:
    print(value)
```

## Mistake 2: Reusing exhausted iterators

Helpers like `zip()` and `enumerate()` return iterators.

Once consumed, they may be empty.

## Mistake 3: Forgetting sorted() creates a new list

```python
numbers = [3, 1, 2]
sorted(numbers)
print(numbers)
```

The original list remains unchanged.

---

# Best Practices

- Use the helper that describes your loop's purpose.
- Prefer `enumerate()` over manual counters.
- Prefer `zip()` over parallel index lookup.
- Use `sorted()` when you need a sorted copy.
- Use `any()` and `all()` with generator expressions for efficient checks.
- Keep loop logic readable.

---

# Summary

Iteration helpers make Python loops clearer and safer.

They remove common manual patterns and replace them with readable built-in
tools. Learning them helps you write code that looks more like idiomatic Python.
