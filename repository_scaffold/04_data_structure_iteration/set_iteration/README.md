# Set Iteration

Sets store unique values and are optimized for membership checks and set
relationships.

This package covers:

- Iterating over a set.
- Union.
- Intersection.
- Difference.
- Subset checks.
- Adding an item without mutating the original set.
- Popping safely from a copied set.
- Creating a set from a list.

Example:

```python
from set_iteration import intersect_sets

common = intersect_sets({"python", "sql"}, {"python", "git"})
print(common)
```

Expected output:

```python
{"python"}
```

Important note: sets do not promise a meaningful business order. Sort the values
before displaying them if order matters to users or tests.
