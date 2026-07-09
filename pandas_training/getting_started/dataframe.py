"""
Examples of creating DataFrames.
"""

import pandas as pd


def create_dataframe_from_dictionary():
    print("\nDataFrame from Dictionary")

    employee = {
        "Name": ["Aarav", "Priya", "Rahul"],
        "Age": [24, 29, 35],
        "Department": ["IT", "HR", "Finance"],
        "Salary": [45000, 52000, 68000],
    }

    df = pd.DataFrame(employee)

    print(df)


def create_dataframe_from_list():
    print("\nDataFrame from List")

    students = [
        [101, "Arjun", "CSE", 8.9],
        [102, "Nisha", "ECE", 9.2],
        [103, "Rohit", "EEE", 7.8],
    ]

    columns = [
        "Roll No",
        "Name",
        "Branch",
        "CGPA",
    ]

    df = pd.DataFrame(
        students,
        columns=columns,
    )

    print(df)


def dataframe_attributes():
    print("\nDataFrame Attributes")

    df = pd.DataFrame(
        {
            "Name": ["A", "B", "C"],
            "Age": [20, 21, 22],
        }
    )

    print("Shape :", df.shape)
    print("Columns :", list(df.columns))
    print("Index :", df.index)
    print("Data Types")
    print(df.dtypes)


def main():
    create_dataframe_from_dictionary()
    create_dataframe_from_list()
    dataframe_attributes()


if __name__ == "__main__":
    main()