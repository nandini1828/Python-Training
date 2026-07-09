"""
DataFrame Examples
"""

import pandas as pd


class DataFrameExamples:

    @staticmethod
    def create_dataframe() -> pd.DataFrame:

        data = {
            "Name": [
                "Bhavya",
                "Rahul",
                "Anjali"
            ],
            "Age": [
                22,
                25,
                24
            ],
            "Department": [
                "AI",
                "Python",
                "Java"
            ]
        }

        return pd.DataFrame(data)