"""
Examples of filtering rows using comparison operators.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    return pd.read_csv(DATA_FOLDER / "employees.csv")


def age_greater_than_30(df):
    print("\nEmployees Age > 30")
    print("-" * 50)
    print(df[df["Age"] > 30])


def salary_greater_than_60000(df):
    print("\nSalary > 60000")
    print("-" * 50)
    print(df[df["Salary"] > 60000])


def employees_from_hyderabad(df):
    print("\nEmployees from Hyderabad")
    print("-" * 50)
    print(df[df["City"] == "Hyderabad"])


def finance_department(df):
    print("\nFinance Department")
    print("-" * 50)
    print(df[df["Department"] == "Finance"])


def experience_less_than_5(df):
    print("\nExperience < 5 Years")
    print("-" * 50)
    print(df[df["Experience"] < 5])


def main():
    df = load_data()

    age_greater_than_30(df)
    salary_greater_than_60000(df)
    employees_from_hyderabad(df)
    finance_department(df)
    experience_less_than_5(df)


if __name__ == "__main__":
    main()