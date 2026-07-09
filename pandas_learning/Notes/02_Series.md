# Pandas Series

## What is a Series?

A Series is a one-dimensional labeled array.

Think of it as a single column in Excel.

---

## Creating a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30])
```

Output

```
0    10
1    20
2    30
```

---

## Custom Index

```python
s = pd.Series(
    [10,20,30],
    index=["A","B","C"]
)
```

---

## Access Elements

```python
s[0]

s["A"]
```

---

## Attributes

```python
s.index

s.values

s.dtype

s.shape
```

---

## Methods

```python
s.mean()

s.max()

s.min()

s.sum()

s.count()
```

---

## Vectorized Operations

```python
s + 10

s * 2

s / 5
```

---

## Advantages

- Fast
- Memory Efficient
- Supports labels

---

## Interview Questions

Difference between list and Series.

Difference between NumPy array and Series.