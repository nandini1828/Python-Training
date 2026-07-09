from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def map_department_codes(df: pd.DataFrame):
    print("\n--- Map Department to Short Code ---")
    updated_df = df.copy()

    department_code_map = {
        "Engineering": "ENG",
        "Sales": "SAL",
        "HR": "HR",
        "Finance": "FIN"
    }

    updated_df["department_code"] = updated_df["department"].map(department_code_map)
    print(updated_df[["name", "department", "department_code"]])


def apply_salary_band(df: pd.DataFrame):
    print("\n--- Apply Salary Band ---")
    updated_df = df.copy()
    updated_df["salary"] = updated_df["salary"].fillna(0)

    def get_salary_band(salary):
        if salary >= 65000:
            return "High"
        if salary >= 50000:
            return "Medium"
        return "Low"

    updated_df["salary_band"] = updated_df["salary"].apply(get_salary_band)
    print(updated_df[["name", "salary", "salary_band"]])


def lambda_bonus_category(df: pd.DataFrame):
    print("\n--- Lambda Bonus Category ---")
    updated_df = df.copy()

    updated_df["bonus_category"] = updated_df["bonus_percent"].apply(
        lambda value: "High Bonus" if value >= 10 else "Standard Bonus"
    )

    print(updated_df[["name", "bonus_percent", "bonus_category"]])


def main():
    print("Pandas - apply, map, lambda")
    employees_df = load_employees_data()

    map_department_codes(employees_df)
    apply_salary_band(employees_df)
    lambda_bonus_category(employees_df)


if __name__ == "__main__":
    main()