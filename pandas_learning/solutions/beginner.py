"""
beginner.py

Reference solutions for Beginner Pandas Exercises.

Author: Sagar Nunugonda
Project: Pandas Learning Repository

Run:

    python solutions/beginner.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

DATASET = Path("datasets/employees.csv")
OUTPUT_FILE = Path("datasets/employees_copy.csv")


# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------


def print_title(title: str) -> None:
    """Print a formatted section title."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def load_dataset() -> pd.DataFrame:
    """
    Load employees dataset.

    Returns
    -------
    pd.DataFrame
        Employee dataset.
    """
    if not DATASET.exists():
        raise FileNotFoundError(f"{DATASET} not found.")

    return pd.read_csv(DATASET)


# -----------------------------------------------------------------------------
# Exercise 1
# -----------------------------------------------------------------------------


def exercise_1() -> pd.DataFrame:
    """Create a DataFrame manually."""

    print_title("Exercise 1 - Create DataFrame")

    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 28],
    }

    df = pd.DataFrame(data)

    print(df)

    return df


# -----------------------------------------------------------------------------
# Exercise 2
# -----------------------------------------------------------------------------


def exercise_2(df: pd.DataFrame) -> None:
    """Display first and last five rows."""

    print_title("Exercise 2 - Head & Tail")

    print("Head\n")
    print(df.head())

    print("\nTail\n")
    print(df.tail())


# -----------------------------------------------------------------------------
# Exercise 3
# -----------------------------------------------------------------------------


def exercise_3(df: pd.DataFrame) -> None:
    """Display DataFrame information."""

    print_title("Exercise 3 - Inspect Dataset")

    print("Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nInfo")
    df.info()


# -----------------------------------------------------------------------------
# Exercise 4
# -----------------------------------------------------------------------------


def exercise_4(df: pd.DataFrame) -> None:
    """Display salary column."""

    print_title("Exercise 4 - Salary Column")

    print(df["salary"])


# -----------------------------------------------------------------------------
# Exercise 5
# -----------------------------------------------------------------------------


def exercise_5(df: pd.DataFrame) -> None:
    """Display selected columns."""

    print_title("Exercise 5 - Multiple Columns")

    print(
        df[
            [
                "first_name",
                "department",
                "salary",
            ]
        ]
    )


# -----------------------------------------------------------------------------
# Exercise 6
# -----------------------------------------------------------------------------


def exercise_6(df: pd.DataFrame) -> None:
    """Salary greater than 70000."""

    print_title("Exercise 6 - Salary > 70000")

    print(df[df["salary"] > 70000])


# -----------------------------------------------------------------------------
# Exercise 7
# -----------------------------------------------------------------------------


def exercise_7(df: pd.DataFrame) -> None:
    """Employees from IT."""

    print_title("Exercise 7 - IT Employees")

    print(
        df[
            df["department"] == "IT"
        ]
    )


# -----------------------------------------------------------------------------
# Exercise 8
# -----------------------------------------------------------------------------


def exercise_8(df: pd.DataFrame) -> None:
    """Employees older than 30."""

    print_title("Exercise 8 - Age > 30")

    print(
        df[
            df["age"] > 30
        ]
    )


# -----------------------------------------------------------------------------
# Exercise 9
# -----------------------------------------------------------------------------


def exercise_9(df: pd.DataFrame) -> None:
    """Sort salary descending."""

    print_title("Exercise 9 - Salary Descending")

    print(
        df.sort_values(
            by="salary",
            ascending=False,
        )
    )


# -----------------------------------------------------------------------------
# Exercise 10
# -----------------------------------------------------------------------------


def exercise_10(df: pd.DataFrame) -> None:
    """Salary statistics."""

    print_title("Exercise 10 - Salary Statistics")

    print("Highest Salary :", df["salary"].max())
    print("Lowest Salary  :", df["salary"].min())
    print("Average Salary :", df["salary"].mean())


# -----------------------------------------------------------------------------
# Exercise 11
# -----------------------------------------------------------------------------


def exercise_11(df: pd.DataFrame) -> None:
    """Unique cities."""

    print_title("Exercise 11 - Unique Cities")

    print(df["city"].unique())


# -----------------------------------------------------------------------------
# Exercise 12
# -----------------------------------------------------------------------------


def exercise_12(df: pd.DataFrame) -> None:
    """Department count."""

    print_title("Exercise 12 - Department Counts")

    print(
        df["department"]
        .value_counts()
    )


# -----------------------------------------------------------------------------
# Bonus
# -----------------------------------------------------------------------------


def bonus(df: pd.DataFrame) -> None:
    """Export dataset."""

    print_title("Bonus - Export CSV")

    df.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print(f"Dataset exported to {OUTPUT_FILE}")


# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------


def summary(df: pd.DataFrame) -> None:
    """Display dataset summary."""

    print_title("Dataset Summary")

    summary_data: dict[str, Any] = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Average Salary": round(
            df["salary"].mean(),
            2,
        ),
        "Departments": df["department"].nunique(),
        "Cities": df["city"].nunique(),
    }

    for key, value in summary_data.items():
        print(f"{key:<20}: {value}")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> None:
    """Execute all beginner solutions."""

    exercise_1()

    df = load_dataset()

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

    bonus(df)

    summary(df)


if __name__ == "__main__":
    main()