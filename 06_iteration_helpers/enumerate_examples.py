"""
Examples demonstrating Python's built-in enumerate() function.

Topics covered:

- Basic enumerate()
- Custom start index
- Enumerating strings
- Enumerating dictionaries
- Row numbering
- Ranking
- Report generation

Author: Python Training
"""

from __future__ import annotations

from typing import Any


def enumerate_list(items: list[Any]) -> list[tuple[int, Any]]:
    """
    Enumerate a list starting at zero.

    Args:
        items:
            Input list.

    Returns:
        List of (index, value) tuples.
    """
    return list(enumerate(items))


def enumerate_list_start(
    items: list[Any],
    start: int,
) -> list[tuple[int, Any]]:
    """
    Enumerate a list using a custom starting index.

    Args:
        items:
            Input list.

        start:
            Starting index.

    Returns:
        Enumerated list.
    """
    return list(enumerate(items, start=start))


def enumerate_string(text: str) -> list[tuple[int, str]]:
    """
    Enumerate the characters of a string.

    Args:
        text:
            Input string.

    Returns:
        Character positions.
    """
    return list(enumerate(text))


def indexed_students(
    students: list[str],
) -> list[str]:
    """
    Create numbered student records.

    Args:
        students:
            Student names.

    Returns:
        Numbered students.
    """
    return [
        f"{index}. {student}"
        for index, student in enumerate(
            students,
            start=1,
        )
    ]


def enumerate_dictionary_keys(
    data: dict[str, Any],
) -> list[tuple[int, str]]:
    """
    Enumerate dictionary keys.

    Args:
        data:
            Input dictionary.

    Returns:
        Enumerated keys.
    """
    return list(enumerate(data.keys()))


def enumerate_dictionary_values(
    data: dict[str, Any],
) -> list[tuple[int, Any]]:
    """
    Enumerate dictionary values.

    Args:
        data:
            Input dictionary.

    Returns:
        Enumerated values.
    """
    return list(enumerate(data.values()))


def enumerate_dictionary_items(
    data: dict[str, Any],
) -> list[tuple[int, tuple[str, Any]]]:
    """
    Enumerate dictionary items.

    Args:
        data:
            Input dictionary.

    Returns:
        Enumerated key-value pairs.
    """
    return list(enumerate(data.items()))


def employee_report(
    employees: list[str],
) -> list[str]:
    """
    Generate a numbered employee report.

    Args:
        employees:
            Employee names.

    Returns:
        Formatted report.
    """
    report: list[str] = []

    for number, employee in enumerate(
        employees,
        start=1,
    ):
        report.append(
            f"Employee {number}: {employee}"
        )

    return report


def ranked_scores(
    scores: list[int],
) -> list[tuple[int, int]]:
    """
    Assign rankings to scores.

    Args:
        scores:
            Score list.

    Returns:
        Ranked scores.
    """
    return list(
        enumerate(
            scores,
            start=1,
        )
    )


def csv_rows(
    rows: list[list[str]],
) -> list[str]:
    """
    Number CSV rows.

    Args:
        rows:
            CSV records.

    Returns:
        Numbered rows.
    """
    result: list[str] = []

    for row_number, row in enumerate(
        rows,
        start=1,
    ):
        result.append(
            f"Row {row_number}: {row}"
        )

    return result


def find_occurrences(
    values: list[Any],
    target: Any,
) -> list[int]:
    """
    Find every occurrence of a value.

    Args:
        values:
            Input list.

        target:
            Value to locate.

    Returns:
        Matching indices.
    """
    indices: list[int] = []

    for index, value in enumerate(values):
        if value == target:
            indices.append(index)

    return indices


def enumerate_words(
    sentence: str,
) -> list[tuple[int, str]]:
    """
    Enumerate words in a sentence.

    Args:
        sentence:
            Input sentence.

    Returns:
        Enumerated words.
    """
    words = sentence.split()

    return list(
        enumerate(
            words,
            start=1,
        )
    )


def inventory_report(
    inventory: dict[str, int],
) -> list[str]:
    """
    Create a numbered inventory report.

    Args:
        inventory:
            Product inventory.

    Returns:
        Formatted inventory report.
    """
    report: list[str] = []

    for index, (product, quantity) in enumerate(
        inventory.items(),
        start=1,
    ):
        report.append(
            f"{index}. {product} ({quantity})"
        )

    return report


__all__ = [
    "enumerate_list",
    "enumerate_list_start",
    "enumerate_string",
    "indexed_students",
    "enumerate_dictionary_keys",
    "enumerate_dictionary_values",
    "enumerate_dictionary_items",
    "employee_report",
    "ranked_scores",
    "csv_rows",
    "find_occurrences",
    "enumerate_words",
    "inventory_report",
]