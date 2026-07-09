"""
grouping.py

Methods for sorting and grouping data.
"""

import pandas as pd


class DataGrouping:

    @staticmethod
    def sort_salary(df: pd.DataFrame):
        return df.sort_values(by="Salary", ascending=False)

    @staticmethod
    def average_salary(df: pd.DataFrame):
        return df.groupby("Department")["Salary"].mean()

    @staticmethod
    def maximum_salary(df: pd.DataFrame):
        return df.groupby("Department")["Salary"].max()

    @staticmethod
    def employee_count(df: pd.DataFrame):
        return df.groupby("Department")["Name"].count()