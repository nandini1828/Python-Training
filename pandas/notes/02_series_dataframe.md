# Series and DataFrame

Before working with data in Pandas, it's important to understand its two main data structures:

1. **Series** (1D)
2. **DataFrame** (2D)

Almost everything you do in Pandas revolves around these two structures.

---

# What is a Series?

A **Series** is a one-dimensional labeled array that stores a single column of data.

Think of it as one column in an Excel sheet.

## Syntax

```python
pd.Series(data)
```

## Example

```python
import pandas as pd

ages = pd.Series([20, 25, 30, 35])

print(ages)
```

### Output

```
0    20
1    25
2    30
3    35
dtype: int64
```

The numbers on the left (`0, 1, 2, 3`) are called the **index**.

---

# Creating a Series

## From a List

```python
import pandas as pd

numbers = pd.Series([10, 20, 30, 40])

print(numbers)
```

---

## From a Dictionary

```python
marks = pd.Series({
    "Math": 95,
    "Science": 90,
    "English": 88
})

print(marks)
```

### Output

```
Math       95
Science    90
English    88
dtype: int64
```

Notice that the dictionary keys become the **index**.

---

## Accessing Values in a Series

```python
ages = pd.Series([20, 25, 30])

print(ages[0])
print(ages[2])
```

### Output

```
20
30
```

---

# Common Series Operations

## Find Maximum Value

```python
ages.max()
```

---

## Find Minimum Value

```python
ages.min()
```

---

## Find Average

```python
ages.mean()
```

---

## Find Sum

```python
ages.sum()
```

---

## Check Data Type

```python
ages.dtype
```

---

# What is a DataFrame?

A **DataFrame** is a two-dimensional table made up of rows and columns.

Think of it like an Excel spreadsheet or a database table.

This is the most commonly used data structure in Pandas.

---

# Creating a DataFrame

## From a Dictionary

```python
import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 22],
    "City": ["New York", "Chicago", "Boston"]
}

df = pd.DataFrame(students)

print(df)
```

### Output

```
      Name  Age      City
0    Alice   20  New York
1      Bob   21   Chicago
2  Charlie   22    Boston
```

Each key becomes a **column**.

Each list becomes the values for that column.

---

# Creating a DataFrame from a List of Dictionaries

```python
employees = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30}
]

df = pd.DataFrame(employees)

print(df)
```

---

# Creating a DataFrame from a CSV File

```python
df = pd.read_csv("employees.csv")
```

We'll learn more about this in the next chapter.

---

# Understanding Rows and Columns

Consider this DataFrame:

| Name | Age | City |
|------|-----|------|
| Alice | 20 | New York |
| Bob | 21 | Chicago |
| Charlie | 22 | Boston |

Rows represent individual records.

Columns represent attributes of those records.

For example:

- **Name** is a column.
- **Age** is a column.
- **Alice** is a row value.

---

# Accessing Columns

```python
df["Name"]
```

Output

```
0      Alice
1        Bob
2    Charlie
```

Notice that selecting one column returns a **Series**.

---

# Accessing Multiple Columns

```python
df[["Name", "Age"]]
```

Output

```
      Name  Age
0    Alice   20
1      Bob   21
2  Charlie   22
```

Selecting multiple columns returns a **DataFrame**.

---

# Series vs DataFrame

| Feature | Series | DataFrame |
|---------|---------|-----------|
| Dimensions | One | Two |
| Looks Like | Single column | Complete table |
| Can Have Multiple Columns? | No | Yes |
| Commonly Used | Less | Very Often |

---

# When Should You Use a Series?

Use a Series when you're working with a single column.

Example:

```python
ages = df["Age"]
```

---

# When Should You Use a DataFrame?

Use a DataFrame when working with complete datasets.

Example:

```python
employees = pd.read_csv("employees.csv")
```

Almost all real-world datasets are DataFrames.

---

# Best Practices

✔ Give meaningful variable names.

```python
employee_df
```

instead of

```python
x
```

---

✔ Keep column names simple.

Good:

```
EmployeeName
Salary
Department
```

Avoid:

```
Employee Name
Salary($)
Department#
```

---

✔ Store related data together.

Example:

| Name | Age | City |
|------|-----|------|

instead of creating separate Series for every column.

---

# Common Mistakes

### Mistake 1

Forgetting to import Pandas.

```python
import pandas as pd
```

---

### Mistake 2

Creating columns with different lengths.

❌ Incorrect

```python
pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [20]
})
```

This will raise an error because every column must have the same number of values.

---

### Mistake 3

Confusing Series and DataFrame.

```python
df["Age"]
```

returns a **Series**.

```python
df[["Age"]]
```

returns a **DataFrame**.

---

# Summary

- A **Series** is a one-dimensional data structure.
- A **DataFrame** is a two-dimensional table.
- A DataFrame is made up of multiple Series.
- Most real-world datasets are stored as DataFrames.
- Selecting one column returns a Series.
- Selecting multiple columns returns a DataFrame.

---

# Key Points

- **Series = One-dimensional**
- **DataFrame = Two-dimensional**
- **Series stores one column**
- **DataFrame stores multiple columns**
- **DataFrame is the most commonly used Pandas data structure**