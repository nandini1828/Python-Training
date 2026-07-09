"""
Examples of selecting rows using loc and iloc.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def select_using_loc(df):
    """Select rows using labels."""

    print("\nloc -> First Employee")
    print("-" * 50)
    print(df.loc[0])

    print("\nloc -> Rows 2 to 5")
    print("-" * 50)
    print(df.loc[2:5])

    print("\nloc -> Name and Salary")
    print("-" * 50)
    print(df.loc[:, ["Name", "Salary"]])


def select_using_iloc(df):
    """Select rows using integer positions."""

    print("\niloc -> First Employee")
    print("-" * 50)
    print(df.iloc[0])

    print("\niloc -> First Five Rows")
    print("-" * 50)
    print(df.iloc[:5])

    print("\niloc -> Rows 2 to 6, Columns 1 to 4")
    print("-" * 50)
    print(df.iloc[2:7, 1:5])


def main():
    df = load_data()

    select_using_loc(df)
    select_using_iloc(df)


if __name__ == "__main__":
    main()