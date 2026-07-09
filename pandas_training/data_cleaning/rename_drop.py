"""
Examples of renaming and dropping rows/columns.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def rename_columns(df):
    print("\nRename Columns")
    print("-" * 60)

    new_df = df.rename(
        columns={
            "Salary": "MonthlySalary",
            "City": "Location",
        }
    )

    print(new_df.head())


def drop_column(df):
    print("\nDrop Experience Column")
    print("-" * 60)

    print(df.drop(columns=["Experience"]))


def drop_row(df):
    print("\nDrop First Row")
    print("-" * 60)

    print(df.drop(index=0))


def main():
    df = load_data()

    rename_columns(df)
    drop_column(df)
    drop_row(df)


if __name__ == "__main__":
    main()