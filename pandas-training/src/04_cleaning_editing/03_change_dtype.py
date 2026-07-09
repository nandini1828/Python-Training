from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def show_current_dtypes(df: pd.DataFrame):
    print("\n--- Current Data Types ---")
    print(df.dtypes)


def convert_salary_dtype(df: pd.DataFrame):
    print("\n--- Convert salary to float ---")
    updated_df = df.copy()
    updated_df["salary"] = updated_df["salary"].astype("float")
    print(updated_df.dtypes)


def convert_joining_date(df: pd.DataFrame):
    print("\n--- Convert joining_date to datetime ---")
    updated_df = df.copy()
    updated_df["joining_date"] = pd.to_datetime(updated_df["joining_date"])
    print(updated_df.dtypes)

    print("\nConverted joining_date column:")
    print(updated_df["joining_date"])


def main():
    print("Pandas - Change Data Type")
    employees_df = load_employees_data()

    show_current_dtypes(employees_df)
    convert_salary_dtype(employees_df)
    convert_joining_date(employees_df)


if __name__ == "__main__":
    main()