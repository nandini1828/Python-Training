from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def loc_examples(df: pd.DataFrame):
    print("\n--- loc[] Examples ---")

    print("\nRow with label 0:")
    print(df.loc[0])

    print("\nValue at row label 0 and column 'name':")
    print(df.loc[0, "name"])

    print("\nRows 0 to 3 with columns name and salary:")
    print(df.loc[0:3, ["name", "salary"]])


def iloc_examples(df: pd.DataFrame):
    print("\n--- iloc[] Examples ---")

    print("\nRow at position 0:")
    print(df.iloc[0])

    print("\nValue at row position 0 and column position 1:")
    print(df.iloc[0, 1])

    print("\nRows 0 to 3 and columns 0 to 2:")
    print(df.iloc[0:4, 0:3])


def main():
    print("Pandas - loc and iloc")
    employees_df = load_employees_data()

    loc_examples(employees_df)
    iloc_examples(employees_df)


if __name__ == "__main__":
    main()