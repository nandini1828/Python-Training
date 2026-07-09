"""
11_concat.py

Learning Objectives
-------------------
1. Row Concatenation
2. Column Concatenation
3. ignore_index
"""

from __future__ import annotations

import pandas as pd


def create_dataframes():

    df1 = pd.DataFrame(
        {
            "Name": ["Alice", "Bob"],
            "Salary": [60000, 70000],
        }
    )

    df2 = pd.DataFrame(
        {
            "Name": ["Charlie", "David"],
            "Salary": [65000, 72000],
        }
    )

    return df1, df2


def concatenate_rows(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
) -> None:

    result = pd.concat(
        [df1, df2],
        ignore_index=True,
    )

    print("\nRow Concatenation")
    print(result)


def concatenate_columns(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
) -> None:

    result = pd.concat(
        [df1, df2],
        axis=1,
    )

    print("\nColumn Concatenation")
    print(result)


def main() -> None:
    df1, df2 = create_dataframes()

    concatenate_rows(df1, df2)

    concatenate_columns(df1, df2)


if __name__ == "__main__":
    main()