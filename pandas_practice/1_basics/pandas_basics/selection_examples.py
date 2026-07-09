"""
selection_examples.py

Examples for selecting and filtering data.
"""

import pandas as pd


class SelectionExamples:

    @staticmethod
    def select_column(
        df: pd.DataFrame,
        column: str
    ) -> pd.Series:
        """Select a single column."""

        return df[column]

    @staticmethod
    def select_columns(
        df: pd.DataFrame,
        columns: list[str]
    ) -> pd.DataFrame:
        """Select multiple columns."""

        return df[columns]

    @staticmethod
    def select_by_label(
        df: pd.DataFrame,
        row: int,
        column: str
    ):
        """Select using loc."""

        return df.loc[row, column]

    @staticmethod
    def select_by_position(
        df: pd.DataFrame,
        row: int,
        column: int
    ):
        """Select using iloc."""

        return df.iloc[row, column]

    @staticmethod
    def filter_age(
        df: pd.DataFrame,
        age: int
    ) -> pd.DataFrame:
        """Filter rows based on age."""

        return df[df["age"] > age]

    @staticmethod
    def multiple_filter(
        df: pd.DataFrame,
        age: int,
        department: str
    ) -> pd.DataFrame:
        """Filter using multiple conditions."""

        return df[
            (df["age"] > age)
            &
            (df["department"] == department)
        ]