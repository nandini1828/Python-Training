"""
Examples of converting data types.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def show_current_dtypes(df):
    print("\nCurrent Data Types")
    print("-" * 60)
    print(df.dtypes)


def convert_salary_to_float(df):
    print("\nConvert Salary to float")
    print("-" * 60)

    new_df = df.copy()
    new_df["Salary"] = new_df["Salary"].astype(float)

    print(new_df.dtypes)


def convert_age_to_string(df):
    print("\nConvert Age to String")
    print("-" * 60)

    new_df = df.copy()
    new_df["Age"] = new_df["Age"].astype(str)

    print(new_df.dtypes)


def convert_order_date():
    sales = pd.read_csv(DATA_FOLDER / "sales.csv")

    print("\nConvert OrderDate to Datetime")
    print("-" * 60)

    sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])

    print(sales.dtypes)


def main():
    df = load_data()

    show_current_dtypes(df)
    convert_salary_to_float(df)
    convert_age_to_string(df)
    convert_order_date()


if __name__ == "__main__":
    main()