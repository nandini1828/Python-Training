"""
03_selecting_filtering.py

Topics Covered:
1. Selecting Columns
2. Selecting Multiple Columns
3. loc[]
4. iloc[]
5. Boolean Filtering
6. Multiple Conditions
"""

from model import PandasData


def select_columns_demo():
    print("\n========== Selecting Columns ==========")

    df = PandasData.employees()

    print("\nSingle Column:")
    print(df["Name"])

    print("\nMultiple Columns:")
    print(df[["Name", "Salary"]])


def loc_demo():
    print("\n========== loc[] ==========")

    df = PandasData.employees()

    print("\nFirst Row:")
    print(df.loc[0])

    print("\nSpecific Value (Row 2, Salary):")
    print(df.loc[2, "Salary"])

    print("\nRows 1 to 3, Name & Department:")
    print(df.loc[1:3, ["Name", "Department"]])


def iloc_demo():
    print("\n========== iloc[] ==========")

    df = PandasData.employees()

    print("\nFirst Row:")
    print(df.iloc[0])

    print("\nSpecific Value (Row 2, Column 4):")
    print(df.iloc[2, 4])

    print("\nRows 1 to 3, Columns 1 to 3:")
    print(df.iloc[1:4, 1:4])


def boolean_filter_demo():
    print("\n========== Boolean Filtering ==========")

    df = PandasData.employees()

    print("\nEmployees with Salary > 50000")
    print(df[df["Salary"] > 50000])

    print("\nEmployees from Hyderabad")
    print(df[df["City"] == "Hyderabad"])


def multiple_conditions_demo():
    print("\n========== Multiple Conditions ==========")

    df = PandasData.employees()

    print("\nSalary > 50000 AND Department == IT")
    print(
        df[
            (df["Salary"] > 50000) &
            (df["Department"] == "IT")
        ]
    )

    print("\nDepartment == HR OR City == Chennai")
    print(
        df[
            (df["Department"] == "HR") |
            (df["City"] == "Chennai")
        ]
    )


def run():
    select_columns_demo()
    loc_demo()
    iloc_demo()
    boolean_filter_demo()
    multiple_conditions_demo()


if __name__ == "__main__":
    run()