"""
utils.py

Reusable utility functions demonstrating Python's built-in sorted() function.
"""

from typing import Any


def sort_numbers(numbers: list[int]) -> list[int]:
    """
    Return numbers sorted in ascending order.
    """
    return sorted(numbers)


def sort_numbers_descending(numbers: list[int]) -> list[int]:
    """
    Return numbers sorted in descending order.
    """
    return sorted(numbers, reverse=True)


def sort_strings(strings: list[str]) -> list[str]:
    """
    Return strings sorted alphabetically.
    """
    return sorted(strings)


def sort_by_length(items: list[str]) -> list[str]:
    """
    Return strings sorted by length.
    """
    return sorted(items, key=len)


def sort_dictionary_keys(data: dict[Any, Any]) -> list[Any]:
    """
    Return dictionary keys in sorted order.
    """
    return sorted(data.keys())


def sort_dictionary_items(data: dict[Any, Any]) -> list[tuple[Any, Any]]:
    """
    Return dictionary items sorted by key.
    """
    return sorted(data.items())


def sort_tuples(items: list[tuple[Any, ...]]) -> list[tuple[Any, ...]]:
    """
    Return tuples sorted in ascending order.
    """
    return sorted(items)


def sort_students_by_marks(
    students: list[tuple[str, int]],
    reverse: bool = True,
) -> list[tuple[str, int]]:
    """
    Return students sorted by marks.
    """
    return sorted(
        students,
        key=lambda student: student[1],
        reverse=reverse,
    )


def case_insensitive_sort(strings: list[str]) -> list[str]:
    """
    Return strings sorted without considering letter case.
    """
    return sorted(strings, key=str.lower)


def sort_set(values: set[Any]) -> list[Any]:
    """
    Return a sorted list from a set.
    """
    return sorted(values)