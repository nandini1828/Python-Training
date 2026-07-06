# List Comprehension

Build lists directly using a compact loop expression.

Example:

```python
words = ["python", "sql", "git"]
lengths = [len(word) for word in words]
```

Filtering goes after the loop:

```python
short_words = [word for word in words if len(word) <= 3]
```

Use list comprehensions when order and duplicates should be preserved.

Avoid packing too much logic into one expression. A readable loop is better than
a clever comprehension.
