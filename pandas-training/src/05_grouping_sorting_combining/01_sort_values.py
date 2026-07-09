from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def sort_by_salary_ascending(df: pd.DataFrame):
    print("\n--- Sort by salary ascending ---")
    updated_df = df.sort_values(by="salary", ascending=True)
    print(updated_df[["name", "salary"]])


def sort_by_salary_descending(df: pd.DataFrame):
    print("\n--- Sort by salary descending ---")
    updated_df = df.sort_values(by="salary", ascending=False)
    print(updated_df[["name", "salary"]])


def sort_by_department_and_salary(df: pd.DataFrame):
    print("\n--- Sort by department, then salary descending ---")
    updated_df = df.sort_values(
        by=["department", "salary"],
        ascending=[True, False]
    )
    print(updated_df[["name", "department", "salary"]])


def main():
    print("Pandas - Sort Values")
    employees_df = load_employees_data()

    sort_by_salary_ascending(employees_df)
    sort_by_salary_descending(employees_df)
    sort_by_department_and_salary(employees_df)


if __name__ == "__main__":
    main()