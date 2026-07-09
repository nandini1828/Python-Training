# Merge and Concat

Sometimes your data is spread across multiple DataFrames. Pandas provides `merge()` and `concat()` to combine them.

---

# Merge DataFrames

`merge()` combines two DataFrames based on a common column, similar to SQL joins.

## Syntax

```python
pd.merge(df1, df2, on="column_name")
```

---

## Example

### Employees

| ID | Name |
|----|------|
| 1 | Alice |
| 2 | Bob |

### Salaries

| ID | Salary |
|----|--------|
| 1 | 50000 |
| 2 | 70000 |

```python
merged_df = pd.merge(
    employees,
    salaries,
    on="ID"
)

print(merged_df)
```

### Output

| ID | Name | Salary |
|----|------|--------|
| 1 | Alice | 50000 |
| 2 | Bob | 70000 |

---

# Merge Types

Some common merge types are:

- `inner` (default)
- `left`
- `right`
- `outer`

Example:

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="left"
)
```

---

# Concatenate DataFrames

`concat()` joins DataFrames by stacking them vertically or horizontally.

## Syntax

```python
pd.concat([df1, df2])
```

---

## Vertical Concatenation

```python
combined = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Rows from `df2` are added below `df1`.

---

## Horizontal Concatenation

```python
combined = pd.concat(
    [df1, df2],
    axis=1
)
```

Columns from both DataFrames are combined.

---

# When to Use

Use **merge()** when both DataFrames have a common key.

Use **concat()** when you want to stack DataFrames together.

---

# Best Practices

- Ensure the key column exists before merging.
- Use `ignore_index=True` when concatenating rows.
- Check the shape of the resulting DataFrame after combining data.

---

# Summary

| Method | Purpose |
|---------|----------|
| `merge()` | Combine using a common key |
| `concat()` | Stack DataFrames |
| `how="left"` | Keep all rows from the left DataFrame |
| `axis=1` | Combine columns |