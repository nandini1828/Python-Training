"""
09_sorting.py

Learning Objectives
-------------------
1. Sort rows using sort_values()
2. Sort by multiple columns
3. Sort index
4. Ranking
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    """Load employee dataset."""
    return pd.read_csv(DATASET)


def sort_salary(df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print("Salary Descending")
    print("=" * 70)

    print(
        df.sort_values(
            by="salary",
            ascending=False,
        )
    )


def sort_multiple_columns(df: pd.DataFrame) -> None:
    print("\n" + "=" * 70)
    print("Department + Salary")
    print("=" * 70)

    print(
        df.sort_values(
            by=["department", "salary"],
            ascending=[True, False],
        )
    )


def ranking(df: pd.DataFrame) -> None:
    df["salary_rank"] = df["salary"].rank(
        ascending=False,
        method="dense",
    )

    print("\nSalary Ranking")
    print(
        df[
            [
                "first_name",
                "salary",
                "salary_rank",
            ]
        ]
    )


def sort_index(df: pd.DataFrame) -> None:
    print("\nSorted Index")
    print(df.sort_index())


def main() -> None:
    df = load_data()

    sort_salary(df)

    sort_multiple_columns(df)

    ranking(df)

    sort_index(df)


if __name__ == "__main__":
    main()