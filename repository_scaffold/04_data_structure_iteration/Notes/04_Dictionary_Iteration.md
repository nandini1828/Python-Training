# Dictionary Iteration

Use dictionary methods and loops to inspect key/value pairs.

The most common dictionary iteration methods are:

- `data.keys()` for keys.
- `data.values()` for values.
- `data.items()` for key/value pairs.

Example:

```python
prices = {"apple": 120, "banana": 40}

for fruit, price in prices.items():
    print(fruit, price)
```

Use `.items()` when both sides are needed. It avoids repeated lookups and makes
the loop intent clear.

Dictionaries preserve insertion order in modern Python, but code should still
avoid depending on dictionary order unless the insertion order is part of the
data contract.
