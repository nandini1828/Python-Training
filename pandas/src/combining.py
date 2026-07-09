"""
combining.py

Methods for merging and concatenating DataFrames.
"""

import pandas as pd


class DataCombining:

    @staticmethod
    def merge_dataframes(df1, df2, key):
        return pd.merge(df1, df2, on=key)

    @staticmethod
    def concatenate(df1, df2):
        return pd.concat([df1, df2], ignore_index=True)