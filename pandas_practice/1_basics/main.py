"""
Pandas Core Concepts - Part 1
"""

import argparse

from pandas_basics import (
    SeriesExamples,
    DataFrameExamples,
    CSVExamples,
    InspectionExamples
)

def demonstrate_series() -> None:

    print("\n" + "=" * 50)
    print("SERIES")
    print("=" * 50)

    print(
        SeriesExamples.create_series()
    )

    print()

    print(
        SeriesExamples.string_series()
    )


def demonstrate_dataframe() -> None:

    print("\n" + "=" * 50)
    print("DATAFRAME")
    print("=" * 50)

    df = DataFrameExamples.create_dataframe()

    print(df)


def demonstrate_csv() -> None:

    print("\n" + "=" * 50)
    print("READ CSV")
    print("=" * 50)

    df = CSVExamples.read_csv(
        "data/employees.csv"
    )

    print(df)

    CSVExamples.save_csv(
        df,
        "data/employees_copy.csv"
    )

    print("\nCSV Saved Successfully")


def run_all() -> None:

    demonstrate_series()
    demonstrate_dataframe()
    demonstrate_csv()
    demonstrate_inspection()

def main() -> None:

    parser = argparse.ArgumentParser(
        description="Pandas Part 1"
    )

    parser.add_argument(
        "--section",
        default="all",
        choices=[
            "all",
            "series",
            "dataframe",
            "csv",
            "inspection"
        ]
    )

    args = parser.parse_args()

    if args.section == "all":
        run_all()

    elif args.section == "series":
        demonstrate_series()

    elif args.section == "dataframe":
        demonstrate_dataframe()

    elif args.section == "csv":
        demonstrate_csv()

    elif args.section == "inspection":
        demonstrate_inspection()

def demonstrate_inspection() -> None:

    print("\n" + "=" * 50)
    print("DATA INSPECTION")
    print("=" * 50)

    df = CSVExamples.read_csv(
        "data/employees.csv"
    )

    print("\nHead")
    print(InspectionExamples.head(df))

    print("\nTail")
    print(InspectionExamples.tail(df))

    print("\nShape")
    print(InspectionExamples.shape(df))

    print("\nInfo")
    InspectionExamples.info(df)

    print("\nDescribe")
    print(InspectionExamples.describe(df))

    print("\nValue Counts (Department)")
    print(
        InspectionExamples.value_counts(
            df,
            "department"
        )
    )

    print("\nUnique Departments")
    print(
        InspectionExamples.unique_values(
            df,
            "department"
        )
    )


if __name__ == "__main__":
    main()