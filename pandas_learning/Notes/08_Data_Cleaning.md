# Data Cleaning

Real-world datasets are rarely clean. Pandas provides powerful tools to clean data.

---

# Detect Missing Values

```python
df.isnull()
```

Count Missing Values

```python
df.isnull().sum()
```

---

# notnull()

```python
df.notnull()
```

---

# Fill Missing Values

Replace nulls with zero.

```python
df.fillna(0)
```

Replace with mean.

```python
df["salary"].fillna(
    df["salary"].mean()
)
```

Forward Fill

```python
df.fillna(method="ffill")
```

Backward Fill

```python
df.fillna(method="bfill")
```

---

# Drop Missing Values

```python
df.dropna()
```

Drop Columns

```python
df.dropna(axis=1)
```

---

# Replace Values

```python
df.replace(
    "Unknown",
    "NA"
)
```

---

# Rename Columns

```python
df.rename(
    columns={
        "salary":"Salary"
    }
)
```

---

# Change Datatype

```python
df["salary"]=df["salary"].astype(float)
```

---

# Remove Duplicate Rows

```python
df.drop_duplicates()
```

---

# Reset Index

```python
df.reset_index(drop=True)
```

---

# Drop Columns

```python
df.drop(
    columns=["manager_id"]
)
```

---

# Drop Rows

```python
df.drop(index=[0])
```

---

# Interview Questions

Difference between

fillna()

and

dropna().

Why use astype()?

How do you remove duplicate rows?

How do you detect missing values?