from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def select_single_column(df: pd.DataFrame):
    print("\n--- Single Column: name ---")
    names = df["name"]
    print(names)
    print("\nReturned type:", type(names))


def select_multiple_columns(df: pd.DataFrame):
    print("\n--- Multiple Columns: name, department, salary ---")
    selected_columns = df[["name", "department", "salary"]]
    print(selected_columns)
    print("\nReturned type:", type(selected_columns))


def main():
    print("Pandas - Selecting Columns")
    employees_df = load_employees_data()

    select_single_column(employees_df)
    select_multiple_columns(employees_df)


if __name__ == "__main__":
    main()