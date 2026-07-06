"""
Examples demonstrating safe list iteration.

Topics covered:

- Safe removal
- Safe filtering
- Copy iteration
- List rebuilding
- Duplicate removal

Author: Python Training
"""

from __future__ import annotations


def remove_negative_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Remove negative numbers safely.

    Args:
        numbers:
            Input list.

    Returns:
        New list without negative values.
    """
    return [
        number
        for number in numbers
        if number >= 0
    ]


def filter_even_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Return only even numbers.

    Args:
        numbers:
            Input list.

    Returns:
        Even numbers.
    """
    return [
        number
        for number in numbers
        if number % 2 == 0
    ]


def remove_duplicates(
    values: list[int],
) -> list[int]:
    """
    Remove duplicate values while preserving order.

    Args:
        values:
            Input values.

    Returns:
        Unique values.
    """
    seen: set[int] = set()

    return [
        value
        for value in values
        if not (
            value in seen
            or seen.add(value)
        )
    ]


def remove_even_in_place(
    numbers: list[int],
) -> list[int]:
    """
    Safely remove even numbers by iterating over a copy.

    Args:
        numbers:
            Input list.

    Returns:
        Modified list.
    """
    result = numbers.copy()

    for number in result[:]:
        if number % 2 == 0:
            result.remove(number)

    return result


def remove_empty_strings(
    values: list[str],
) -> list[str]:
    """
    Remove empty strings.

    Args:
        values:
            Input values.

    Returns:
        Clean list.
    """
    return [
        value
        for value in values
        if value
    ]


def replace_negative_with_zero(
    numbers: list[int],
) -> list[int]:
    """
    Replace negative numbers with zero.

    Args:
        numbers:
            Input list.

    Returns:
        Updated list.
    """
    return [
        0
        if number < 0
        else number
        for number in numbers
    ]


def snapshot_iteration(
    values: list[int],
) -> list[int]:
    """
    Iterate over a snapshot of a list.

    Args:
        values:
            Input list.

    Returns:
        Snapshot.
    """
    return [
        value
        for value in values.copy()
    ]


__all__ = [
    "remove_negative_numbers",
    "filter_even_numbers",
    "remove_duplicates",
    "remove_even_in_place",
    "remove_empty_strings",
    "replace_negative_with_zero",
    "snapshot_iteration",
]