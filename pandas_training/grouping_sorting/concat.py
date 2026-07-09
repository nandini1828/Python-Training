"""
Examples of concatenating DataFrames.
"""

from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():
    employees = pd.read_csv(DATA_FOLDER / "employees.csv")
    new_employees = pd.read_csv(DATA_FOLDER / "new_employees.csv")

    return employees, new_employees


def concat_rows(emp, new_emp):
    print("\nConcatenate Rows (axis=0)")
    print("-" * 60)

    print(
        pd.concat(
            [emp, new_emp],
            axis=0,
            ignore_index=True,
        )
    )


def concat_columns(emp):
    print("\nConcatenate Columns (axis=1)")
    print("-" * 60)

    bonus = pd.DataFrame(
        {
            "AnnualBonus": [
                5000,
                6000,
                7000,
                5500,
                8000,
                6500,
                6200,
                7500,
                6800,
                5200,
            ]
        }
    )

    print(
        pd.concat(
            [emp, bonus],
            axis=1,
        )
    )


def main():
    employees, new_employees = load_data()

    concat_rows(employees, new_employees)
    concat_columns(employees)


if __name__ == "__main__":
    main()