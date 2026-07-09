"""
12_project_analysis.py

Mini Project

Employee Data Analysis
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATASET)


def overview(df: pd.DataFrame) -> None:
    print("\nDataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nMissing Values")
    print(df.isnull().sum())


def salary_statistics(df: pd.DataFrame) -> None:
    print("\nAverage Salary")
    print(df["salary"].mean())

    print("\nHighest Salary")
    print(df["salary"].max())

    print("\nLowest Salary")
    print(df["salary"].min())


def department_analysis(df: pd.DataFrame) -> None:
    print("\nEmployees Per Department")

    print(
        df["department"].value_counts()
    )

    print("\nAverage Salary Per Department")

    print(
        df.groupby("department")["salary"].mean()
    )


def city_analysis(df: pd.DataFrame) -> None:
    print("\nEmployees Per City")

    print(
        df.groupby("city")["employee_id"]
        .count()
        .sort_values(ascending=False)
    )


def top_performers(df: pd.DataFrame) -> None:
    print("\nTop Five Salaries")

    print(
        df.nlargest(
            5,
            "salary",
        )[
            [
                "first_name",
                "department",
                "salary",
            ]
        ]
    )


def save_summary(df: pd.DataFrame) -> None:

    summary = (
        df.groupby("department")
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
            max_salary=("salary", "max"),
            average_rating=(
                "performance_rating",
                "mean",
            ),
        )
        .reset_index()
    )

    summary.to_csv(
        "datasets/department_summary.csv",
        index=False,
    )

    print(
        "\nSummary exported to department_summary.csv"
    )


def main() -> None:

    df = load_data()

    overview(df)

    salary_statistics(df)

    department_analysis(df)

    city_analysis(df)

    top_performers(df)

    save_summary(df)


if __name__ == "__main__":
    main()