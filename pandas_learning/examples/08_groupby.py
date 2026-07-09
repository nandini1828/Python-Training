"""
08_groupby.py

Learning Objectives

- groupby()
- sum()
- mean()
- max()
- min()
- count()
- agg()
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATASET)


def salary_statistics(df: pd.DataFrame) -> None:
    print("\nAverage Salary By Department\n")

    print(
        df.groupby("department")["salary"].mean()
    )

    print("\nMaximum Salary\n")

    print(
        df.groupby("department")["salary"].max()
    )

    print("\nMinimum Salary\n")

    print(
        df.groupby("department")["salary"].min()
    )


def employee_count(df: pd.DataFrame) -> None:
    print("\nEmployee Count\n")

    print(
        df.groupby("department")[
            "employee_id"
        ].count()
    )


def multiple_aggregations(df: pd.DataFrame) -> None:
    print("\nMultiple Aggregations\n")

    result = (
        df.groupby("department")
        .agg(
            {
                "salary": [
                    "min",
                    "max",
                    "mean",
                    "sum",
                ],
                "age": [
                    "min",
                    "max",
                    "mean",
                ],
                "performance_rating": [
                    "mean",
                ],
            }
        )
    )

    print(result)


def multi_column_group(df: pd.DataFrame) -> None:
    print("\nDepartment and City\n")

    print(
        df.groupby(
            ["department", "city"]
        )["salary"].mean()
    )


def main() -> None:
    df = load_data()

    salary_statistics(df)

    employee_count(df)

    multiple_aggregations(df)

    multi_column_group(df)


if __name__ == "__main__":
    main()