"""
Getting Started with Pandas
"""

import pandas as pd


def run():

    print("\n========== GETTING STARTED ==========\n")

    # Import Pandas
    print("Pandas Imported Successfully")

    # Series
    numbers = pd.Series([10, 20, 30, 40])

    print("\nSeries")
    print(numbers)

    # DataFrame

    students = pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie"],
            "Age": [22, 23, 21],
            "Marks": [90, 80, 95],
        }
    )

    print("\nDataFrame")
    print(students)

    # Read CSV

    employees = pd.read_csv("data/employees.csv")

    print("\nCSV Loaded Successfully")
    print(employees.head())

    # Save CSV

    employees.to_csv("data/employees_copy.csv", index=False)

    print("\nCSV Saved Successfully")