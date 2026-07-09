"""
Series Examples
"""

import pandas as pd


class SeriesExamples:

    @staticmethod
    def create_series() -> pd.Series:

        return pd.Series(
            [10, 20, 30, 40, 50],
            name="Numbers"
        )

    @staticmethod
    def string_series() -> pd.Series:

        return pd.Series(
            ["Python", "Pandas", "NumPy"],
            name="Courses"
        )