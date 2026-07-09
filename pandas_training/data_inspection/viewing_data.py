"""
Examples of viewing DataFrame records.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    """Load employees dataset."""

    return pd.read_csv(DATA_FOLDER / "employees.csv")


def show_head(df):
    """Display first 5 rows."""

    print("\nFirst 5 Rows")
    print("-" * 40)
    print(df.head())


def show_tail(df):
    """Display last 5 rows."""

    print("\nLast 5 Rows")
    print("-" * 40)
    print(df.tail())


def show_sample(df, rows=3):
    """Display random rows."""

    print(f"\nRandom {rows} Rows")
    print("-" * 40)
    print(df.sample(rows, random_state=42))


def main():
    df = load_data()

    show_head(df)
    show_tail(df)
    show_sample(df)


if __name__ == "__main__":
    main()