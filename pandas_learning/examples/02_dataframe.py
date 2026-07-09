"""
02_dataframe.py

Learning Objectives

- Create DataFrames
- Inspect DataFrames
- Add columns
- Remove columns
- Select rows and columns
"""

from __future__ import annotations

import pandas as pd


def create_dataframe() -> pd.DataFrame:
    """Create a sample employee DataFrame."""

    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 28, 35],
        "Department": [
            "IT",
            "HR",
            "Finance",
            "Sales",
        ],
        "Salary": [
            60000,
            55000,
            70000,
            65000,
        ],
    }

    return pd.DataFrame(data)


def inspect_dataframe(df: pd.DataFrame) -> None:
    """Display DataFrame information."""

    print("\nDataFrame")
    print(df)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nStatistics")
    print(df.describe())


def modify_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Add and remove columns."""

    df["Bonus"] = df["Salary"] * 0.10

    print("\nAdded Bonus Column")
    print(df)

    df = df.drop(columns=["Bonus"])

    return df


def main() -> None:
    df = create_dataframe()

    inspect_dataframe(df)

    df = modify_dataframe(df)

    print("\nFinal DataFrame")
    print(df)


if __name__ == "__main__":
    main()