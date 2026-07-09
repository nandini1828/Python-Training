"""
04_info_shape.py

Learning Objectives

- head()
- tail()
- info()
- shape
- describe()
- value_counts()
- unique()
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


DATASET = Path("datasets/employees.csv")


def load_data() -> pd.DataFrame:
    """Load dataset."""

    return pd.read_csv(DATASET)


def inspect(df: pd.DataFrame) -> None:
    """Inspect DataFrame."""

    print("\nHEAD")
    print(df.head())

    print("\nTAIL")
    print(df.tail())

    print("\nSHAPE")
    print(df.shape)

    print("\nCOLUMNS")
    print(df.columns.tolist())

    print("\nINFO")
    df.info()

    print("\nSTATISTICS")
    print(df.describe())

    print("\nDEPARTMENTS")
    print(df["department"].value_counts())

    print("\nUNIQUE CITIES")
    print(df["city"].unique())

    print("\nNUMBER OF UNIQUE CITIES")
    print(df["city"].nunique())


def main() -> None:
    try:
        dataframe = load_data()

        inspect(dataframe)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()