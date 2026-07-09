# Pandas Basics

## What is Pandas?
Pandas is a Python library used for working with structured/tabular data such as CSV files, Excel-like tables, and datasets used in analysis or preprocessing.

It provides two main data structures:
- **Series** → one-dimensional labeled data
- **DataFrame** → two-dimensional tabular data with rows and columns

---

# 1. Importing Pandas

```python
import pandas as pd
```

---

# 2. Series

A Series is a single column of data.

## Example
```python
import pandas as pd

marks = pd.Series([85, 90, 78], name="marks")
print(marks)
```

## Key points
- Has values
- Has an index
- Has a dtype

---

# 3. DataFrame

A DataFrame is a table of rows and columns.

## Example
```python
df = pd.DataFrame({
    "name": ["Karthik", "Rahul", "Ananya"],
    "salary": [65000, 52000, 48000]
})
print(df)
```

---

# 4. Reading and Writing CSV

## Read CSV
```python
df = pd.read_csv("employees.csv")
```

## Write CSV
```python
df.to_csv("output.csv", index=False)
```

### Why `index=False`?
Without it, Pandas writes the DataFrame index as an extra column in the CSV.

---

# 5. Basic DataFrame Inspection

## Shape
```python
df.shape
```
Returns:
```python
(rows, columns)
```

## Columns
```python
df.columns
```

## Index
```python
df.index
```

## Data types
```python
df.dtypes
```

---

# 6. Quick Preview Methods

## First rows
```python
df.head()
df.head(3)
```

## Last rows
```python
df.tail()
df.tail(2)
```

---

# 7. `info()` vs `describe()`

## `df.info()`
Used to inspect:
- column names
- non-null counts
- data types
- memory usage

```python
df.info()
```

## `df.describe()`
Used to inspect summary statistics for numeric columns:
- count
- mean
- std
- min
- max
- quartiles

```python
df.describe()
```

For text/object columns:
```python
df.describe(include="object")
```

---

# 8. `value_counts()`, `unique()`, `nunique()`

## Count category frequency
```python
df["department"].value_counts()
```

## Show unique values
```python
df["department"].unique()
```

## Count unique values
```python
df["department"].nunique()
```

---

# 9. Series vs DataFrame Selection

## Single column → Series
```python
df["salary"]
```

## Multiple columns → DataFrame
```python
df[["name", "salary"]]
```

---

# 10. Mental Model

When working with Pandas, always ask:
- Is this operation on a **Series** or a **DataFrame**?
- Am I selecting **rows** or **columns**?
- Am I **transforming** data or **summarizing** it?

---

# Quick Recap

## Core objects
- `pd.Series()`
- `pd.DataFrame()`

## File operations
- `pd.read_csv()`
- `df.to_csv()`

## Inspection
- `df.head()`
- `df.tail()`
- `df.shape`
- `df.columns`
- `df.dtypes`
- `df.info()`
- `df.describe()`

## Column summary
- `value_counts()`
- `unique()`
- `nunique()`