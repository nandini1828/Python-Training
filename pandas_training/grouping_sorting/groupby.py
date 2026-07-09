"""
Examples of grouping and aggregation.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def average_salary(df):
    print("\nAverage Salary by Department")
    print("-" * 60)

    print(
        df.groupby("Department")["Salary"].mean()
    )


def total_salary(df):
    print("\nTotal Salary by Department")
    print("-" * 60)

    print(
        df.groupby("Department")["Salary"].sum()
    )


def employee_count(df):
    print("\nEmployee Count by Department")
    print("-" * 60)

    print(
        df.groupby("Department")["EmployeeID"].count()
    )


def maximum_salary(df):
    print("\nMaximum Salary by Department")
    print("-" * 60)

    print(
        df.groupby("Department")["Salary"].max()
    )


def multiple_aggregations(df):
    print("\nMultiple Aggregations")
    print("-" * 60)

    print(
        df.groupby("Department").agg(
            {
                "Salary": ["mean", "min", "max"],
                "Experience": ["mean", "max"],
            }
        )
    )


def main():
    df = load_data()

    average_salary(df)
    total_salary(df)
    employee_count(df)
    maximum_salary(df)
    multiple_aggregations(df)


if __name__ == "__main__":
    main()