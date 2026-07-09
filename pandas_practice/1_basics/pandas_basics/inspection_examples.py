"""
inspection_examples.py

Examples for inspecting DataFrames.
"""

import pandas as pd


class InspectionExamples:

    @staticmethod
    def head(df: pd.DataFrame) -> pd.DataFrame:
        """Returns first 5 rows."""
        return df.head()

    @staticmethod
    def tail(df: pd.DataFrame) -> pd.DataFrame:
        """Returns last 5 rows."""
        return df.tail()

    @staticmethod
    def shape(df: pd.DataFrame) -> tuple:
        """Returns (rows, columns)."""
        return df.shape

    @staticmethod
    def info(df: pd.DataFrame) -> None:
        """Displays DataFrame information."""
        df.info()

    @staticmethod
    def describe(df: pd.DataFrame) -> pd.DataFrame:
        """Returns statistical summary."""
        return df.describe()

    @staticmethod
    def value_counts(
        df: pd.DataFrame,
        column: str
    ) -> pd.Series:
        """Returns value counts."""
        return df[column].value_counts()

    @staticmethod
    def unique_values(
        df: pd.DataFrame,
        column: str
    ) -> list:
        """Returns unique values."""
        return df[column].unique().tolist()