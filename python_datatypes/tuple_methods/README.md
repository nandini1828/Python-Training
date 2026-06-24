# Tuple Methods

## Concept Overview

This module includes tuple utilities for slicing, converting, and deriving basic statistics.

## Why It Exists

Tuples are immutable sequences used for fixed structural data such as coordinates, configuration tuples, and event records.

## Real World Use Cases

- Converting tuple data to lists for JSON serialization
- Creating subviews for algorithm inputs
- Measuring tuple cardinality in analytics workflows

## Example Code

```python
from python_datatypes.tuple_methods import tuple_to_list, tuple_slice

converted = tuple_to_list((1, 2, 3))
slice_result = tuple_slice((1, 2, 3), 0, 2)
```

## Expected Output

```python
converted == [1, 2, 3]
slice_result == (1, 2)
```
