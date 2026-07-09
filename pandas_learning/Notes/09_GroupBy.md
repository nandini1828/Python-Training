# GroupBy in Pandas

## Introduction

GroupBy is one of the most powerful features in Pandas. It allows you to split data into groups, perform calculations on each group, and combine the results.

The GroupBy operation follows the **Split → Apply → Combine** paradigm.

```
Original Data
      │
      ▼
Split into Groups
      │
      ▼
Apply Aggregation
      │
      ▼
Combined Result
```

---

# Syntax

```python
df.groupby("column")
```

Example

```python
import pandas as pd

df = pd.read_csv("datasets/employees.csv")

group = df.groupby("department")
```

---

# Sum

```python
df.groupby("department")["salary"].sum()
```

Output

```
department

Finance      153000
HR           110000
IT           372000
Marketing    116000
Sales        207000
```

---

# Mean

```python
df.groupby("department")["salary"].mean()
```

---

# Count

```python
df.groupby("department")["employee_id"].count()
```

---

# Maximum

```python
df.groupby("department")["salary"].max()
```

---

# Minimum

```python
df.groupby("department")["salary"].min()
```

---

# Multiple Aggregations

```python
df.groupby("department")["salary"].agg(
    ["min", "max", "mean", "sum", "count"]
)
```

---

# Group By Multiple Columns

```python
df.groupby(
    ["department", "city"]
)["salary"].mean()
```

---

# Aggregate Multiple Columns

```python
df.groupby("department").agg(
{
    "salary": "mean",
    "age": "max",
    "performance_rating": "mean"
}
)
```

---

# Reset Index

```python
grouped = (
    df.groupby("department")["salary"]
      .mean()
      .reset_index()
)
```

---

# Sort Grouped Result

```python
df.groupby("department")["salary"] \
    .mean() \
    .sort_values(ascending=False)
```

---

# Size vs Count

## size()

Counts every row.

```python
df.groupby("department").size()
```

---

## count()

Counts only non-null values.

```python
df.groupby("department").count()
```

---

# Practical Examples

Average salary by department

```python
df.groupby("department")["salary"].mean()
```

Highest paid employee per department

```python
df.groupby("department")["salary"].max()
```

Average performance rating

```python
df.groupby("department")["performance_rating"].mean()
```

---

# Common Mistakes

❌ Forgetting `reset_index()`

❌ Grouping by incorrect column names

❌ Mixing numeric and string columns in aggregations

---

# Best Practices

- Use meaningful aggregation names.
- Reset the index when further processing is needed.
- Prefer `.agg()` when multiple metrics are required.
- Chain operations for readability.

---

# Interview Questions

1. Explain the Split-Apply-Combine strategy.
2. Difference between `size()` and `count()`.
3. Difference between `agg()` and `apply()`.
4. Can GroupBy use multiple columns?
5. How do you calculate multiple statistics at once?