# List Comprehension

List comprehensions build lists from iterables.

Basic shape:

```python
[expression for item in iterable]
```

With filtering:

```python
[number for number in numbers if number % 2 == 0]
```

This package includes helpers for:

- Squaring numbers.
- Measuring word lengths.
- Filtering even numbers.
- Uppercasing words.
- Flattening nested rows.
- Combining words from two collections.
- Filtering short words.
- Splitting strings into characters.
- Creating indexed display labels.

Keep list comprehensions focused. If the expression needs several named
intermediate steps, a regular loop is usually easier to maintain.
