# Dictionary Methods

## Concept Overview

This module contains reusable dictionary helpers for merging, filtering, and flattening nested maps.

## Why It Exists

Enterprise code often requires safe dictionary transformation utilities that preserve structure and support schema-driven lookup.

## Real World Use Cases

- Merging configuration maps
- Filtering API payload fields
- Flattening nested JSON for analytics pipelines

## Example Code

```python
from python_datatypes.dictionary_methods import merge_dictionary, filter_dictionary, flatten_dictionary

base = {"id": 1, "attributes": {"region": "us-east"}}
override = {"active": True}
merged = merge_dictionary(base, override)
```

## Expected Output

```python
{"id": 1, "attributes": {"region": "us-east"}, "active": True}
```
