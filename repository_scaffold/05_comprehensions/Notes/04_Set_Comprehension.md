# Set Comprehension

Build sets quickly using a comprehension syntax.

Example:

```python
words = ["Python", "python", "SQL"]
normalized = {word.lower() for word in words}
```

The result contains unique values only:

```python
{"python", "sql"}
```

Set comprehensions are useful for membership, uniqueness, and comparison tasks.
They are not useful when output order matters.
