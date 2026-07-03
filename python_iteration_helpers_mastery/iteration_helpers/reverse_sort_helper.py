"""
reversed() and sorted() helper functions.
"""

from typing import Any


def reverse_items(items: list[Any]) -> list[Any]:
    """
    Returns items in reverse order using reversed().

    Parameters
    ----------
    items : list[Any]
        Input list.

    Returns
    -------
    list[Any]
        Reversed list.
    """
    return list(reversed(items))


def sort_numbers(numbers: list[int]) -> list[int]:
    """
    Returns numbers sorted in ascending order.

    Parameters
    ----------
    numbers : list[int]
        List of integers.

    Returns
    -------
    list[int]
        Sorted integers.
    """
    return sorted(numbers)


def sort_records_by_key(records: list[dict[str, Any]], key_name: str) -> list[dict[str, Any]]:
    """
    Sorts a list of dictionaries by a specific key using sorted().

    Parameters
    ----------
    records : list[dict[str, Any]]
        List of dictionary records.
    key_name : str
        Key to sort by.

    Returns
    -------
    list[dict[str, Any]]
        Sorted records.
    """
    return sorted(records, key=lambda record: record[key_name])