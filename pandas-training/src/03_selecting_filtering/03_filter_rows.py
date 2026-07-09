from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def filter_by_salary(df: pd.DataFrame):
    print("\n--- Employees with salary greater than 60000 ---")
    filtered_df = df[df["salary"] > 60000]
    print(filtered_df)


def filter_by_city(df: pd.DataFrame):
    print("\n--- Employees from Hyderabad ---")
    filtered_df = df[df["city"] == "Hyderabad"]
    print(filtered_df)


def filter_by_experience(df: pd.DataFrame):
    print("\n--- Employees with experience >= 4 years ---")
    filtered_df = df[df["experience_years"] >= 4]
    print(filtered_df)


def main():
    print("Pandas - Filter Rows")
    employees_df = load_employees_data()

    filter_by_salary(employees_df)
    filter_by_city(employees_df)
    filter_by_experience(employees_df)


if __name__ == "__main__":
    main()