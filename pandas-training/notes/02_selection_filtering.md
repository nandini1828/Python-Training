# Pandas Selection and Filtering

This section covers how to select columns, access rows, and filter data based on conditions.

---

# 1. Selecting Columns

## Single column
```python
df["name"]
```
Returns a **Series**.

## Multiple columns
```python
df[["name", "salary"]]
```
Returns a **DataFrame**.

---

# 2. `loc[]` — Label-based selection

Use `loc` when selecting by row label and column name.

## Syntax
```python
df.loc[row_label, column_label]
```

## Examples
```python
df.loc[0]
df.loc[0, "name"]
df.loc[0:3, ["name", "salary"]]
```

---

# 3. `iloc[]` — Position-based selection

Use `iloc` when selecting by row/column number positions.

## Syntax
```python
df.iloc[row_position, column_position]
```

## Examples
```python
df.iloc[0]
df.iloc[0, 1]
df.iloc[0:4, 0:3]
```

---

# 4. `loc` vs `iloc`

## `loc`
- uses labels / names
- row label + column name

```python
df.loc[0, "salary"]
```

## `iloc`
- uses integer positions
- row index position + column position

```python
df.iloc[0, 2]
```

---

# 5. Filtering Rows

Filtering means keeping only rows that match a condition.

## Example
```python
df[df["salary"] > 60000]
```

## More examples
```python
df[df["city"] == "Hyderabad"]
df[df["experience_years"] >= 4]
```

---

# 6. Multiple Conditions

## AND condition
```python
df[(df["city"] == "Hyderabad") & (df["salary"] > 60000)]
```

## OR condition
```python
df[(df["city"] == "Hyderabad") | (df["city"] == "Chennai")]
```

---

# 7. Important Pandas Filtering Rules

## Use `&` instead of `and`
Wrong:
```python
df[df["salary"] > 60000 and df["city"] == "Hyderabad"]
```

Correct:
```python
df[(df["salary"] > 60000) & (df["city"] == "Hyderabad")]
```

## Use `|` instead of `or`
Wrong:
```python
df[df["city"] == "Hyderabad" or df["city"] == "Chennai"]
```

Correct:
```python
df[(df["city"] == "Hyderabad") | (df["city"] == "Chennai")]
```

## Put each condition in parentheses
Correct:
```python
df[(df["salary"] > 50000) & (df["experience_years"] >= 3)]
```

---

# 8. Common Selection Patterns

## Select subset of columns after filtering
```python
df[df["salary"] > 60000][["name", "salary"]]
```

## Filter first, then use `loc`
```python
df.loc[df["salary"] > 60000, ["name", "salary"]]
```

---

# Quick Recap

## Column selection
- `df["col"]`
- `df[["col1", "col2"]]`

## Row/column access
- `df.loc[]`
- `df.iloc[]`

## Filtering
- `df[df["col"] > value]`
- `&` for AND
- `|` for OR