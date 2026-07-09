"""
Examples of reading and writing CSV files.
"""

from pathlib import Path

import pandas as pd


DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def read_csv_file(file_name):
    """
    Read a CSV file from the data folder.
    """

    file_path = DATA_FOLDER / file_name

    dataframe = pd.read_csv(file_path)

    return dataframe


def save_csv_file(dataframe, output_file):
    """
    Save a DataFrame as a CSV file.
    """

    output_path = DATA_FOLDER / output_file

    dataframe.to_csv(
        output_path,
        index=False,
    )

    print(f"\nFile saved successfully -> {output_path}")


def demo_csv_operations():
    print("=" * 60)
    print("READ CSV")
    print("=" * 60)

    employees = read_csv_file("employees.csv")

    print(employees)

    print("\nSaving copy as employees_copy.csv")

    save_csv_file(
        employees,
        "employees_copy.csv",
    )


if __name__ == "__main__":
    demo_csv_operations()