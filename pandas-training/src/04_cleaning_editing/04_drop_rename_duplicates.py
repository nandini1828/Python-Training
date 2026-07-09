from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def drop_column_example(df: pd.DataFrame):
    print("\n--- Drop email Column ---")
    updated_df = df.drop(columns=["email"])
    print(updated_df.head())


def drop_row_example(df: pd.DataFrame):
    print("\n--- Drop Row With Index 0 ---")
    updated_df = df.drop(index=[0])
    print(updated_df.head())


def rename_columns_example(df: pd.DataFrame):
    print("\n--- Rename salary -> monthly_salary ---")
    updated_df = df.rename(columns={"salary": "monthly_salary"})
    print(updated_df.head())


def duplicate_examples(df: pd.DataFrame):
    print("\n--- Duplicate Row Check ---")
    print(df.duplicated())

    print("\n--- Duplicate Count ---")
    print(df.duplicated().sum())

    print("\n--- Remove Duplicate Rows ---")
    no_duplicate_df = df.drop_duplicates()
    print(no_duplicate_df)

    print("\nOriginal shape:", df.shape)
    print("After removing duplicates:", no_duplicate_df.shape)


def main():
    print("Pandas - Drop, Rename, Duplicates")
    employees_df = load_employees_data()

    drop_column_example(employees_df)
    drop_row_example(employees_df)
    rename_columns_example(employees_df)
    duplicate_examples(employees_df)


if __name__ == "__main__":
    main()