from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
DATASET_DIR = BASE_DIR / "datasets"


def load_employees_data() -> pd.DataFrame:
    employees_file = DATASET_DIR / "employees.csv"
    return pd.read_csv(employees_file)


def lowercase_names(df: pd.DataFrame):
    print("\n--- Lowercase Names ---")
    updated_df = df.copy()
    updated_df["name_lower"] = updated_df["name"].str.lower()
    print(updated_df[["name", "name_lower"]])


def uppercase_departments(df: pd.DataFrame):
    print("\n--- Uppercase Departments ---")
    updated_df = df.copy()
    updated_df["department_upper"] = updated_df["department"].str.upper()
    print(updated_df[["department", "department_upper"]])


def replace_city_name(df: pd.DataFrame):
    print("\n--- Replace Hyderabad with HYD ---")
    updated_df = df.copy()
    updated_df["city"] = updated_df["city"].fillna("Unknown")
    updated_df["city_short"] = updated_df["city"].str.replace("Hyderabad", "HYD")
    print(updated_df[["city", "city_short"]])


def email_domain_check(df: pd.DataFrame):
    print("\n--- Check if email contains '@company.com' ---")
    updated_df = df.copy()
    updated_df["is_company_email"] = updated_df["email"].str.contains("@company.com")
    print(updated_df[["email", "is_company_email"]])


def main():
    print("Pandas - String Cleaning Basics")
    employees_df = load_employees_data()

    lowercase_names(employees_df)
    uppercase_departments(employees_df)
    replace_city_name(employees_df)
    email_domain_check(employees_df)


if __name__ == "__main__":
    main()