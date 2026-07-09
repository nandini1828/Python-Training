# Cleaning Data

Real-world datasets often contain missing values, duplicate records, or incorrect data. Data cleaning helps prepare the data for analysis.

---

# Check for Missing Values

Use `isnull()` to identify missing values.

```python
df.isnull()
```

To count missing values in each column:

```python
df.isnull().sum()
```

---

# Fill Missing Values

Replace missing values with a default value.

```python
df.fillna(0)
```

Example:

```python
df["Salary"] = df["Salary"].fillna(50000)
```

---

# Remove Missing Values

Delete rows containing missing values.

```python
df.dropna()
```

You can also remove columns with missing values.

```python
df.dropna(axis=1)
```

---

# Add or Modify a Column

Create a new column.

```python
df["Bonus"] = df["Salary"] * 0.10
```

Modify an existing column.

```python
df["Age"] = df["Age"] + 1
```

---

# Change Data Type

Convert a column to another data type.

```python
df["Salary"] = df["Salary"].astype(float)
```

---

# Rename Columns

```python
df.rename(
    columns={"Salary": "Annual Salary"}
)
```

To update the DataFrame directly:

```python
df.rename(
    columns={"Salary": "Annual Salary"},
    inplace=True
)
```

---

# Drop Columns

```python
df.drop(columns=["Department"])
```

Drop rows:

```python
df.drop(index=0)
```

---

# Remove Duplicate Rows

```python
df.drop_duplicates()
```

---

# Best Practices

- Check for missing values before analysis.
- Rename columns to make them meaningful.
- Avoid deleting data unless necessary.
- Create a backup before making major changes.

---

# Summary

| Method | Purpose |
|---------|----------|
| `isnull()` | Find missing values |
| `fillna()` | Fill missing values |
| `dropna()` | Remove missing values |
| `astype()` | Change data type |
| `rename()` | Rename columns |
| `drop()` | Remove rows or columns |
| `drop_duplicates()` | Remove duplicate records |