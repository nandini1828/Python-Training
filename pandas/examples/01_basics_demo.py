"""
Demo: Pandas Basics

Topics Covered:
1. Creating a Series
2. Creating a DataFrame
3. Reading a CSV file
4. Saving a CSV file
"""

import sys
from pathlib import Path

# Add the project root to Python's import path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from src.basics import PandasBasics


def main():
    print("=" * 50)
    print("1. Creating a Series")
    print("=" * 50)

    series = PandasBasics.create_series()
    print(series)

    print("\n")

    print("=" * 50)
    print("2. Creating a DataFrame")
    print("=" * 50)

    dataframe = PandasBasics.create_dataframe()
    print(dataframe)

    print("\n")

    print("=" * 50)
    print("3. Reading a CSV File")
    print("=" * 50)

    employee_df = PandasBasics.load_csv(
        "data/sample_data.csv"
    )

    print(employee_df)

    print("\n")

    print("=" * 50)
    print("4. Saving Data to a CSV File")
    print("=" * 50)

    PandasBasics.save_csv(
        employee_df,
        "data/output.csv"
    )


if __name__ == "__main__":
    main()