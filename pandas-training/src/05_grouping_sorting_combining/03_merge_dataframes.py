import pandas as pd


def create_employee_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "employee_id": [101, 102, 103, 104],
        "name": ["Karthik", "Rahul", "Ananya", "Sneha"],
        "department_id": [1, 2, 3, 1]
    })


def create_department_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "department_id": [1, 2, 3, 4],
        "department_name": ["Engineering", "Sales", "HR", "Finance"]
    })


def inner_join_example(employees_df: pd.DataFrame, departments_df: pd.DataFrame):
    print("\n--- Inner Join ---")
    merged_df = pd.merge(
        employees_df,
        departments_df,
        on="department_id",
        how="inner"
    )
    print(merged_df)


def left_join_example(employees_df: pd.DataFrame, departments_df: pd.DataFrame):
    print("\n--- Left Join ---")
    merged_df = pd.merge(
        employees_df,
        departments_df,
        on="department_id",
        how="left"
    )
    print(merged_df)


def outer_join_example(employees_df: pd.DataFrame, departments_df: pd.DataFrame):
    print("\n--- Outer Join ---")
    merged_df = pd.merge(
        employees_df,
        departments_df,
        on="department_id",
        how="outer"
    )
    print(merged_df)


def main():
    print("Pandas - Merge DataFrames")

    employees_df = create_employee_dataframe()
    departments_df = create_department_dataframe()

    print("\nEmployees DataFrame:")
    print(employees_df)

    print("\nDepartments DataFrame:")
    print(departments_df)

    inner_join_example(employees_df, departments_df)
    left_join_example(employees_df, departments_df)
    outer_join_example(employees_df, departments_df)


if __name__ == "__main__":
    main()