"""
06_filtering.py

Learning Objectives

- Boolean Indexing
- Multiple Conditions
- isin()
- between()
- query()
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATASET)


def basic_filters(df: pd.DataFrame) -> None:
    print("\nEmployees Older Than 30\n")
    print(df[df["age"] > 30])

    print("\nSalary Greater Than 70000\n")
    print(df[df["salary"] > 70000])


def multiple_conditions(df: pd.DataFrame) -> None:
    print("\nIT Employees With Salary > 70000\n")

    result = df[
        (df["department"] == "IT")
        & (df["salary"] > 70000)
    ]

    print(result)


def isin_example(df: pd.DataFrame) -> None:
    print("\nDepartments IT and Finance\n")

    print(
        df[
            df["department"].isin(
                ["IT", "Finance"]
            )
        ]
    )


def between_example(df: pd.DataFrame) -> None:
    print("\nSalary Between 60000 and 80000\n")

    print(
        df[
            df["salary"].between(
                60000,
                80000,
            )
        ]
    )


def query_example(df: pd.DataFrame) -> None:
    print("\nQuery Example\n")

    print(
        df.query(
            "salary > 60000 and age < 35"
        )
    )


def main() -> None:
    df = load_data()

    basic_filters(df)

    multiple_conditions(df)

    isin_example(df)

    between_example(df)

    query_example(df)


if __name__ == "__main__":
    main()