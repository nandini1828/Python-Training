# Dictionary Iteration

Dictionaries store key/value pairs and are one of the most important data
structures in everyday Python programs.

This package demonstrates how to:

- Iterate through key/value pairs.
- Read keys and values separately.
- Merge dictionaries.
- Convert dictionaries into lists of tuples.
- Invert keys and values.
- Count item frequencies.
- Find values by key.

Example:

```python
from dictionary_iteration import iterate_dictionary

scores = {"math": 90, "science": 84}
print(iterate_dictionary(scores))
```

Expected output:

```python
[("math", 90), ("science", 84)]
```

Use `.items()` when both the key and value are needed. Use `.keys()` or
`.values()` only when the missing side of the pair is genuinely unnecessary.
