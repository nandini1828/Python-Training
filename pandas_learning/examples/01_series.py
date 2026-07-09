"""
01_series.py
------------

Learning Objectives
-------------------
1. Understand what a Pandas Series is.
2. Create Series from lists and dictionaries.
3. Access Series elements.
4. Perform vectorized operations.
5. Explore common Series methods.

Run:
    python examples/01_series.py
"""

from __future__ import annotations

import pandas as pd


def create_numeric_series() -> pd.Series:
    """Create a numeric Series."""
    return pd.Series(
        [10, 20, 30, 40, 50],
        name="Numbers",
    )


def create_custom_index_series() -> pd.Series:
    """Create a Series with custom labels."""
    return pd.Series(
        [90, 85, 95],
        index=["Alice", "Bob", "Charlie"],
        name="Scores",
    )


def create_dictionary_series() -> pd.Series:
    """Create a Series from a dictionary."""
    student_marks = {
        "Math": 91,
        "Science": 88,
        "English": 95,
    }

    return pd.Series(student_marks, name="Marks")


def demonstrate_operations(series: pd.Series) -> None:
    """Display common Series operations."""

    print("\nOriginal Series")
    print(series)

    print("\nMean:", series.mean())
    print("Max :", series.max())
    print("Min :", series.min())
    print("Sum :", series.sum())
    print("Count:", series.count())

    print("\nMultiply by 2")
    print(series * 2)

    print("\nAdd 10")
    print(series + 10)


def main() -> None:
    print("=" * 60)
    print("PANDAS SERIES EXAMPLES")
    print("=" * 60)

    numeric = create_numeric_series()
    custom = create_custom_index_series()
    dictionary = create_dictionary_series()

    print("\nNumeric Series")
    print(numeric)

    print("\nSeries Attributes")
    print("Name:", numeric.name)
    print("Shape:", numeric.shape)
    print("Size:", numeric.size)
    print("Data Type:", numeric.dtype)

    print("\nCustom Index Series")
    print(custom)

    print("\nAccess Bob's Score")
    print(custom["Bob"])

    print("\nDictionary Series")
    print(dictionary)

    demonstrate_operations(numeric)


if __name__ == "__main__":
    main()