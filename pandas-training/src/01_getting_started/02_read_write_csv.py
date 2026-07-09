from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


def read_csv_example():
    employees_file = DATASET_DIR / "employees.csv"
    employees_df = pd.read_csv(employees_file)

    print("\n--- Employees Data Read From CSV ---")
    print(employees_df.head())

    return employees_df


def write_csv_example(df: pd.DataFrame):
    output_file = OUTPUT_DIR / "employees_copy.csv"
    df.to_csv(output_file, index=False)

    print(f"\nCSV written successfully to: {output_file}")


def main():
    print("Pandas Read and Write CSV Example")
    employees_df = read_csv_example()
    write_csv_example(employees_df)


if __name__ == "__main__":
    main()