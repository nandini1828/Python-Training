"""
01_series.py

Learning Objective:
-------------------
Understand how to create and work with Pandas Series.
"""

from __future__ import annotations

import pandas as pd


def create_series() -> pd.Series:
    """Create a sample Pandas Series."""
    return pd.Series(
        [10, 20, 30, 40],
        index=["A", "B", "C", "D"],
        name="Scores",
    )


def main() -> None:
    series = create_series()

    print("\nSeries")
    print(series)

    print("\nValues")
    print(series.values)

    print("\nIndex")
    print(series.index)

    print("\nMean:", series.mean())
    print("Max :", series.max())
    print("Min :", series.min())


if __name__ == "__main__":
    main()