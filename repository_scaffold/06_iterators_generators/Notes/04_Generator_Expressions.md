# Generator Expressions

Generator expressions are short generator tools that look like comprehensions.

List comprehension:

```python
[number * number for number in range(5)]
```

Generator expression:

```python
(number * number for number in range(5))
```

The list comprehension builds all values immediately. The generator expression
produces each value only when requested.

Use generator expressions for streaming calculations:

```python
total = sum(number * number for number in range(1000))
```
