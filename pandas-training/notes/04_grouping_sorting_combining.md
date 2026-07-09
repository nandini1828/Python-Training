# Pandas Grouping, Sorting, and Combining

This section covers sorting, grouping with aggregation, merging DataFrames, and concatenating DataFrames.

---

# 1. Sorting Rows

## Sort ascending
```python
df.sort_values(by="salary")
```

## Sort descending
```python
df.sort_values(by="salary", ascending=False)
```

## Sort by multiple columns
```python
df.sort_values(by=["department", "salary"], ascending=[True, False])
```

---

# 2. GroupBy Basics

Grouping means splitting data into groups based on a category and then applying an aggregation.

## Example: average salary by department
```python
df.groupby("department")["salary"].mean()
```

## Example: count employees by city
```python
df.groupby("city")["employee_id"].count()
```

## Example: max salary by department
```python
df.groupby("department")["salary"].max()
```

---

# 3. Multiple Aggregations with `agg()`

```python
df.groupby("department").agg({
    "salary": ["mean", "max", "min"],
    "experience_years": ["mean", "max"],
    "employee_id": "count"
})
```

This is useful when you want several summary statistics at once.

---

# 4. Common Aggregation Functions

- `mean()`
- `sum()`
- `count()`
- `max()`
- `min()`
- `median()`

---

# 5. Merge DataFrames

Use `pd.merge()` when combining tables based on a common key.

## Syntax
```python
pd.merge(df1, df2, on="department_id", how="inner")
```

---

# 6. Types of Merge

## Inner join
Keeps only matching rows from both DataFrames.

```python
pd.merge(df1, df2, on="department_id", how="inner")
```

## Left join
Keeps all rows from the left DataFrame and matching rows from the right.

```python
pd.merge(df1, df2, on="department_id", how="left")
```

## Outer join
Keeps all rows from both DataFrames.

```python
pd.merge(df1, df2, on="department_id", how="outer")
```

---

# 7. Concatenation

Use `pd.concat()` when stacking DataFrames.

## Row-wise concat
```python
pd.concat([df1, df2], axis=0)
```

## Column-wise concat
```python
pd.concat([df1, df2], axis=1)
```

---

# 8. Merge vs Concat

## Merge
Use when:
- DataFrames share a common key
- you want SQL-like joins

## Concat
Use when:
- stacking rows of similar tables
- placing tables side by side

---

# 9. Practical Use Cases

## Sorting
- top salaries
- latest dates
- highest sales

## Grouping
- average salary by department
- sales by category
- student count by class

## Merge
- employees + departments
- orders + customers
- students + attendance table

## Concat
- combine monthly sales files
- combine multiple batches of the same dataset

---

# Quick Recap

## Sorting
- `sort_values()`

## Grouping
- `groupby()`
- `agg()`

## Combining
- `pd.merge()`
- `pd.concat()`