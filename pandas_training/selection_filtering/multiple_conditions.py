"""
Examples of filtering with multiple conditions.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def and_condition(df):
    """Using & (AND)."""

    print("\nAge > 30 AND Salary > 60000")
    print("-" * 60)

    result = df[
        (df["Age"] > 30) &
        (df["Salary"] > 60000)
    ]

    print(result)


def or_condition(df):
    """Using | (OR)."""

    print("\nDepartment = HR OR Finance")
    print("-" * 60)

    result = df[
        (df["Department"] == "HR") |
        (df["Department"] == "Finance")
    ]

    print(result)


def not_condition(df):
    """Using ~ (NOT)."""

    print("\nEmployees NOT in IT Department")
    print("-" * 60)

    result = df[
        ~(df["Department"] == "IT")
    ]

    print(result)


def complex_condition(df):
    """Complex filtering."""

    print("\nIT Employees from Hyderabad with Salary > 45000")
    print("-" * 60)

    result = df[
        (df["Department"] == "IT") &
        (df["City"] == "Hyderabad") &
        (df["Salary"] > 45000)
    ]

    print(result)


def between_condition(df):
    """Using between()."""

    print("\nEmployees with Age Between 25 and 35")
    print("-" * 60)

    result = df[
        df["Age"].between(25, 35)
    ]

    print(result)


def isin_condition(df):
    """Using isin()."""

    print("\nEmployees from Hyderabad or Bangalore")
    print("-" * 60)

    result = df[
        df["City"].isin(["Hyderabad", "Bangalore"])
    ]

    print(result)


def main():
    df = load_data()

    and_condition(df)
    or_condition(df)
    not_condition(df)
    complex_condition(df)
    between_condition(df)
    isin_condition(df)


if __name__ == "__main__":
    main()