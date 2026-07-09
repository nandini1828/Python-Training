"""
05_grouping_sorting_combining.py

Topics Covered:
1. sort_values()
2. groupby()
3. merge()
4. concat()
"""

import pandas as pd


def create_employee_data():
    """Create sample employee data."""
    return pd.DataFrame({
        "Emp_ID": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Department": ["HR", "IT", "IT", "Finance", "HR"],
        "Salary": [45000, 65000, 55000, 70000, 50000]
    })


def create_department_data():
    """Create sample department data."""
    return pd.DataFrame({
        "Department": ["HR", "IT", "Finance"],
        "Manager": ["John", "Sarah", "Michael"]
    })


def sort_values_demo():
    print("\n========== sort_values() ==========")

    df = create_employee_data()

    print("\nOriginal DataFrame:")
    print(df)

    print("\nSort by Salary (Ascending):")
    print(df.sort_values(by="Salary"))

    print("\nSort by Salary (Descending):")
    print(df.sort_values(by="Salary", ascending=False))


def groupby_demo():
    print("\n========== groupby() ==========")

    df = create_employee_data()

    print("\nAverage Salary by Department:")
    print(df.groupby("Department")["Salary"].mean())

    print("\nMaximum Salary by Department:")
    print(df.groupby("Department")["Salary"].max())

    print("\nEmployee Count by Department:")
    print(df.groupby("Department")["Emp_ID"].count())


def merge_demo():
    print("\n========== merge() ==========")

    employees = create_employee_data()
    departments = create_department_data()

    merged_df = pd.merge(
        employees,
        departments,
        on="Department",
        how="inner"
    )

    print(merged_df)


def concat_demo():
    print("\n========== concat() ==========")

    df1 = pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Salary": [45000, 65000]
    })

    df2 = pd.DataFrame({
        "Name": ["Charlie", "David"],
        "Salary": [55000, 70000]
    })

    print("\nConcatenate Rows:")
    print(pd.concat([df1, df2], ignore_index=True))

    print("\nConcatenate Columns:")
    print(pd.concat([df1, df2], axis=1))


def run():
    sort_values_demo()
    groupby_demo()
    merge_demo()
    concat_demo()


if __name__ == "__main__":
    run()