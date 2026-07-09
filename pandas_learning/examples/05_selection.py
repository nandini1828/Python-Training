"""
05_selection.py

Learning Objectives
-------------------
- Select single and multiple columns
- Select rows using loc and iloc
- Access scalar values using at and iat
- Slice rows and columns
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATASET)


def select_columns(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("SELECT SINGLE COLUMN")
    print("=" * 60)

    print(df["first_name"])

    print("\n" + "=" * 60)
    print("SELECT MULTIPLE COLUMNS")
    print("=" * 60)

    print(df[["first_name", "department", "salary"]])


def loc_examples(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("LOC EXAMPLES")
    print("=" * 60)

    print("\nFirst Row")
    print(df.loc[0])

    print("\nRows 2-5")
    print(df.loc[2:5])

    print("\nSpecific Columns")
    print(df.loc[:, ["first_name", "salary"]])

    print("\nSingle Cell")
    print(df.loc[0, "salary"])


def iloc_examples(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("ILOC EXAMPLES")
    print("=" * 60)

    print(df.iloc[0])

    print("\nRows 2-5")
    print(df.iloc[2:6])

    print("\nRows and Columns")
    print(df.iloc[1:5, 0:4])


def scalar_lookup(df: pd.DataFrame) -> None:
    print("\n" + "=" * 60)
    print("AT / IAT")
    print("=" * 60)

    print("Salary:", df.at[0, "salary"])

    print("Department:", df.iat[0, 3])


def main() -> None:
    df = load_data()

    select_columns(df)

    loc_examples(df)

    iloc_examples(df)

    scalar_lookup(df)


if __name__ == "__main__":
    main()