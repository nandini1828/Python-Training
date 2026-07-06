# Introduction

Comprehensions are expressions that build collections from iterables.

They combine three ideas:

- Where the data comes from.
- What each output value should look like.
- Which values should be included.

Example:

```python
squares = [number * number for number in range(5)]
```

This produces:

```python
[0, 1, 4, 9, 16]
```

Comprehensions are not automatically better than loops. They are better when
they make the transformation easier to read.
