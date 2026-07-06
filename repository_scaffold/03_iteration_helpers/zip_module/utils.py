"""
utils.py

Reusable utility functions demonstrating Python's built-in zip() function.
"""

from typing import Any


def zip_lists(first: list[Any], second: list[Any]) -> list[tuple[Any, Any]]:
    """
    Combine two lists into a list of tuples.
    """
    return list(zip(first, second))


def zip_three_lists(
    first: list[Any],
    second: list[Any],
    third: list[Any],
) -> list[tuple[Any, Any, Any]]:
    """
    Combine three lists into a list of tuples.
    """
    return list(zip(first, second, third))


def create_dictionary(keys: list[Any], values: list[Any]) -> dict[Any, Any]:
    """
    Create a dictionary using zip().
    """
    return dict(zip(keys, values))


def unzip_pairs(
    pairs: list[tuple[Any, Any]],
) -> tuple[tuple[Any, ...], tuple[Any, ...]]:
    """
    Unzip a list of key-value pairs.
    """
    if not pairs:
        return (), ()

    return zip(*pairs)


def compare_lists(
    first: list[Any],
    second: list[Any],
) -> list[bool]:
    """
    Compare corresponding elements of two lists.
    """
    return [left == right for left, right in zip(first, second)]


def create_employee_records(
    ids: list[int],
    names: list[str],
) -> list[dict[str, Any]]:
    """
    Create employee records from IDs and names.
    """
    return [
        {"id": employee_id, "name": name}
        for employee_id, name in zip(ids, names)
    ]


def pair_coordinates(
    x_values: list[int],
    y_values: list[int],
) -> list[tuple[int, int]]:
    """
    Pair x and y coordinates.
    """
    return list(zip(x_values, y_values))


def student_report(
    students: list[str],
    grades: list[str],
) -> list[str]:
    """
    Generate student grade reports.
    """
    return [
        f"{student} -> Grade {grade}"
        for student, grade in zip(students, grades)
    ]


def total_prices(
    products: list[str],
    prices: list[float],
) -> list[str]:
    """
    Create formatted product-price strings.
    """
    return [
        f"{product}: ₹{price}"
        for product, price in zip(products, prices)
    ]


def zip_to_indexed_dict(
    keys: list[Any],
    values: list[Any],
) -> dict[int, tuple[Any, Any]]:
    """
    Create a dictionary with indexes as keys and zipped pairs as values.
    """
    return {
        index: pair
        for index, pair in enumerate(zip(keys, values))
    }