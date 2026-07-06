# Introduction

This note explains iterators and generators in simple terms.

An iterable is something Python can loop over.

An iterator is the object that remembers where the loop currently is.

```python
values = iter([1, 2, 3])

print(next(values))
print(next(values))
```

Generators are a convenient way to create iterators without writing a full class.

```python
def numbers():
    yield 1
    yield 2
```

Lazy iteration is useful because Python does not need to create every value
before work can begin.
