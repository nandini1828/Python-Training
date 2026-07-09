"""
04_cleaning_editing.py

Topics Covered:
1. isnull()
2. fillna()
3. dropna()
4. Add/Edit Columns
5. astype()
6. drop()
7. rename()
8. drop_duplicates()
"""

import pandas as pd


def create_dataframe():
    """Create a sample DataFrame with missing and duplicate values."""
    return pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "Bob"],
        "Age": [25, None, 30, None],
        "Salary": [50000, 60000, None, 60000],
        "Department": ["HR", "IT", "Finance", "IT"]
    })


def isnull_demo():
    print("\n========== isnull() ==========")

    df = create_dataframe()

    print(df)
    print("\nMissing Values:")
    print(df.isnull().sum())


def fillna_demo():
    print("\n========== fillna() ==========")

    df = create_dataframe()

    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Salary"] = df["Salary"].fillna(0)

    print(df)


def dropna_demo():
    print("\n========== dropna() ==========")

    df = create_dataframe()

    print(df.dropna())


def add_edit_column_demo():
    print("\n========== Add/Edit Columns ==========")

    df = create_dataframe()

    df["Bonus"] = df["Salary"].fillna(0) * 0.10
    df["Department"] = df["Department"].str.upper()

    print(df)


def astype_demo():
    print("\n========== astype() ==========")

    df = create_dataframe()

    df["Age"] = df["Age"].fillna(0).astype(int)

    print(df)
    print("\nData Types:")
    print(df.dtypes)


def drop_demo():
    print("\n========== drop() ==========")

    df = create_dataframe()

    print("\nDrop Column:")
    print(df.drop(columns=["Department"]))

    print("\nDrop First Row:")
    print(df.drop(index=0))


def rename_demo():
    print("\n========== rename() ==========")

    df = create_dataframe()

    df = df.rename(columns={
        "Name": "Employee_Name",
        "Salary": "Monthly_Salary"
    })

    print(df)


def drop_duplicates_demo():
    print("\n========== drop_duplicates() ==========")

    df = create_dataframe()

    print("Before:")
    print(df)

    print("\nAfter:")
    print(df.drop_duplicates())


def run():
    isnull_demo()
    fillna_demo()
    dropna_demo()
    add_edit_column_demo()
    astype_demo()
    drop_demo()
    rename_demo()
    drop_duplicates_demo()


if __name__ == "__main__":
    run()