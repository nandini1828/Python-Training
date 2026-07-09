"""
Examples of creating and working with Pandas Series.
"""

import pandas as pd


def create_series_from_list():
    print("\nSeries from List")

    numbers = [10, 20, 30, 40, 50]

    series = pd.Series(numbers)

    print(series)


def create_series_from_dictionary():
    print("\nSeries from Dictionary")

    student_marks = {
        "Math": 95,
        "Science": 91,
        "English": 88,
        "Social": 84,
    }

    series = pd.Series(student_marks)

    print(series)


def create_series_with_custom_index():
    print("\nSeries with Custom Index")

    fruits = ["Apple", "Banana", "Orange"]

    series = pd.Series(
        fruits,
        index=["A", "B", "C"],
    )

    print(series)


def series_attributes():
    print("\nSeries Attributes")

    numbers = pd.Series([100, 200, 300, 400])

    print("Values")
    print(numbers.values)

    print("\nIndex")
    print(numbers.index)

    print("\nData Type")
    print(numbers.dtype)

    print("\nShape")
    print(numbers.shape)

    print("\nSize")
    print(numbers.size)


def main():
    create_series_from_list()
    create_series_from_dictionary()
    create_series_with_custom_index()
    series_attributes()


if __name__ == "__main__":
    main()