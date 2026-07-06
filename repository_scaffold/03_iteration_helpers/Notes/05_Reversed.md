# reversed() in Python

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what `reversed()` does.
- Iterate over a sequence from end to beginning.
- Compare `reversed()` with slicing.
- Use `reversed()` with lists, tuples, strings, and ranges.
- Avoid assuming `reversed()` creates a list.

---

# Introduction

`reversed()` returns an iterator that produces values in reverse order.

Example

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

---

# Syntax

```python
reversed(sequence)
```

The object must support reverse iteration.

Common examples:

- List
- Tuple
- String
- Range

---

# Basic Example

```python
numbers = [10, 20, 30]
result = reversed(numbers)

print(list(result))
```

Output

```text
[30, 20, 10]
```

`reversed()` itself returns an iterator, so `list()` is used here only for display.

---

# Using reversed() with Strings

```python
text = "python"

for char in reversed(text):
    print(char)
```

Output

```text
n
o
h
t
y
p
```

To build a reversed string:

```python
reversed_text = "".join(reversed(text))
```

---

# reversed() vs Slicing

```python
values = [1, 2, 3]

copy_reverse = values[::-1]
iterator_reverse = reversed(values)
```

| Feature | Slicing `[::-1]` | `reversed()` |
|---|---|---|
| Return type | New list/string copy | Iterator |
| Memory use | Higher for large data | Lower |
| Good for | Reusable reversed copy | One-pass reverse iteration |

---

# Real-World Example: Recent Activity

```python
events = ["login", "view_product", "checkout"]

for event in reversed(events):
    print(event)
```

Output

```text
checkout
view_product
login
```

This pattern is useful when showing newest activity first.

---

# Common Mistakes

## Mistake 1: Expecting a list

```python
result = reversed([1, 2, 3])
print(result)
```

This prints a reverse iterator object.

Use:

```python
print(list(result))
```

## Mistake 2: Reusing the same reversed iterator

```python
result = reversed([1, 2, 3])

print(list(result))
print(list(result))
```

Second output is empty because the iterator is exhausted.

## Mistake 3: Using reversed() for sorting

`reversed()` changes traversal direction. It does not sort values.

Use `sorted(values, reverse=True)` for descending sort.

---

# Best Practices

- Use `reversed()` for one-pass reverse iteration.
- Use slicing when you need a reusable reversed copy.
- Use `"".join(reversed(text))` for reversed strings.
- Use `sorted(..., reverse=True)` when sorting is required.

---

# Summary

`reversed()` provides memory-efficient reverse iteration.

It is useful when values already have an order and you want to process them from
last to first.
