"""
07_cleaning.py

Learning Objectives

- Missing Values
- fillna()
- dropna()
- replace()
- astype()
- rename()
- drop_duplicates()
"""

from __future__ import annotations

import pandas as pd


def create_dirty_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Name": [
                "Alice",
                "Bob",
                "Bob",
                None,
                "David",
            ],
            "Age": [
                25,
                None,
                None,
                40,
                28,
            ],
            "Salary": [
                60000,
                50000,
                50000,
                None,
                70000,
            ],
        }
    )


def inspect(df: pd.DataFrame) -> None:
    print("\nMissing Values\n")
    print(df.isnull().sum())


def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    df["Age"] = df["Age"].fillna(df["Age"].mean())

    df["Salary"] = df["Salary"].fillna(0)

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(
        columns={
            "Name": "Employee Name",
            "Salary": "Annual Salary",
        }
    )


def convert_dtype(df: pd.DataFrame) -> pd.DataFrame:
    df["Age"] = df["Age"].astype(int)

    return df


def main() -> None:
    df = create_dirty_dataframe()

    print("\nOriginal Data\n")
    print(df)

    inspect(df)

    df = fill_missing(df)

    df = remove_duplicates(df)

    df = rename_columns(df)

    df = convert_dtype(df)

    print("\nCleaned Data\n")
    print(df)


if __name__ == "__main__":
    main()