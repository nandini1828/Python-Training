# Intermediate Pandas

This section covers common transformation and analysis features such as `map`, `apply`, `lambda`, datetime handling, pivot tables, and crosstabs.

---

# 1. `map()`

Use `map()` mainly on a **Series** when replacing values using a dictionary or mapping.

## Example
```python
department_code_map = {
    "Engineering": "ENG",
    "Sales": "SAL",
    "HR": "HR",
    "Finance": "FIN"
}

df["department_code"] = df["department"].map(department_code_map)
```

---

# 2. `apply()`

Use `apply()` when you need custom logic for each value.

## Example
```python
def get_salary_band(salary):
    if salary >= 65000:
        return "High"
    if salary >= 50000:
        return "Medium"
    return "Low"

df["salary_band"] = df["salary"].apply(get_salary_band)
```

---

# 3. `lambda`

A lambda is a small anonymous function often used inside `apply()`.

## Example
```python
df["bonus_category"] = df["bonus_percent"].apply(
    lambda x: "High Bonus" if x >= 10 else "Standard Bonus"
)
```

---

# 4. Datetime Conversion

## Convert string to datetime
```python
df["joining_date"] = pd.to_datetime(df["joining_date"])
```

---

# 5. Extract Date Parts with `.dt`

## Year
```python
df["joining_year"] = df["joining_date"].dt.year
```

## Month
```python
df["joining_month"] = df["joining_date"].dt.month
```

## Day
```python
df["joining_day"] = df["joining_date"].dt.day
```

## Day name
```python
df["joining_day_name"] = df["joining_date"].dt.day_name()
```

---

# 6. Filtering by Date Parts

## Example
```python
df[df["joining_date"].dt.year == 2024]
```

---

# 7. Pivot Tables

Pivot tables summarize values into a matrix format.

## Example
```python
pd.pivot_table(
    df,
    values="revenue",
    index="category",
    columns="city",
    aggfunc="sum"
)
```

## Main arguments
- `values` → numeric column to aggregate
- `index` → row grouping
- `columns` → column grouping
- `aggfunc` → aggregation function

---

# 8. Crosstab

`pd.crosstab()` counts combinations between categorical columns.

## Example
```python
pd.crosstab(df["city"], df["section"])
```

This shows how many records belong to each city-section combination.

---

# 9. When to Use What

## `map()`
Use for direct value mapping.

## `apply()`
Use when logic is more custom.

## `lambda`
Use for small inline transformation logic.

## `pivot_table()`
Use for summary tables with aggregated numeric values.

## `crosstab()`
Use for counting combinations between categories.

---

# Quick Recap

## Transformation
- `map()`
- `apply()`
- `lambda`

## Datetime
- `pd.to_datetime()`
- `.dt.year`
- `.dt.month`
- `.dt.day`
- `.dt.day_name()`

## Summary tables
- `pd.pivot_table()`
- `pd.crosstab()`