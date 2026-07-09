# Pandas Core Concepts & Commands

A simple, bulleted list of essential Pandas concepts and commands for quick reference.

## 1. Getting Started & Importing
* **Import Pandas:** `import pandas as pd` — The standard way to import the library.
* **Series:** `pd.Series([values])` — A single column of data (1D list).
* **DataFrame:** `pd.DataFrame({dict})` — A complete table of data (2D grid).
* **Read CSV:** `pd.read_csv("file.csv")` — Load data from a CSV file.
* **Save CSV:** `df.to_csv("file.csv", index=False)` — Save data to a CSV file.

## 2. Looking at Your Data
* **View Rows:** `df.head()` and `df.tail()` — Show the first or last few rows of the table.
* **Table Info:** `df.info()` — Check column names, data types, and missing values.
* **Table Shape:** `df.shape` — Get the number of rows and columns (e.g., `(100, 5)`).
* **Stats Summary:** `df.describe()` — Show basic statistics (mean, min, max, etc.) for numbers.
* **Value Counts:** `df["column"].value_counts()` — Count how many times each value appears.
* **Unique Values:** `df["column"].unique()` — List all the unique entries in a column.

## 3. Selecting & Filtering Data
* **Select Columns:** `df["column_name"]` or `df[["col1", "col2"]]` — Get specific columns.
* **Select by Label:** `df.loc[row_label, col_label]` — Get data using names/labels.
* **Select by Position:** `df.iloc[row_pos, col_pos]` — Get data using row/column index numbers.
* **Filter Rows:** `df[df["age"] > 25]` — Keep only rows that match a specific condition.
* **Multiple Filters:** `df[(df["age"] > 25) & (df["city"] == "NY")]` — Filter using AND (`&`) or OR (`|`).

## 4. Cleaning & Editing Data
* **Find Nulls:** `df.isnull().sum()` — Count how many missing/blank values are in each column.
* **Fill Nulls:** `df.fillna(value)` — Replace blank spaces/nulls with a default value.
* **Drop Nulls:** `df.dropna()` — Delete rows containing any empty cells.
* **Add/Edit Column:** `df["new_col"] = df["col1"] * 2` — Create a new column or modify an old one.
* **Change Data Type:** `df["col"].astype("float")` — Convert column data type (e.g., text to numbers).
* **Drop Columns/Rows:** `df.drop(columns=["col"])` or `df.drop(index=[0])` — Delete columns or rows.
* **Rename Columns:** `df.rename(columns={"old": "new"})` — Change the headers of the table.
* **Remove Duplicates:** `df.drop_duplicates()` — Find and delete identical rows.

## 5. Grouping, Sorting & Combining
* **Sort Rows:** `df.sort_values(by="col", ascending=False)` — Sort table by a column.
* **GroupBy:** `df.groupby("category")["value"].mean()` — Group items by category and find their average.
* **Merge (Join):** `pd.merge(df1, df2, on="key")` — Combine two tables using a matching key column.
* **Concat (Stack):** `pd.concat([df1, df2], axis=0)` — Stack one table on top of another.







 