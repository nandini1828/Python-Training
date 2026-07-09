# Filtering Data

Filtering extracts rows matching one or more conditions.

---

# Equal

```python
df[df["department"]=="IT"]
```

---

# Greater Than

```python
df[df["salary"]>60000]
```

---

# Less Than

```python
df[df["age"]<30]
```

---

# Multiple Conditions

AND

```python
df[
    (df["salary"]>60000)
    &
    (df["department"]=="IT")
]
```

---

OR

```python
df[
    (df["salary"]>60000)
    |
    (df["department"]=="HR")
]
```

---

NOT

```python
df[
    ~(df["department"]=="HR")
]
```

---

# isin()

```python
df[
    df["department"].isin(
        ["IT","Finance"]
    )
]
```

---

# between()

```python
df[
    df["salary"].between(
        50000,
        80000
    )
]
```

---

# query()

```python
df.query(
    "salary>60000"
)
```

Multiple

```python
df.query(
    "salary>60000 and department=='IT'"
)
```

---

# String Filtering

```python
df[
    df["city"].str.contains("York")
]
```

---

# Interview Questions

Difference between

query()

and

Boolean indexing.

Difference between

isin()

and

==.