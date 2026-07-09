"""
Examples of descriptive statistics.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def describe_data(df):
    print("\nDescribe")
    print("-" * 40)
    print(df.describe())


def show_mean(df):
    print("\nAverage Salary")
    print(df["Salary"].mean())


def show_median(df):
    print("\nMedian Salary")
    print(df["Salary"].median())


def show_min(df):
    print("\nMinimum Salary")
    print(df["Salary"].min())


def show_max(df):
    print("\nMaximum Salary")
    print(df["Salary"].max())


def show_sum(df):
    print("\nTotal Salary")
    print(df["Salary"].sum())


def show_count(df):
    print("\nEmployee Count")
    print(df["EmployeeID"].count())


def main():
    df = load_data()

    describe_data(df)
    show_mean(df)
    show_median(df)
    show_min(df)
    show_max(df)
    show_sum(df)
    show_count(df)


if __name__ == "__main__":
    main()