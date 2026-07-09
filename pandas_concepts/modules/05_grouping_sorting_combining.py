"""
Grouping, Sorting and Combining
"""

import pandas as pd


def run():

    employees = pd.read_csv("data/employees.csv")

    departments = pd.read_csv("data/departments.csv")

    print("\n========== SORTING ==========\n")

    print(employees.sort_values(by="salary", ascending=False))

    print("\n========== GROUPBY ==========\n")

    print(
        employees.groupby("department")["salary"].mean()
    )

    print("\n========== MERGE ==========\n")

    merged = pd.merge(
        employees,
        departments,
        on="department",
    )

    print(merged)

    print("\n========== CONCAT ==========\n")

    top = employees.iloc[:3]

    bottom = employees.iloc[3:]

    combined = pd.concat(
        [top, bottom],
        axis=0,
    )

    print(combined)