"""
Examples of sorting DataFrames.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def sort_by_salary_ascending(df):
    print("\nSort by Salary (Ascending)")
    print("-" * 60)
    print(df.sort_values(by="Salary"))


def sort_by_salary_descending(df):
    print("\nSort by Salary (Descending)")
    print("-" * 60)
    print(df.sort_values(by="Salary", ascending=False))


def sort_by_multiple_columns(df):
    print("\nSort by Department and Salary")
    print("-" * 60)

    print(
        df.sort_values(
            by=["Department", "Salary"],
            ascending=[True, False]
        )
    )


def sort_by_index(df):
    print("\nSort by Index")
    print("-" * 60)

    shuffled = df.sample(frac=1, random_state=42)

    print("Shuffled DataFrame")
    print(shuffled)

    print("\nSorted by Index")
    print(shuffled.sort_index())


def main():
    df = load_data()

    sort_by_salary_ascending(df)
    sort_by_salary_descending(df)
    sort_by_multiple_columns(df)
    sort_by_index(df)


if __name__ == "__main__":
    main()