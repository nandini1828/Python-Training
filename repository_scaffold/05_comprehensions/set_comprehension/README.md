# Set Comprehension

Set comprehensions build unique-value collections.

Basic shape:

```python
{expression for item in iterable}
```

This package includes helpers for:

- Creating unique uppercase values.
- Creating unique squares.
- Filtering even numbers.
- Extracting unique characters.
- Filtering longer words.
- Finding characters shared by two strings.

Use set comprehensions when uniqueness matters more than order. If display order
matters, convert the result with `sorted`.
