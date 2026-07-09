"""
01_getting_started.py

Topics Covered:
1. Importing Pandas
2. Series
3. DataFrame
4. Reading CSV
5. Writing CSV
"""

import pandas as pd
from model import PandasData


def import_pandas_demo():
    print("\n========== Import Pandas ==========")
    print("Pandas imported successfully as 'pd'.")


def series_demo():
    print("\n========== Series ==========")

    numbers = pd.Series([10, 20, 30, 40, 50])
    print(numbers)

    fruits = pd.Series(
        ["Apple", "Banana", "Orange"],
        index=["A", "B", "C"]
    )
    print("\nSeries with custom index:")
    print(fruits)


def dataframe_demo():
    print("\n========== DataFrame ==========")

    df = PandasData.employees()
    print(df)


def read_csv_demo():
    print("\n========== Read CSV ==========")

    try:
        df = pd.read_csv("data/employees.csv")
        print(df.head())
    except FileNotFoundError:
        print("employees.csv not found.")
        print("Using sample DataFrame instead.\n")
        print(PandasData.employees())


def write_csv_demo():
    print("\n========== Write CSV ==========")

    df = PandasData.employees()

    df.to_csv("employees_output.csv", index=False)

    print("DataFrame saved as employees_output.csv")


def run():
    import_pandas_demo()
    series_demo()
    dataframe_demo()
    read_csv_demo()
    write_csv_demo()


if __name__ == "__main__":
    run()