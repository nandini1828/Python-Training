from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def find_nulls(df: pd.DataFrame):
    print("\n--- Null Check (True/False) ---")
    print(df.isnull())

    print("\n--- Null Count Per Column ---")
    print(df.isnull().sum())


def fill_nulls(df: pd.DataFrame):
    print("\n--- Fill Missing City with 'Unknown' ---")
    filled_city_df = df.copy()
    filled_city_df["city"] = filled_city_df["city"].fillna("Unknown")
    print(filled_city_df[["name", "city"]])

    print("\n--- Fill Missing Salary with 0 ---")
    filled_salary_df = df.copy()
    filled_salary_df["salary"] = filled_salary_df["salary"].fillna(0)
    print(filled_salary_df[["name", "salary"]])


def drop_null_rows(df: pd.DataFrame):
    print("\n--- Drop Rows With Any Null Value ---")
    dropped_df = df.dropna()
    print(dropped_df)

    print("\nOriginal shape:", df.shape)
    print("After dropna shape:", dropped_df.shape)


def main():
    print("Pandas - Find, Fill, Drop Nulls")
    employees_df = load_employees_data()

    find_nulls(employees_df)
    fill_nulls(employees_df)
    drop_null_rows(employees_df)


if __name__ == "__main__":
    main()