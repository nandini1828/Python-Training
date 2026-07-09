from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def analyze_department_column(df: pd.DataFrame):
    print("\n--- Department Value Counts ---")
    print(df["department"].value_counts())

    print("\n--- Department Unique Values ---")
    print(df["department"].unique())

    print("\n--- Number of Unique Departments ---")
    print(df["department"].nunique())


def analyze_city_column(df: pd.DataFrame):
    print("\n--- City Value Counts ---")
    print(df["city"].value_counts())

    print("\n--- City Unique Values ---")
    print(df["city"].unique())

    print("\n--- Number of Unique Cities ---")
    print(df["city"].nunique())


def main():
    print("Pandas - Value Counts and Unique")
    employees_df = load_employees_data()

    analyze_department_column(employees_df)
    analyze_city_column(employees_df)


if __name__ == "__main__":
    main()