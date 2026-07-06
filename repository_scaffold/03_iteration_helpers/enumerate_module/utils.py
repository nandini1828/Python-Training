"""
utils.py

Reusable utility functions demonstrating Python's built-in enumerate() function.
"""

from typing import Any


def enumerate_items(items: list[Any]) -> list[tuple[int, Any]]:
    """
    Return a list of (index, value) pairs.
    """
    return list(enumerate(items))


def enumerate_with_start(items: list[Any], start: int) -> list[tuple[int, Any]]:
    """
    Return enumerated items starting from a custom index.
    """
    return list(enumerate(items, start=start))


def create_index_dictionary(items: list[Any]) -> dict[int, Any]:
    """
    Create a dictionary using indexes as keys.
    """
    return {index: value for index, value in enumerate(items)}


def find_item_index(items: list[Any], target: Any) -> int:
    """
    Return the index of the target item.
    Returns -1 if not found.
    """
    for index, value in enumerate(items):
        if value == target:
            return index

    return -1


def number_lines(lines: list[str]) -> list[str]:
    """
    Return numbered lines starting from 1.
    """
    return [
        f"{line_number}. {line}"
        for line_number, line in enumerate(lines, start=1)
    ]


def enumerate_characters(text: str) -> list[tuple[int, str]]:
    """
    Return (index, character) pairs for a string.
    """
    return list(enumerate(text))


def enumerate_tuple(items: tuple[Any, ...]) -> list[tuple[int, Any]]:
    """
    Return enumerated tuple elements.
    """
    return list(enumerate(items))


def create_student_records(students: list[str], start_roll: int = 1) -> dict[int, str]:
    """
    Create student records with roll numbers.
    """
    return {
        roll: student
        for roll, student in enumerate(students, start=start_roll)
    }


def even_index_items(items: list[Any]) -> list[Any]:
    """
    Return elements located at even indexes.
    """
    return [
        value
        for index, value in enumerate(items)
        if index % 2 == 0
    ]


def odd_index_items(items: list[Any]) -> list[Any]:
    """
    Return elements located at odd indexes.
    """
    return [
        value
        for index, value in enumerate(items)
        if index % 2 != 0
    ]