from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def convert_joining_date(df: pd.DataFrame) -> pd.DataFrame:
    updated_df = df.copy()
    updated_df["joining_date"] = pd.to_datetime(updated_df["joining_date"])
    return updated_df


def extract_year_month_day(df: pd.DataFrame):
    print("\n--- Extract Year, Month, Day from joining_date ---")
    updated_df = convert_joining_date(df)

    updated_df["joining_year"] = updated_df["joining_date"].dt.year
    updated_df["joining_month"] = updated_df["joining_date"].dt.month
    updated_df["joining_day"] = updated_df["joining_date"].dt.day

    print(
        updated_df[
            ["name", "joining_date", "joining_year", "joining_month", "joining_day"]
        ]
    )


def extract_day_name(df: pd.DataFrame):
    print("\n--- Extract Day Name ---")
    updated_df = convert_joining_date(df)

    updated_df["joining_day_name"] = updated_df["joining_date"].dt.day_name()
    print(updated_df[["name", "joining_date", "joining_day_name"]])


def filter_recent_joiners(df: pd.DataFrame):
    print("\n--- Employees who joined in 2024 ---")
    updated_df = convert_joining_date(df)

    filtered_df = updated_df[updated_df["joining_date"].dt.year == 2024]
    print(filtered_df[["name", "joining_date"]])


def main():
    print("Pandas - Datetime Basics")
    employees_df = load_employees_data()

    extract_year_month_day(employees_df)
    extract_day_name(employees_df)
    filter_recent_joiners(employees_df)


if __name__ == "__main__":
    main()