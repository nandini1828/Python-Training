"""
Cleaning and Editing Data
"""

import pandas as pd


def run():

    df = pd.read_csv("data/employees.csv")

    print("\n========== DATA CLEANING ==========\n")

    print("Null Values")
    print(df.isnull().sum())

    print("\nFill Missing Age")

    filled = df.fillna({"age": 0})

    print(filled)

    print("\nDrop Null Rows")

    print(df.dropna())

    print("\nNew Column")

    df["bonus"] = df["salary"] * 0.10

    print(df)

    print("\nChange Data Type")

    df["age"] = df["age"].fillna(0).astype(float)

    print(df.dtypes)

    print("\nDrop Column")

    print(df.drop(columns=["bonus"]))

    print("\nRename Column")

    renamed = df.rename(columns={"salary": "monthly_salary"})

    print(renamed.head())

    print("\nRemove Duplicates")

    print(df.drop_duplicates())