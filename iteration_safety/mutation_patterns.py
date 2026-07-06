"""
Examples demonstrating safe mutation patterns.

Topics covered:

- Filtering
- Transformation
- Copy-on-write
- Safe replacement
- Immutable-style updates

Author: Python Training
"""

from __future__ import annotations


def filter_positive_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Keep only positive numbers.

    Args:
        numbers:
            Input list.

    Returns:
        Positive numbers.
    """
    return [
        number
        for number in numbers
        if number > 0
    ]


def replace_negative_numbers(
    numbers: list[int],
    replacement: int = 0,
) -> list[int]:
    """
    Replace negative numbers.

    Args:
        numbers:
            Input list.

        replacement:
            Replacement value.

    Returns:
        Updated list.
    """
    return [
        replacement
        if number < 0
        else number
        for number in numbers
    ]


def increment_values(
    numbers: list[int],
) -> list[int]:
    """
    Increment every value.

    Args:
        numbers:
            Input list.

    Returns:
        Incremented values.
    """
    return [
        number + 1
        for number in numbers
    ]


def normalize_strings(
    words: list[str],
) -> list[str]:
    """
    Normalize strings.

    Args:
        words:
            Input words.

    Returns:
        Normalized words.
    """
    return [
        word.strip().lower()
        for word in words
    ]


def merge_lists(
    first: list[int],
    second: list[int],
) -> list[int]:
    """
    Merge two lists.

    Args:
        first:
            First list.

        second:
            Second list.

    Returns:
        Combined list.
    """
    return [
        *first,
        *second,
    ]


def remove_duplicates(
    values: list[int],
) -> list[int]:
    """
    Remove duplicate values.

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


def safe_update_dictionary(
    data: dict[str, int],
    updates: dict[str, int],
) -> dict[str, int]:
    """
    Return an updated dictionary.

    Args:
        data:
            Original dictionary.

        updates:
            New values.

    Returns:
        Updated copy.
    """
    result = data.copy()
    result.update(updates)

    return result


__all__ = [
    "filter_positive_numbers",
    "replace_negative_numbers",
    "increment_values",
    "normalize_strings",
    "merge_lists",
    "remove_duplicates",
    "safe_update_dictionary",
]