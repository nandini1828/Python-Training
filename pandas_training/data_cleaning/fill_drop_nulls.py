"""
Examples of filling and dropping missing values.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees_missing.csv")


def fill_with_constant(df):
    print("\nFill Missing Values with 'Unknown'")
    print("-" * 60)

    new_df = df.fillna("Unknown")
    print(new_df)


def fill_salary_with_mean(df):
    print("\nFill Salary with Mean")
    print("-" * 60)

    new_df = df.copy()
    new_df["Salary"] = new_df["Salary"].fillna(
        new_df["Salary"].mean()
    )

    print(new_df)


def forward_fill(df):
    print("\nForward Fill")
    print("-" * 60)

    print(df.ffill())


def backward_fill(df):
    print("\nBackward Fill")
    print("-" * 60)

    print(df.bfill())


def drop_rows_with_nulls(df):
    print("\nDrop Rows Containing Null Values")
    print("-" * 60)

    print(df.dropna())


def main():
    df = load_data()

    fill_with_constant(df)
    fill_salary_with_mean(df)
    forward_fill(df)
    backward_fill(df)
    drop_rows_with_nulls(df)


if __name__ == "__main__":
    main()