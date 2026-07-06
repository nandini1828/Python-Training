# Iterator Protocol

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the iterator protocol.
- Implement `__iter__` and `__next__`.
- Explain how `StopIteration` ends iteration.
- Build a custom iterator class.
- Understand iterator state and exhaustion.
- Use `iter` and `next` manually.

---

# Introduction

The iterator protocol is the rule that allows Python objects to work with
`for` loops.

Any object that follows this protocol can be traversed one value at a time.

The protocol uses two methods:

- `__iter__`
- `__next__`

---

# The Two Required Methods

## `__iter__`

Returns an iterator object.

```python
def __iter__(self):
    return self
```

## `__next__`

Returns the next value.

Raises `StopIteration` when no values remain.

```python
def __next__(self):
    if no_values_left:
        raise StopIteration
    return next_value
```

---

# Custom Iterator Example

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value
```

Usage

```python
for number in CountDown(3):
    print(number)
```

Output

```text
3
2
1
0
```

---

# How Python Uses the Iterator

```text
for number in CountDown(3)
        |
        v
iter(CountDown(3))
        |
        v
__iter__()
        |
        v
next(iterator)
        |
        v
__next__()
        |
        v
value or StopIteration
```

---

# Manual Iteration

```python
counter = CountDown(2)
iterator = iter(counter)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output

```text
2
1
0
```

Calling `next` again raises `StopIteration`.

---

# Iterator State

Iterators remember where they are.

```python
counter = CountDown(3)

print(next(counter))
print(list(counter))
```

Output

```text
3
[2, 1, 0]
```

The first value was already consumed.

---

# Iterable Check

The safest way to check whether something is iterable is to call `iter`.

```python
def is_iterable(value):
    try:
        iter(value)
    except TypeError:
        return False

    return True
```

This is better than only checking for an attribute because Python's iteration
rules can be more flexible.

---

# Real-World Example: Reading Batches

Custom iterators can represent:

- Database cursor rows
- Paginated API results
- Sensor readings
- Log events
- Generated report rows

The caller can use a simple `for` loop without knowing how values are fetched.

---

# Common Mistakes

## Mistake 1: Forgetting to raise StopIteration

Without `StopIteration`, iteration may never end.

## Mistake 2: Returning a new iterator incorrectly

For iterator objects, `__iter__` usually returns `self`.

## Mistake 3: Reusing an exhausted iterator

Once an iterator is exhausted, it does not automatically restart.

---

# Best Practices

- Use iterator classes when explicit state is needed.
- Validate constructor inputs.
- Keep `__next__` small and predictable.
- Raise `StopIteration` when values are finished.
- Use generator functions when a class would be unnecessary.

---

# Summary

The iterator protocol explains how Python loops work internally.

By implementing `__iter__` and `__next__`, custom objects can produce values one
at a time and behave naturally in `for` loops.
