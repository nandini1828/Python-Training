"""
Examples of detecting missing values.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees_missing.csv")


def show_missing_values(df):
    print("\nMissing Values (True = Missing)")
    print("-" * 60)
    print(df.isnull())


def show_not_missing(df):
    print("\nNot Missing Values (True = Available)")
    print("-" * 60)
    print(df.notnull())


def count_missing_values(df):
    print("\nMissing Values Count")
    print("-" * 60)
    print(df.isnull().sum())


def total_missing_values(df):
    print("\nTotal Missing Values")
    print("-" * 60)
    print(df.isnull().sum().sum())


def main():
    df = load_data()

    show_missing_values(df)
    show_not_missing(df)
    count_missing_values(df)
    total_missing_values(df)


if __name__ == "__main__":
    main()