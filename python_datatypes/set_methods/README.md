# Set Methods

## Concept Overview

This module provides set analysis utilities for intersections, symmetric differences, and statistics.

## Why It Exists

Sets are used in enterprise systems to evaluate membership, deduplicate values, and compare distinct collections.

## Real World Use Cases

- Finding common IDs between datasets
- Comparing feature flag sets
- Evaluating unique membership across distributed events

## Example Code

```python
from python_datatypes.set_methods import symmetric_difference, intersection_summary

result = symmetric_difference([1, 2], [2, 3])
```

## Expected Output

```python
result == {1, 3}
```
