"""
CSV Examples
"""

import pandas as pd


class CSVExamples:

    @staticmethod
    def read_csv(file_path: str) -> pd.DataFrame:

        return pd.read_csv(file_path)

    @staticmethod
    def save_csv(
        dataframe: pd.DataFrame,
        file_path: str
    ) -> None:

        dataframe.to_csv(
            file_path,
            index=False
        )