# List Iteration

Lists are ordered collections, which makes them ideal for examples where
position and sequence matter.

This package contains helpers for:

- Returning list items in order.
- Pairing each item with its index using `enumerate`.
- Finding all positions where a target appears.
- Filtering positive numbers.
- Transforming strings to uppercase.
- Summing numeric items.
- Flattening one level of nested lists.
- Removing duplicates while preserving first-seen order.
- Building a small summary of a list.

Example:

```python
from list_iteration import enumerate_list

print(enumerate_list(["red", "green"], start=1))
```

Expected output:

```python
[(1, "red"), (2, "green")]
```

Run the demo through the module entry point:

```bash
python3 repository_scaffold/04_data_structure_iteration/main.py
```
