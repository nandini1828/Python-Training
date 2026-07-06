# List Iteration

Lists preserve insertion order, so looping over a list returns values in the same
sequence in which they are stored.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Use `enumerate` when the position matters:

```python
for index, value in enumerate(numbers):
    print(index, value)
```

Common list iteration tasks include:

- Filtering values.
- Transforming values.
- Searching for indexes.
- Summarizing values.
- Flattening nested lists.
- Removing duplicates while preserving order.

Avoid adding index variables manually unless there is a clear reason. Python's
iteration helpers are usually clearer and less error-prone.
