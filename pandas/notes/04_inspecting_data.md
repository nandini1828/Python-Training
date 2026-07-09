# Inspecting Data

After loading a dataset, the first step is to understand its structure. Pandas provides several methods to quickly inspect your data.

---

# View the First Few Rows

Use `head()` to display the first 5 rows by default.

## Syntax

```python
df.head()
```

You can also specify the number of rows.

```python
df.head(10)
```

---

# View the Last Few Rows

Use `tail()` to display the last 5 rows.

```python
df.tail()
```

Example:

```python
df.tail(3)
```

---

# Check the Shape

Use `shape` to know the number of rows and columns.

```python
df.shape
```

Example Output:

```python
(100, 5)
```

This means:

- 100 rows
- 5 columns

---

# View Column Information

Use `info()` to get a summary of the DataFrame.

```python
df.info()
```

It shows:

- Number of rows
- Column names
- Data types
- Missing values
- Memory usage

---

# Get Statistical Summary

Use `describe()` to view statistics for numeric columns.

```python
df.describe()
```

It includes:

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

---

# Count Unique Values

Use `value_counts()` to count how many times each value appears.

```python
df["Department"].value_counts()
```

Example Output:

```
IT         10
HR          5
Finance     3
```

---

# View Unique Values

Use `unique()` to display all unique values in a column.

```python
df["Department"].unique()
```

Example Output:

```python
['HR', 'IT', 'Finance']
```

---

# Best Practices

- Always inspect the dataset before making changes.
- Use `head()` to quickly verify the data was loaded correctly.
- Use `info()` to check data types and missing values.

---

# Summary

| Method | Purpose |
|---------|----------|
| `head()` | View first rows |
| `tail()` | View last rows |
| `shape` | Number of rows and columns |
| `info()` | Dataset summary |
| `describe()` | Statistical summary |
| `value_counts()` | Count occurrences |
| `unique()` | Show unique values |