# Inspecting Data in Pandas

## Introduction

Before cleaning or analyzing a dataset, it's important to understand its structure. Pandas provides several methods to quickly inspect your data.

---

## Load Dataset

```python
import pandas as pd

df = pd.read_csv("datasets/employees.csv")
```

---

# head()

Displays the first 5 rows.

```python
df.head()
```

Display first 10 rows.

```python
df.head(10)
```

---

# tail()

Displays the last rows.

```python
df.tail()

df.tail(3)
```

---

# shape

Returns

```
(rows, columns)
```

Example

```python
df.shape
```

Output

```
(15, 12)
```

---

# columns

Returns all column names.

```python
df.columns
```

---

# index

Returns row indexes.

```python
df.index
```

---

# dtypes

Shows datatype of every column.

```python
df.dtypes
```

Example Output

```
Age            int64
Salary         int64
Department     object
JoiningDate    object
```

---

# info()

One of the most important methods.

```python
df.info()
```

Shows

- Number of rows
- Number of columns
- Missing values
- Memory usage
- Datatypes

---

# describe()

Generates statistics.

```python
df.describe()
```

Returns

- Mean
- Median
- Standard Deviation
- Min
- Max
- Quartiles

---

# describe(include="object")

```python
df.describe(include="object")
```

Shows

- Count
- Unique
- Top
- Frequency

---

# value_counts()

Count occurrences.

```python
df["department"].value_counts()
```

Output

```
IT          5

Sales       3

Finance     2
```

---

# unique()

Returns unique values.

```python
df["department"].unique()
```

---

# nunique()

Number of unique values.

```python
df["department"].nunique()
```

---

# sample()

Random rows.

```python
df.sample(5)
```

---

# memory_usage()

```python
df.memory_usage()
```

---

# Interview Questions

### Difference between head() and sample()?

### Difference between unique() and value_counts()?

### Why use info() before analysis?

### What does describe() return?