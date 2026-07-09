"""
03_read_csv.py

Learning Objectives

- Read CSV files
- Display records
- Save CSV
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


DATASET = Path("datasets/employees.csv")


def load_dataset() -> pd.DataFrame:
    """Load employee dataset."""

    if not DATASET.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET}"
        )

    return pd.read_csv(DATASET)


def display_data(df: pd.DataFrame) -> None:
    """Print dataset preview."""

    print("\nFirst Five Rows")
    print(df.head())

    print("\nLast Five Rows")
    print(df.tail())


def save_copy(df: pd.DataFrame) -> None:
    """Save a copy of the dataset."""

    output = Path("datasets/output.csv")

    df.to_csv(output, index=False)

    print(f"\nDataset saved to {output}")


def main() -> None:
    try:
        df = load_dataset()

        display_data(df)

        save_copy(df)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()