# List Modification Trap

Modifying a list while iterating can cause unexpected results.

Example:

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
```

This can skip values because the list changes while the loop is still tracking
positions.

Safer options:

- Build a new list with the values you want to keep.
- Iterate over a copy.
- Return a modified copy from a helper function.

Preferred style for this module:

```python
def remove_item(values, item):
    result = values.copy()
    if item in result:
        result.remove(item)
    return result
```

This keeps the caller's original list unchanged and makes tests easier to
reason about.
