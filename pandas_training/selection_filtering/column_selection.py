"""
Examples of selecting columns from a DataFrame.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    """Load employees dataset."""
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def select_single_column(df):
    """Select a single column."""

    print("\nSingle Column (Name)")
    print("-" * 50)
    print(df["Name"])


def select_multiple_columns(df):
    """Select multiple columns."""

    print("\nMultiple Columns (Name, Department, Salary)")
    print("-" * 50)
    print(df[["Name", "Department", "Salary"]])


def select_columns_using_list(df):
    """Select columns dynamically."""

    columns = ["EmployeeID", "Name", "City"]

    print("\nColumns using List")
    print("-" * 50)
    print(df[columns])


def main():
    df = load_data()

    select_single_column(df)
    select_multiple_columns(df)
    select_columns_using_list(df)


if __name__ == "__main__":
    main()