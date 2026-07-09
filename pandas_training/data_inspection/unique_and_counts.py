"""
Examples of finding unique values and counting occurrences.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def show_unique_departments(df):
    print("\nUnique Departments")
    print("-" * 40)
    print(df["Department"].unique())


def show_number_of_departments(df):
    print("\nNumber of Departments")
    print("-" * 40)
    print(df["Department"].nunique())


def show_department_counts(df):
    print("\nDepartment Counts")
    print("-" * 40)
    print(df["Department"].value_counts())


def show_city_counts(df):
    print("\nCity Counts")
    print("-" * 40)
    print(df["City"].value_counts())


def main():
    df = load_data()

    show_unique_departments(df)
    show_number_of_departments(df)
    show_department_counts(df)
    show_city_counts(df)


if __name__ == "__main__":
    main()