from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def show_dataframe_overview(df: pd.DataFrame):
    print("\n--- DataFrame Overview ---")

    print("\nShape of DataFrame:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nIndex:")
    print(df.index)

    print("\nData types:")
    print(df.dtypes)


def main():
    print("Pandas DataFrame Overview")
    employees_df = load_employees_data()
    show_dataframe_overview(employees_df)


if __name__ == "__main__":
    main()