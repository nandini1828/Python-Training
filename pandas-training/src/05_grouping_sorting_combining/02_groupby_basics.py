from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def average_salary_by_department(df: pd.DataFrame):
    print("\n--- Average Salary by Department ---")
    result = df.groupby("department")["salary"].mean()
    print(result)


def employee_count_by_city(df: pd.DataFrame):
    print("\n--- Employee Count by City ---")
    result = df.groupby("city")["employee_id"].count()
    print(result)


def max_salary_by_department(df: pd.DataFrame):
    print("\n--- Maximum Salary by Department ---")
    result = df.groupby("department")["salary"].max()
    print(result)


def multiple_aggregations(df: pd.DataFrame):
    print("\n--- Multiple Aggregations by Department ---")
    result = df.groupby("department").agg({
        "salary": ["mean", "max", "min"],
        "experience_years": ["mean", "max"],
        "employee_id": "count"
    })
    print(result)


def main():
    print("Pandas - GroupBy Basics")
    employees_df = load_employees_data()

    average_salary_by_department(employees_df)
    employee_count_by_city(employees_df)
    max_salary_by_department(employees_df)
    multiple_aggregations(employees_df)


if __name__ == "__main__":
    main()