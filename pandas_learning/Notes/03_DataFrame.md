# DataFrame

## What is a DataFrame?

A DataFrame is a two-dimensional table consisting of rows and columns.

It is the most commonly used data structure in Pandas.

---

## Create DataFrame

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob"],
    "Age": [25, 30],
    "City": ["New York", "Boston"]
}

df = pd.DataFrame(data)
```

---

## DataFrame Layout

```
Name    Age    City

Alice   25     NY

Bob     30     Boston
```

---

## Attributes

```python
df.shape

df.columns

df.index

df.dtypes

df.values
```

---

## Methods

```python
head()

tail()

describe()

info()
```

---

## Selecting Columns

```python
df["Age"]

df[["Name", "City"]]
```

---

## Adding Columns

```python
df["Salary"] = [50000, 60000]
```

---

## Deleting Columns

```python
df.drop(columns=["Salary"])
```

---

## Interview Questions

What is a DataFrame?

How is DataFrame different from Series?