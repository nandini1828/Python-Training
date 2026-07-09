"""
Examples of finding and removing duplicate rows.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees_missing.csv")


def show_duplicates(df):
    print("\nDuplicate Rows")
    print("-" * 60)

    print(df[df.duplicated()])


def show_duplicate_mask(df):
    print("\nDuplicate Boolean Mask")
    print("-" * 60)

    print(df.duplicated())


def remove_duplicates(df):
    print("\nAfter Removing Duplicates")
    print("-" * 60)

    print(df.drop_duplicates())


def main():
    df = load_data()

    show_duplicates(df)
    show_duplicate_mask(df)
    remove_duplicates(df)


if __name__ == "__main__":
    main()