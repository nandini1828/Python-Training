# Dictionary Comprehension

Create dictionaries from loops in one line.

Example:

```python
names = ["Asha", "Ravi"]
scores = [45, 40]

score_map = {name: score for name, score in zip(names, scores)}
```

Dictionary comprehensions are useful for:

- Transforming keys.
- Transforming values.
- Filtering key/value pairs.
- Creating lookup tables.

Be careful when the generated keys are not unique. Dictionaries keep one value
per key, so later values replace earlier values.
