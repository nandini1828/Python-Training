"""
Examples demonstrating Python's reversed() and sorted() functions.

Topics covered:

- reversed()
- sorted()
- Custom sorting
- Reverse ordering
- Case-insensitive sorting

Author: Python Training
"""

from __future__ import annotations

from typing import Any


def reverse_list(items: list[Any]) -> list[Any]:
    """
    Reverse a list.

    Args:
        items:
            Input list.

    Returns:
        Reversed list.
    """
    return list(reversed(items))


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text:
            Input string.

    Returns:
        Reversed string.
    """
    return "".join(reversed(text))


def sort_numbers(
    numbers: list[int],
    descending: bool = False,
) -> list[int]:
    """
    Sort numbers.

    Args:
        numbers:
            Input numbers.

        descending:
            Sort in descending order.

    Returns:
        Sorted numbers.
    """
    return sorted(
        numbers,
        reverse=descending,
    )


def sort_strings_case_insensitive(
    values: list[str],
) -> list[str]:
    """
    Sort strings ignoring case.

    Args:
        values:
            Input strings.

    Returns:
        Sorted strings.
    """
    return sorted(
        values,
        key=str.lower,
    )


def sort_by_length(
    values: list[str],
) -> list[str]:
    """
    Sort strings by length.

    Args:
        values:
            Input strings.

    Returns:
        Length-sorted strings.
    """
    return sorted(
        values,
        key=len,
    )


def sort_dictionary_keys(
    data: dict[str, Any],
) -> list[str]:
    """
    Return sorted dictionary keys.

    Args:
        data:
            Input dictionary.

    Returns:
        Sorted keys.
    """
    return sorted(data.keys())


def sort_dictionary_values(
    data: dict[str, int],
) -> list[int]:
    """
    Return sorted dictionary values.

    Args:
        data:
            Input dictionary.

    Returns:
        Sorted values.
    """
    return sorted(data.values())


def sort_records_by_age(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Sort employee records by age.

    Args:
        records:
            Employee records.

    Returns:
        Sorted records.
    """
    return sorted(
        records,
        key=lambda record: record["age"],
    )


def sort_records_by_name(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Sort employee records by name.

    Args:
        records:
            Employee records.

    Returns:
        Sorted records.
    """
    return sorted(
        records,
        key=lambda record: record["name"].lower(),
    )


__all__ = [
    "reverse_list",
    "reverse_string",
    "sort_numbers",
    "sort_strings_case_insensitive",
    "sort_by_length",
    "sort_dictionary_keys",
    "sort_dictionary_values",
    "sort_records_by_age",
    "sort_records_by_name",
]