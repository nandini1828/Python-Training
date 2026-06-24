# List Methods

## Concept Overview
This package focuses on common list operations and transformations that appear in everyday Python code.

## Why It Exists
Lists are one of the most frequently used Python data structures, and reusable utilities make them easier to work with at scale.

## Real World Use Cases
- Data ingestion and batching
- Comparing sequences
- Computing aggregate statistics

## Example Code
```python
from list_methods.list_utils import chunk_list

chunks = chunk_list([1, 2, 3, 4], 2)
```

## Expected Output
A list of evenly sized sublists.
