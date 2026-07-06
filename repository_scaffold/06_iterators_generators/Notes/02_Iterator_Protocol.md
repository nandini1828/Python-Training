# Iterator Protocol

Learn how Python iteration works using __iter__ and __next__.

Python's `for` loop calls `iter` on the object, then repeatedly calls `next`
until `StopIteration` is raised.

Class outline:

```python
class Example:
    def __iter__(self):
        return self

    def __next__(self):
        ...
```

Important detail: iterators are usually stateful. If you call `next` manually,
the next loop starts from the updated state.
