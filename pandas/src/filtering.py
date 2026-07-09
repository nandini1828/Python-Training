"""
filtering.py

Methods for selecting and filtering data.
"""

import pandas as pd


class DataFiltering:

    @staticmethod
    def select_column(df: pd.DataFrame, column: str):
        return df[column]

    @staticmethod
    def select_columns(df: pd.DataFrame, columns: list):
        return df[columns]

    @staticmethod
    def select_with_loc(df: pd.DataFrame, row):
        return df.loc[row]

    @staticmethod
    def select_with_iloc(df: pd.DataFrame, row):
        return df.iloc[row]

    @staticmethod
    def filter_age(df: pd.DataFrame, age: int):
        return df[df["Age"] > age]

    @staticmethod
    def filter_department(df: pd.DataFrame, department: str):
        return df[df["Department"] == department]