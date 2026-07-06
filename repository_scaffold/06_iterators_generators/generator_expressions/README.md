# Generator Expressions

Generator expressions look like comprehensions, but they produce values lazily.

Example:

```python
squares = (number * number for number in range(5))
```

This package includes lazy helpers for:

- Squaring numbers.
- Filtering even numbers.
- Yielding characters.
- Yielding word lengths.
- Producing running totals.

Use generator expressions when you need to stream values into another operation,
such as `sum`, `any`, `all`, or a `for` loop.
