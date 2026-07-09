# Introduction to Pandas

## What is Pandas?

Pandas is an open-source Python library used for working with structured or tabular data.

It helps us:

- Read datasets
- Clean data
- Analyze data
- Filter records
- Perform calculations
- Save processed data

Think of Pandas as **Excel with Python**.

---

## Why Do We Use Pandas?

Without Pandas, processing large datasets requires writing many loops and functions.

With Pandas, most operations can be done using built-in methods.

For example,

Instead of writing a loop to calculate an average,

```python
average = df["Salary"].mean()
```

Pandas does it in one line.

---

## Installing Pandas

```bash
pip install pandas
```

---

## Importing Pandas

```python
import pandas as pd
```

`pd` is simply an alias for the pandas library.

---

## What Can Pandas Read?

- CSV files
- Excel files
- JSON files
- SQL Databases

---

## Main Data Structures

Pandas mainly provides two data structures.

### 1. Series

A one-dimensional collection of data.

Example:

```python
ages = pd.Series([20, 25, 30])
```

### 2. DataFrame

A two-dimensional table with rows and columns.

Example:

```python
students = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [20, 21]
})
```

---

## Where is Pandas Used?

- Data Science
- Machine Learning
- Business Analytics
- Finance
- Research
- Data Engineering

---

## Key Points

- Pandas is built on top of NumPy.
- DataFrame is the most commonly used data structure.
- Pandas makes working with datasets simple and efficient.