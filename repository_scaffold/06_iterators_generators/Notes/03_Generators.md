# Generators

Generators let Python produce values one at a time.

Generator functions use `yield` instead of `return` for each produced value.

```python
def countdown(start):
    while start >= 0:
        yield start
        start -= 1
```

Each call to `next` resumes the function from where it paused.

Generators keep memory usage low because they do not build a complete list
unless the caller asks for one.
