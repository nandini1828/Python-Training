# Selecting and Filtering Data

Once a dataset is loaded, you'll often need to select specific rows or columns for analysis.

---

# Select a Single Column

Use the column name inside square brackets.

```python
df["Name"]
```

This returns a **Series**.

---

# Select Multiple Columns

Pass a list of column names.

```python
df[["Name", "Salary"]]
```

This returns a **DataFrame**.

---

# Select Rows Using `loc`

`loc` selects data using row and column labels.

## Syntax

```python
df.loc[row_label, column_label]
```

Example:

```python
df.loc[0]
```

Select specific columns:

```python
df.loc[:, ["Name", "Age"]]
```

---

# Select Rows Using `iloc`

`iloc` selects data using row and column positions.

## Syntax

```python
df.iloc[row_index, column_index]
```

Example:

```python
df.iloc[0]
```

Select the first two rows and first three columns.

```python
df.iloc[0:2, 0:3]
```

---

# Filter Rows

Display employees older than 30.

```python
df[df["Age"] > 30]
```

---

# Multiple Conditions

Use `&` for AND.

```python
df[
    (df["Age"] > 30) &
    (df["Department"] == "IT")
]
```

Use `|` for OR.

```python
df[
    (df["City"] == "New York") |
    (df["City"] == "Chicago")
]
```

---

# Best Practices

- Use `loc` when working with labels.
- Use `iloc` when working with positions.
- Wrap each condition in parentheses when using multiple filters.

---

# Summary

| Method | Purpose |
|---------|----------|
| `df["col"]` | Select one column |
| `df[["A","B"]]` | Select multiple columns |
| `loc` | Label-based selection |
| `iloc` | Position-based selection |
| `df[condition]` | Filter rows |