# Merge and Concat in Pandas

## Introduction

Large datasets are often spread across multiple files or tables.

Pandas provides:

- merge()
- concat()
- join()

to combine data.

---

# Merge

Merge combines DataFrames using one or more common columns.

Syntax

```python
pd.merge(left, right, on="column")
```

---

## Inner Join

Returns matching rows only.

```python
pd.merge(
    employees,
    departments,
    on="department",
    how="inner"
)
```

---

## Left Join

Keeps all rows from left DataFrame.

```python
pd.merge(
    employees,
    departments,
    on="department",
    how="left"
)
```

---

## Right Join

```python
pd.merge(
    employees,
    departments,
    how="right",
    on="department"
)
```

---

## Outer Join

Returns every row.

```python
pd.merge(
    employees,
    departments,
    how="outer",
    on="department"
)
```

---

# Merge on Different Column Names

```python
pd.merge(
    df1,
    df2,
    left_on="emp_id",
    right_on="employee_id"
)
```

---

# Merge on Multiple Columns

```python
pd.merge(
    df1,
    df2,
    on=["department", "city"]
)
```

---

# Concat

Stacks DataFrames together.

```python
pd.concat([df1, df2])
```

---

## Row-wise

```python
pd.concat(
    [df1, df2],
    axis=0
)
```

---

## Column-wise

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

## Ignore Index

```python
pd.concat(
    [df1, df2],
    ignore_index=True
)
```

---

# Join

Join uses indexes.

```python
df1.join(df2)
```

---

# Merge vs Concat

| Merge | Concat |
|-------|--------|
| Uses keys | Stacks data |
| SQL-like | Appends data |
| Matches rows | No matching |

---

# Common Mistakes

❌ Wrong column names

❌ Duplicate key values

❌ Forgetting `how`

---

# Best Practices

- Always inspect keys before merging.
- Remove duplicate keys if necessary.
- Prefer explicit `how`.
- Validate row counts after merge.

---

# Interview Questions

1. Difference between Merge and Concat.
2. Difference between Join and Merge.
3. Explain Inner, Left, Right and Outer joins.
4. What happens if duplicate keys exist?
5. How do you merge on multiple columns?