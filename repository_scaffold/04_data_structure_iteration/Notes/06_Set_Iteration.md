# Set Iteration

Sets are unordered collections; learn how to read and combine them.

Sets are useful when uniqueness matters.

```python
tags = {"python", "testing", "python"}
print(tags)
```

The duplicate value appears only once.

Common set operations:

- `a | b` returns the union.
- `a & b` returns the intersection.
- `a - b` returns values in `a` but not in `b`.
- `a <= b` checks whether `a` is a subset of `b`.

Set iteration is fine for processing every value, but the order is not suitable
for user-facing output or strict list comparisons.

When order matters, convert to a sorted list:

```python
for tag in sorted(tags):
    print(tag)
```
