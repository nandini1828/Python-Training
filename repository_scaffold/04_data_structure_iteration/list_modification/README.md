# List Modification

List mutation is common, but changing a list in place can surprise callers when
the same list object is reused elsewhere.

The helpers in this package return modified copies. That keeps examples simple,
testable, and safe for beginners.

Covered operations:

- Append an item.
- Remove an item if it exists.
- Insert an item at an index.
- Pop the last item safely.
- Extend with another list.
- Replace matching values.
- Return an empty list.
- Return a sorted copy.
- Return unique values in first-seen order.

Example:

```python
from list_modification import append_item

numbers = [1, 2]
updated = append_item(numbers, 3)

print(numbers)
print(updated)
```

Expected output:

```python
[1, 2]
[1, 2, 3]
```
