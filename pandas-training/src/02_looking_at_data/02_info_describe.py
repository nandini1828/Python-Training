from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def show_info(df: pd.DataFrame):
    print("\n--- DataFrame Info ---")
    df.info()


def show_describe(df: pd.DataFrame):
    print("\n--- Numeric Summary (describe) ---")
    print(df.describe())

    print("\n--- Object/Text Column Summary ---")
    print(df.describe(include="object"))


def main():
    print("Pandas - Info and Describe")
    employees_df = load_employees_data()

    show_info(employees_df)
    show_describe(employees_df)


if __name__ == "__main__":
    main()