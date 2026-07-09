"""
Examples of inspecting DataFrame structure.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def show_info(df):
    print("\nDataFrame Info")
    print("-" * 40)
    df.info()


def show_shape(df):
    print("\nShape")
    print("-" * 40)
    print(df.shape)


def show_columns(df):
    print("\nColumns")
    print("-" * 40)
    print(df.columns.tolist())


def show_index(df):
    print("\nIndex")
    print("-" * 40)
    print(df.index)


def show_dtypes(df):
    print("\nData Types")
    print("-" * 40)
    print(df.dtypes)


def main():
    df = load_data()

    show_info(df)
    show_shape(df)
    show_columns(df)
    show_index(df)
    show_dtypes(df)


if __name__ == "__main__":
    main()