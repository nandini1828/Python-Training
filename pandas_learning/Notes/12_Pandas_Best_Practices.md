# Pandas Best Practices

## Introduction

Writing clean Pandas code improves readability, maintainability, and performance.

---

# 1. Use Meaningful Variable Names

Good

```python
employees_df
```

Bad

```python
x
```

---

# 2. Avoid Loops

Bad

```python
for row in df:
```

Good

Use vectorized operations.

```python
df["salary"] * 2
```

---

# 3. Chain Operations

Good

```python
(
    df
    .dropna()
    .sort_values("salary")
    .reset_index(drop=True)
)
```

---

# 4. Use loc Instead of Chained Indexing

Good

```python
df.loc[0, "salary"] = 60000
```

Bad

```python
df["salary"][0] = 60000
```

---

# 5. Handle Missing Values Early

```python
df.isnull().sum()
```

---

# 6. Validate Data Types

```python
df.dtypes
```

---

# 7. Avoid Duplicate Rows

```python
df.drop_duplicates()
```

---

# 8. Keep Functions Small

Instead of one huge script, write reusable functions.

---

# 9. Use Method Chaining

Readable

```python
(
    df
    .query("salary > 60000")
    .groupby("department")
    .mean()
)
```

---

# 10. Save Intermediate Results

Useful during debugging.

---

# Performance Tips

- Use categorical dtype for repeated strings.
- Avoid apply() if vectorized methods exist.
- Read only required columns.

Example

```python
pd.read_csv(
    "employees.csv",
    usecols=["salary", "department"]
)
```

---

# Common Mistakes

- Forgetting inplace behavior.
- Comparing strings instead of dates.
- Using loops instead of vectorization.
- Ignoring missing values.
- Forgetting reset_index().

---

# Interview Questions

1. Why avoid loops?
2. Why prefer vectorized operations?
3. Explain chained indexing.
4. What are Pandas best practices for large datasets?