# Dictionary Comprehension

Dictionary comprehensions build dictionaries from iterable data.

Basic shape:

```python
{key_expression: value_expression for item in iterable}
```

This package includes helpers for:

- Mapping numbers to their squares.
- Creating dictionaries from key and value lists.
- Uppercasing keys.
- Mapping strings to their lengths.
- Filtering dictionary items by value.
- Inverting dictionaries with unique values.
- Normalizing scores into percentages.

Dictionary comprehensions are best when the key and value rules are both easy to
see. If duplicate keys are produced, later values overwrite earlier ones.
