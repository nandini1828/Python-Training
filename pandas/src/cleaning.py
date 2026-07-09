"""
cleaning.py

Methods for cleaning datasets.
"""

import pandas as pd


class DataCleaning:

    @staticmethod
    def missing_values(df: pd.DataFrame):
        return df.isnull().sum()

    @staticmethod
    def fill_missing(df: pd.DataFrame, value):
        return df.fillna(value)

    @staticmethod
    def drop_missing(df: pd.DataFrame):
        return df.dropna()

    @staticmethod
    def add_bonus(df: pd.DataFrame):
        df["Bonus"] = df["Salary"] * 0.10
        return df

    @staticmethod
    def rename_salary(df: pd.DataFrame):
        return df.rename(columns={"Salary": "Annual Salary"})

    @staticmethod
    def remove_duplicates(df: pd.DataFrame):
        return df.drop_duplicates()