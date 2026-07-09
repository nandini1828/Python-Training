"""
intermediate.py

Reference solutions for Intermediate Pandas Exercises.

Topics Covered
--------------
1. loc()
2. iloc()
3. Boolean Indexing
4. isin()
5. between()
6. query()
7. rename()
8. astype()
9. drop_duplicates()
10. replace()
11. groupby()
12. Multiple GroupBy
13. sort_values()
14. rank()

Run

python solutions/intermediate.py
"""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

# =============================================================================
# Configuration
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

DATASET = Path("datasets/employees.csv")


# =============================================================================
# Utility Functions
# =============================================================================


def print_header(title: str) -> None:
    """Print section header."""

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)


def load_dataset() -> pd.DataFrame:
    """Load employees dataset."""

    if not DATASET.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET}"
        )

    logger.info("Loading dataset...")

    return pd.read_csv(DATASET)


# =============================================================================
# Exercise 1
# =============================================================================


def exercise_1(df: pd.DataFrame) -> None:
    """
    Display rows 3–8 using loc.
    """

    print_header("Exercise 1 : loc()")

    print(df.loc[3:8])


# =============================================================================
# Exercise 2
# =============================================================================


def exercise_2(df: pd.DataFrame) -> None:
    """
    Display rows 5–10 and columns 2–6.
    """

    print_header("Exercise 2 : iloc()")

    print(df.iloc[5:11, 2:7])


# =============================================================================
# Exercise 3
# =============================================================================


def exercise_3(df: pd.DataFrame) -> None:
    """
    Employees where

    salary > 60000

    AND

    age < 30
    """

    print_header("Exercise 3 : Boolean Filtering")

    filtered = df[
        (df["salary"] > 60000)
        &
        (df["age"] < 30)
    ]

    print(filtered)


# =============================================================================
# Exercise 4
# =============================================================================


def exercise_4(df: pd.DataFrame) -> None:
    """
    Filter using isin().
    """

    print_header("Exercise 4 : isin()")

    result = df[
        df["department"].isin(
            [
                "IT",
                "Finance",
                "Marketing",
            ]
        )
    ]

    print(result)


# =============================================================================
# Exercise 5
# =============================================================================


def exercise_5(df: pd.DataFrame) -> None:
    """
    Salary between
    60000 and 90000.
    """

    print_header("Exercise 5 : between()")

    result = df[
        df["salary"].between(
            60000,
            90000,
        )
    ]

    print(result)


# =============================================================================
# Exercise 6
# =============================================================================


def exercise_6(df: pd.DataFrame) -> pd.DataFrame:
    """
    Query example.
    """

    print_header("Exercise 6 : query()")

    result = df.query(
        "salary > 70000"
    )

    print(result)

    return result


# =============================================================================
# Exercise 7
# =============================================================================


def exercise_7(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename salary column.
    """

    print_header("Exercise 7 : rename()")

    renamed = df.rename(
        columns={
            "salary": "annual_salary"
        }
    )

    print(renamed.head())

    return renamed


# =============================================================================
# Exercise 8
# =============================================================================


def exercise_8(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert salary datatype.
    """

    print_header("Exercise 8 : astype()")

    converted = df.copy()

    converted["salary"] = (
        converted["salary"]
        .astype(float)
    )

    print(converted.dtypes)

    return converted


# =============================================================================
# Exercise 9
# =============================================================================


def exercise_9(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """

    print_header("Exercise 9 : drop_duplicates()")

    before = len(df)

    cleaned = df.drop_duplicates()

    after = len(cleaned)

    print(f"Rows Before : {before}")
    print(f"Rows After  : {after}")

    return cleaned


# =============================================================================
# Exercise 10
# =============================================================================


def exercise_10(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace city names.
    """

    print_header("Exercise 10 : replace()")

    updated = df.copy()

    updated["city"] = (
        updated["city"]
        .replace(
            {
                "New York": "NY"
            }
        )
    )

    print(
        updated[
            [
                "first_name",
                "city",
            ]
        ].head()
    )

    return updated
# =============================================================================
# Exercise 11
# =============================================================================


def exercise_11(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by department and calculate
    average and maximum salary.
    """

    print_header("Exercise 11 : GroupBy Department")

    result = (
        df.groupby("department")
        .agg(
            average_salary=("salary", "mean"),
            maximum_salary=("salary", "max"),
        )
        .reset_index()
    )

    print(result)

    return result


# =============================================================================
# Exercise 12
# =============================================================================


def exercise_12(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by department and city.
    """

    print_header("Exercise 12 : Department + City")

    result = (
        df.groupby(
            [
                "department",
                "city",
            ]
        )
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
            average_age=("age", "mean"),
        )
        .reset_index()
        .sort_values(
            by=[
                "department",
                "city",
            ]
        )
    )

    print(result)

    return result


# =============================================================================
# Exercise 13
# =============================================================================


def exercise_13(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort by department and salary.
    """

    print_header("Exercise 13 : Sorting")

    result = df.sort_values(
        by=[
            "department",
            "salary",
        ],
        ascending=[
            True,
            False,
        ],
    )

    print(
        result[
            [
                "first_name",
                "department",
                "salary",
            ]
        ]
    )

    return result


# =============================================================================
# Exercise 14
# =============================================================================


def exercise_14(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create salary ranking.
    """

    print_header("Exercise 14 : Ranking")

    ranked = df.copy()

    ranked["salary_rank"] = ranked["salary"].rank(
        ascending=False,
        method="dense",
    )

    print(
        ranked[
            [
                "first_name",
                "salary",
                "salary_rank",
            ]
        ].sort_values(
            by="salary_rank"
        )
    )

    return ranked


# =============================================================================
# Summary
# =============================================================================


def summary(df: pd.DataFrame) -> None:
    """
    Display dataset summary.
    """

    print_header("Summary")

    print(f"Rows                : {len(df)}")
    print(f"Columns             : {len(df.columns)}")
    print(f"Departments         : {df['department'].nunique()}")
    print(f"Cities              : {df['city'].nunique()}")
    print(f"Average Salary      : {df['salary'].mean():,.2f}")
    print(f"Maximum Salary      : {df['salary'].max():,.2f}")
    print(f"Minimum Salary      : {df['salary'].min():,.2f}")


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    """
    Execute all intermediate exercises.
    """

    logger.info("Starting Intermediate Pandas Solutions")

    df = load_dataset()

    exercise_1(df)

    exercise_2(df)

    exercise_3(df)

    exercise_4(df)

    exercise_5(df)

    exercise_6(df)

    exercise_7(df)

    exercise_8(df)

    exercise_9(df)

    exercise_10(df)

    exercise_11(df)

    exercise_12(df)

    exercise_13(df)

    exercise_14(df)

    summary(df)

    logger.info("Completed Successfully")


if __name__ == "__main__":
    main()
# =============================================================================
# Exercise 11
# =============================================================================


def exercise_11(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by department and calculate
    average and maximum salary.
    """

    print_header("Exercise 11 : GroupBy Department")

    result = (
        df.groupby("department")
        .agg(
            average_salary=("salary", "mean"),
            maximum_salary=("salary", "max"),
        )
        .reset_index()
    )

    print(result)

    return result


# =============================================================================
# Exercise 12
# =============================================================================


def exercise_12(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by department and city.
    """

    print_header("Exercise 12 : Department + City")

    result = (
        df.groupby(
            [
                "department",
                "city",
            ]
        )
        .agg(
            employee_count=("employee_id", "count"),
            average_salary=("salary", "mean"),
            average_age=("age", "mean"),
        )
        .reset_index()
        .sort_values(
            by=[
                "department",
                "city",
            ]
        )
    )

    print(result)

    return result


# =============================================================================
# Exercise 13
# =============================================================================


def exercise_13(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort by department and salary.
    """

    print_header("Exercise 13 : Sorting")

    result = df.sort_values(
        by=[
            "department",
            "salary",
        ],
        ascending=[
            True,
            False,
        ],
    )

    print(
        result[
            [
                "first_name",
                "department",
                "salary",
            ]
        ]
    )

    return result


# =============================================================================
# Exercise 14
# =============================================================================


def exercise_14(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create salary ranking.
    """

    print_header("Exercise 14 : Ranking")

    ranked = df.copy()

    ranked["salary_rank"] = ranked["salary"].rank(
        ascending=False,
        method="dense",
    )

    print(
        ranked[
            [
                "first_name",
                "salary",
                "salary_rank",
            ]
        ].sort_values(
            by="salary_rank"
        )
    )

    return ranked


# =============================================================================
# Summary
# =============================================================================


def summary(df: pd.DataFrame) -> None:
    """
    Display dataset summary.
    """

    print_header("Summary")

    print(f"Rows                : {len(df)}")
    print(f"Columns             : {len(df.columns)}")
    print(f"Departments         : {df['department'].nunique()}")
    print(f"Cities              : {df['city'].nunique()}")
    print(f"Average Salary      : {df['salary'].mean():,.2f}")
    print(f"Maximum Salary      : {df['salary'].max():,.2f}")
    print(f"Minimum Salary      : {df['salary'].min():,.2f}")


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    """
    Execute all intermediate exercises.
    """

    logger.info("Starting Intermediate Pandas Solutions")

    df = load_dataset()

    exercise_1(df)

    exercise_2(df)

    exercise_3(df)

    exercise_4(df)

    exercise_5(df)

    exercise_6(df)

    exercise_7(df)

    exercise_8(df)

    exercise_9(df)

    exercise_10(df)

    exercise_11(df)

    exercise_12(df)

    exercise_13(df)

    exercise_14(df)

    summary(df)

    logger.info("Completed Successfully")


if __name__ == "__main__":
    main()    