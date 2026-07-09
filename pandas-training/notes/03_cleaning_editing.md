# Pandas Cleaning and Editing

This section covers how to detect missing data, clean it, modify columns, rename/drop columns, and remove duplicates.

---

# 1. Missing Values

## Find missing values
```python
df.isnull()
df.isnull().sum()
```

`isnull()` gives True/False for every cell.  
`isnull().sum()` gives the null count per column.

---

# 2. Fill Missing Values

## Fill one column
```python
df["city"] = df["city"].fillna("Unknown")
```

## Fill numeric column
```python
df["salary"] = df["salary"].fillna(0)
```

---

# 3. Drop Missing Values

## Drop rows with any null value
```python
df.dropna()
```

## Drop rows only if specific column is null
```python
df.dropna(subset=["salary"])
```

---

# 4. Add New Columns

## Example
```python
df["bonus_amount"] = df["salary"] * df["bonus_percent"] / 100
```

## Another example
```python
df["total_compensation"] = df["salary"] + df["bonus_amount"]
```

---

# 5. Edit Existing Columns

## Example
```python
df["salary"] = df["salary"] * 1.10
```

---

# 6. Change Data Types

## Check dtypes
```python
df.dtypes
```

## Convert numeric type
```python
df["salary"] = df["salary"].astype("float")
```

## Convert to datetime
```python
df["joining_date"] = pd.to_datetime(df["joining_date"])
```

---

# 7. Drop Columns / Rows

## Drop columns
```python
df.drop(columns=["email"])
```

## Drop rows by index
```python
df.drop(index=[0, 1])
```

---

# 8. Rename Columns

## Example
```python
df.rename(columns={"salary": "monthly_salary"})
```

If you want to keep the result:
```python
df = df.rename(columns={"salary": "monthly_salary"})
```

---

# 9. Duplicates

## Check duplicates
```python
df.duplicated()
```

## Count duplicate rows
```python
df.duplicated().sum()
```

## Remove duplicates
```python
df.drop_duplicates()
```

---

# 10. String Cleaning with `.str`

## Lowercase
```python
df["name"].str.lower()
```

## Uppercase
```python
df["department"].str.upper()
```

## Replace text
```python
df["city"].str.replace("Hyderabad", "HYD")
```

## Contains pattern
```python
df["email"].str.contains("@company.com")
```

---

# 11. Good Cleaning Habits

## Work on a copy when experimenting
```python
clean_df = df.copy()
```

## Check nulls before analysis
```python
df.isnull().sum()
```

## Check duplicates before reporting
```python
df.duplicated().sum()
```

---

# Quick Recap

## Null handling
- `isnull()`
- `fillna()`
- `dropna()`

## Column editing
- `df["new_col"] = ...`
- `astype()`
- `to_datetime()`

## Structural cleanup
- `drop()`
- `rename()`
- `drop_duplicates()`

## Text cleanup
- `.str.lower()`
- `.str.upper()`
- `.str.replace()`
- `.str.contains()`