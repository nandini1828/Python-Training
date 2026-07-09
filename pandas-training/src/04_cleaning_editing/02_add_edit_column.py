from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def add_bonus_amount_column(df: pd.DataFrame):
    print("\n--- Add bonus_amount Column ---")
    updated_df = df.copy()

    updated_df["salary"] = updated_df["salary"].fillna(0)
    updated_df["bonus_amount"] = (
        updated_df["salary"] * updated_df["bonus_percent"] / 100
    )

    print(updated_df[["name", "salary", "bonus_percent", "bonus_amount"]])


def add_total_compensation_column(df: pd.DataFrame):
    print("\n--- Add total_compensation Column ---")
    updated_df = df.copy()

    updated_df["salary"] = updated_df["salary"].fillna(0)
    updated_df["bonus_amount"] = (
        updated_df["salary"] * updated_df["bonus_percent"] / 100
    )
    updated_df["total_compensation"] = (
        updated_df["salary"] + updated_df["bonus_amount"]
    )

    print(updated_df[["name", "salary", "bonus_amount", "total_compensation"]])


def edit_existing_column(df: pd.DataFrame):
    print("\n--- Increase salary by 10% ---")
    updated_df = df.copy()

    updated_df["salary"] = updated_df["salary"].fillna(0)
    updated_df["salary"] = updated_df["salary"] * 1.10

    print(updated_df[["name", "salary"]])


def main():
    print("Pandas - Add and Edit Columns")
    employees_df = load_employees_data()

    add_bonus_amount_column(employees_df)
    add_total_compensation_column(employees_df)
    edit_existing_column(employees_df)


if __name__ == "__main__":
    main()