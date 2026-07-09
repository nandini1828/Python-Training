# Sorting and Grouping Data

Sorting and grouping are commonly used when analyzing data. Sorting arranges the data in a specific order, while grouping helps summarize data based on categories.

---

# Sorting Data

Use `sort_values()` to sort a DataFrame by one or more columns.

## Syntax

```python
df.sort_values(by="column_name")
```

### Sort in Ascending Order

```python
df.sort_values(by="Salary")
```

Ascending order is the default.

---

### Sort in Descending Order

```python
df.sort_values(by="Salary", ascending=False)
```

This displays the highest salary first.

---

### Sort by Multiple Columns

```python
df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
)
```

This sorts employees by department and then by salary in descending order.

---

# Grouping Data

Use `groupby()` to group rows that have the same value in a column.

## Syntax

```python
df.groupby("column_name")
```

Grouping is usually followed by an aggregation function like `sum()`, `mean()`, or `count()`.

---

### Average Salary by Department

```python
df.groupby("Department")["Salary"].mean()
```

---

### Total Salary by Department

```python
df.groupby("Department")["Salary"].sum()
```

---

### Count Employees in Each Department

```python
df.groupby("Department")["Name"].count()
```

---

### Maximum Salary

```python
df.groupby("Department")["Salary"].max()
```

---

### Minimum Salary

```python
df.groupby("Department")["Salary"].min()
```

---

# Common Aggregation Functions

| Function | Description |
|----------|-------------|
| `sum()` | Total value |
| `mean()` | Average value |
| `count()` | Number of records |
| `max()` | Maximum value |
| `min()` | Minimum value |

---

# Best Practices

- Sort data before presenting it.
- Use `groupby()` to summarize large datasets.
- Choose the correct aggregation function based on your analysis.

---

# Summary

| Method | Purpose |
|---------|----------|
| `sort_values()` | Sort rows |
| `groupby()` | Group similar records |
| `sum()` | Total values |
| `mean()` | Average |
| `count()` | Count records |
| `max()` | Maximum value |
| `min()` | Minimum value |