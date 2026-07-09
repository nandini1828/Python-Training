# Reading and Writing CSV Files

Most real-world datasets are stored in **CSV (Comma-Separated Values)** files. Pandas makes it easy to read data from a CSV file, work with it, and save the modified data back to a CSV.

---

# What is a CSV File?

A CSV file stores data in rows and columns, where each value is separated by a comma.

Example (`employees.csv`):

```csv
Name,Age,Department,Salary
Alice,25,HR,50000
Bob,30,IT,70000
Charlie,28,Finance,65000
```

Each row represents a record, and each column represents a specific attribute.

---

# Reading a CSV File

To load a CSV file into a Pandas DataFrame, use the `read_csv()` function.

## Syntax

```python
pd.read_csv("file_name.csv")
```

## Example

```python
import pandas as pd

df = pd.read_csv("employees.csv")

print(df)
```

This reads the CSV file and stores the data in a DataFrame.

---

# Common Parameters

### Read Specific Number of Rows

```python
df = pd.read_csv("employees.csv", nrows=3)
```

Reads only the first 3 rows.

---

### Read Selected Columns

```python
df = pd.read_csv(
    "employees.csv",
    usecols=["Name", "Salary"]
)
```

Only the specified columns are loaded.

---

### Skip Rows

```python
df = pd.read_csv(
    "employees.csv",
    skiprows=2
)
```

Skips the first two rows while reading the file.

---

### Use a Different Delimiter

If the values are separated by a semicolon (`;`) instead of a comma:

```python
df = pd.read_csv(
    "employees.csv",
    sep=";"
)
```

---

# Saving a DataFrame

After making changes to a DataFrame, you can save it as a new CSV file.

## Syntax

```python
df.to_csv("output.csv")
```

---

## Save Without Index

By default, Pandas also saves the index column.

To avoid this:

```python
df.to_csv(
    "output.csv",
    index=False
)
```

This is the most commonly used way of saving a CSV.

---

# Example

```python
import pandas as pd

df = pd.read_csv("employees.csv")

df["Bonus"] = df["Salary"] * 0.10

df.to_csv("updated_employees.csv", index=False)
```

This creates a new column called **Bonus** and saves the updated data.

---

# Best Practices

- Keep your data files in a separate `data/` folder.
- Always check the data after loading it using `df.head()` or `df.info()`.
- Use `index=False` when saving CSV files unless you specifically need the index.

---

# Common Mistakes

### Incorrect File Path

```python
pd.read_csv("employee.csv")
```

If the file doesn't exist or the path is incorrect, Pandas raises a `FileNotFoundError`.

---

### Forgetting `index=False`

```python
df.to_csv("output.csv")
```

This adds an extra index column to the CSV.

Preferred:

```python
df.to_csv("output.csv", index=False)
```

---

# Summary

- A CSV file stores data in rows and columns.
- Use `pd.read_csv()` to load a CSV file.
- Use `df.to_csv()` to save a DataFrame.
- Use `index=False` to prevent saving the index column.
- `usecols`, `nrows`, `skiprows`, and `sep` are commonly used parameters.

---

# Key Points

- `pd.read_csv()` → Read a CSV file.
- `df.to_csv()` → Save a DataFrame to a CSV.
- `index=False` → Prevents writing the index column.
- `usecols` → Reads selected columns.
- `nrows` → Reads a limited number of rows.