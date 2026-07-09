from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def show_head_tail_shape(df: pd.DataFrame):
    print("\n--- First 5 Rows (head) ---")
    print(df.head())

    print("\n--- First 3 Rows ---")
    print(df.head(3))

    print("\n--- Last 5 Rows (tail) ---")
    print(df.tail())

    print("\n--- Last 2 Rows ---")
    print(df.tail(2))

    print("\n--- Shape of DataFrame ---")
    print(df.shape)

    print("\nTotal rows:", df.shape[0])
    print("Total columns:", df.shape[1])


def main():
    print("Pandas - Head, Tail, Shape")
    employees_df = load_employees_data()
    show_head_tail_shape(employees_df)


if __name__ == "__main__":
    main()