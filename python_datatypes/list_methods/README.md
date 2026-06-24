# List Methods

## Concept Overview

This module demonstrates list utilities for safe pagination, de-duplication, and simple analytics.

## Why It Exists

Python lists are mutable sequences that often require deterministic filtering and paging behavior in enterprise systems.

## Real World Use Cases

- Paginating API results
- Normalizing event streams
- Preparing ordered, unique output lists for reports

## Example Code

```python
from python_datatypes.list_methods import unique_ordered, paginate_list

unique = unique_ordered([1, 2, 2, 3])
page = paginate_list([1, 2, 3, 4], page=1, page_size=2)
```

## Expected Output

```python
unique == [1, 2, 3]
page == [1, 2]
```
