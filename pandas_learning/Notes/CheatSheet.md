# Pandas Cheat Sheet

## Import

```python
import pandas as pd
```

---

## Read Data

```python
pd.read_csv()

pd.read_excel()

pd.read_json()
```

---

## Save Data

```python
df.to_csv()

df.to_excel()
```

---

## Inspect

```python
df.head()

df.tail()

df.info()

df.describe()

df.shape

df.columns

df.dtypes

df.sample()
```

---

## Selection

```python
df["col"]

df[["col1", "col2"]]

df.loc[]

df.iloc[]

df.at[]

df.iat[]
```

---

## Filtering

```python
df[df["salary"] > 50000]

df.query()

df.isin()

df.between()
```

---

## Cleaning

```python
df.isnull()

df.notnull()

df.fillna()

df.dropna()

df.drop_duplicates()

df.replace()

df.rename()

df.astype()

df.reset_index()
```

---

## Sorting

```python
df.sort_values()

df.sort_index()
```

---

## Grouping

```python
df.groupby()

.sum()

.mean()

.max()

.min()

.count()

.agg()
```

---

## Merge & Concat

```python
pd.merge()

pd.concat()

df.join()
```

---

## String Operations

```python
.str.upper()

.str.lower()

.str.strip()

.str.contains()

.str.replace()

.str.split()
```

---

## DateTime

```python
pd.to_datetime()

.dt.year

.dt.month

.dt.day

.dt.hour

pd.date_range()
```

---

## Useful Functions

```python
apply()

map()

pivot()

pivot_table()

melt()

value_counts()

unique()

nunique()
```

---

# Pandas Workflow

```
Read Data
      │
      ▼
Inspect
      │
      ▼
Clean
      │
      ▼
Filter
      │
      ▼
Transform
      │
      ▼
Group
      │
      ▼
Merge
      │
      ▼
Analyze
      │
      ▼
Export
```

---

# Common Interview Methods

- head()
- info()
- describe()
- loc
- iloc
- groupby()
- merge()
- concat()
- pivot_table()
- apply()
- fillna()
- drop_duplicates()
- to_datetime()
