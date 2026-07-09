"""
Examples of adding and modifying columns.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def add_bonus_column(df):
    print("\nAdd Bonus Column")
    print("-" * 60)

    new_df = df.copy()
    new_df["Bonus"] = new_df["Salary"] * 0.10

    print(new_df)


def add_total_salary(df):
    print("\nAdd Total Salary")
    print("-" * 60)

    new_df = df.copy()
    new_df["TotalSalary"] = new_df["Salary"] + (
        new_df["Salary"] * 0.10
    )

    print(new_df)


def modify_salary(df):
    print("\nIncrease Salary by 5%")
    print("-" * 60)

    new_df = df.copy()
    new_df["Salary"] = new_df["Salary"] * 1.05

    print(new_df)


def apply_lambda(df):
    print("\nExperience Category")
    print("-" * 60)

    new_df = df.copy()

    new_df["ExperienceLevel"] = new_df["Experience"].apply(
        lambda x: "Senior" if x >= 8 else "Junior"
    )

    print(new_df)


def main():
    df = load_data()

    add_bonus_column(df)
    add_total_salary(df)
    modify_salary(df)
    apply_lambda(df)


if __name__ == "__main__":
    main()