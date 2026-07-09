# Indexing and Selecting Data

## Introduction

Selecting rows and columns is one of the most common tasks in Pandas.

---

# Select Single Column

```python
df["salary"]
```

Returns

```
Series
```

---

# Select Multiple Columns

```python
df[
    ["name","salary"]
]
```

Returns

```
DataFrame
```

---

# loc

Label-based indexing.

Syntax

```python
df.loc[row_label, column_label]
```

Example

```python
df.loc[0]
```

Specific columns

```python
df.loc[:, ["name","salary"]]
```

Row slice

```python
df.loc[2:5]
```

---

# iloc

Position-based indexing.

```python
df.iloc[0]
```

Specific columns

```python
df.iloc[:,0]
```

Rows and columns

```python
df.iloc[1:5,0:3]
```

---

# at

Fast scalar lookup.

```python
df.at[0,"salary"]
```

---

# iat

Fast integer lookup.

```python
df.iat[0,2]
```

---

# Setting Values

```python
df.loc[0,"salary"]=70000
```

---

# Selecting Multiple Rows

```python
df.loc[[0,3,5]]
```

---

# Boolean Indexing

```python
df[df["salary"]>50000]
```

---

# Interview Questions

Difference between

- loc
- iloc
- at
- iat

When should iloc be preferred?

When should loc be used?