"""
Examples of merging DataFrames.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    employees = pd.read_csv(DATA_FOLDER / "employees.csv")
    bonus = pd.read_csv(DATA_FOLDER / "department_bonus.csv")

    return employees, bonus


def inner_merge(emp, bonus):
    print("\nInner Merge")
    print("-" * 60)

    print(
        pd.merge(
            emp,
            bonus,
            on="Department",
            how="inner",
        )
    )


def left_merge(emp, bonus):
    print("\nLeft Merge")
    print("-" * 60)

    print(
        pd.merge(
            emp,
            bonus,
            on="Department",
            how="left",
        )
    )


def right_merge(emp, bonus):
    print("\nRight Merge")
    print("-" * 60)

    print(
        pd.merge(
            emp,
            bonus,
            on="Department",
            how="right",
        )
    )


def outer_merge(emp, bonus):
    print("\nOuter Merge")
    print("-" * 60)

    print(
        pd.merge(
            emp,
            bonus,
            on="Department",
            how="outer",
        )
    )


def main():
    employees, bonus = load_data()

    inner_merge(employees, bonus)
    left_merge(employees, bonus)
    right_merge(employees, bonus)
    outer_merge(employees, bonus)


if __name__ == "__main__":
    main()