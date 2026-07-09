"""
inspection.py

This module contains utility methods for inspecting a DataFrame.
"""

import pandas as pd


class DataInspection:

    @staticmethod
    def display_head(df: pd.DataFrame, rows: int = 5):
        """Display the first few rows."""
        print(df.head(rows))

    @staticmethod
    def display_tail(df: pd.DataFrame, rows: int = 5):
        """Display the last few rows."""
        print(df.tail(rows))

    @staticmethod
    def display_shape(df: pd.DataFrame):
        """Display number of rows and columns."""
        print("Shape:", df.shape)

    @staticmethod
    def display_info(df: pd.DataFrame):
        """Display DataFrame information."""
        df.info()

    @staticmethod
    def display_statistics(df: pd.DataFrame):
        """Display summary statistics."""
        print(df.describe())

    @staticmethod
    def value_counts(df: pd.DataFrame, column: str):
        """Display value counts for a column."""
        print(df[column].value_counts())

    @staticmethod
    def unique_values(df: pd.DataFrame, column: str):
        """Display unique values in a column."""
        print(df[column].unique())