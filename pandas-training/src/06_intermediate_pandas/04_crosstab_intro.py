from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_students_data() -> pd.DataFrame:
    students_file = DATASET_DIR / "students.csv"
    return pd.read_csv(students_file)


def crosstab_class_section(df: pd.DataFrame):
    print("\n--- Crosstab: Class vs Section ---")
    result = pd.crosstab(df["class"], df["section"])
    print(result)


def crosstab_city_section(df: pd.DataFrame):
    print("\n--- Crosstab: City vs Section ---")
    result = pd.crosstab(df["city"], df["section"])
    print(result)


def crosstab_city_class(df: pd.DataFrame):
    print("\n--- Crosstab: City vs Class ---")
    result = pd.crosstab(df["city"], df["class"])
    print(result)


def main():
    print("Pandas - Crosstab Intro")
    students_df = load_students_data()

    crosstab_class_section(students_df)
    crosstab_city_section(students_df)
    crosstab_city_class(students_df)


if __name__ == "__main__":
    main()