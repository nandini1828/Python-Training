from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def filter_with_and_condition(df: pd.DataFrame):
    print("\n--- Employees from Hyderabad with salary > 60000 ---")
    filtered_df = df[(df["city"] == "Hyderabad") & (df["salary"] > 60000)]
    print(filtered_df)


def filter_with_or_condition(df: pd.DataFrame):
    print("\n--- Employees from Hyderabad OR Chennai ---")
    filtered_df = df[(df["city"] == "Hyderabad") | (df["city"] == "Chennai")]
    print(filtered_df)


def filter_department_and_experience(df: pd.DataFrame):
    print("\n--- Engineering employees with experience >= 3 years ---")
    filtered_df = df[
        (df["department"] == "Engineering") & (df["experience_years"] >= 3)
    ]
    print(filtered_df)


def main():
    print("Pandas - Multiple Conditions")
    employees_df = load_employees_data()

    filter_with_and_condition(employees_df)
    filter_with_or_condition(employees_df)
    filter_department_and_experience(employees_df)


if __name__ == "__main__":
    main()