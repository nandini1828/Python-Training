"""
Examples demonstrating Python's zip() function.

Topics covered:

- zip()
- itertools.zip_longest()
- Parallel iteration
- Dictionary creation
- Unzipping
- Employee record creation

Author: Python Training
"""

from __future__ import annotations

from itertools import zip_longest
from typing import Any


def zip_lists(
    first: list[Any],
    second: list[Any],
) -> list[tuple[Any, Any]]:
    """
    Zip two lists.

    Args:
        first:
            First list.

        second:
            Second list.

    Returns:
        Zipped list.
    """
    return list(zip(first, second))


def zip_three_lists(
    first: list[Any],
    second: list[Any],
    third: list[Any],
) -> list[tuple[Any, Any, Any]]:
    """
    Zip three lists.

    Args:
        first:
            First list.

        second:
            Second list.

        third:
            Third list.

    Returns:
        Zipped values.
    """
    return list(zip(first, second, third))


def zip_longest_lists(
    first: list[Any],
    second: list[Any],
    fill_value: Any = None,
) -> list[tuple[Any, Any]]:
    """
    Zip two unequal lists.

    Args:
        first:
            First list.

        second:
            Second list.

        fill_value:
            Replacement value.

    Returns:
        Zipped values.
    """
    return list(
        zip_longest(
            first,
            second,
            fillvalue=fill_value,
        )
    )


def create_dictionary(
    keys: list[str],
    values: list[Any],
) -> dict[str, Any]:
    """
    Create dictionary using zip.

    Args:
        keys:
            Dictionary keys.

        values:
            Dictionary values.

    Returns:
        Dictionary.
    """
    return dict(zip(keys, values))


def unzip_pairs(
    pairs: list[tuple[Any, Any]],
) -> tuple[list[Any], list[Any]]:
    """
    Unzip paired values.

    Args:
        pairs:
            Paired values.

    Returns:
        Two separate lists.
    """
    if not pairs:
        return [], []

    first, second = zip(*pairs)

    return list(first), list(second)


def combine_employee_records(
    names: list[str],
    departments: list[str],
) -> list[dict[str, str]]:
    """
    Combine employee data.

    Args:
        names:
            Employee names.

        departments:
            Department names.

    Returns:
        Employee records.
    """
    records: list[dict[str, str]] = []

    for name, department in zip(
        names,
        departments,
    ):
        records.append(
            {
                "name": name,
                "department": department,
            }
        )

    return records


def merge_student_marks(
    students: list[str],
    marks: list[int],
) -> list[str]:
    """
    Merge student names with marks.

    Args:
        students:
            Student names.

        marks:
            Student marks.

    Returns:
        Formatted results.
    """
    result: list[str] = []

    for student, mark in zip(
        students,
        marks,
    ):
        result.append(
            f"{student}: {mark}"
        )

    return result


def parallel_sum(
    first: list[int],
    second: list[int],
) -> list[int]:
    """
    Add corresponding values.

    Args:
        first:
            First list.

        second:
            Second list.

    Returns:
        Summed values.
    """
    return [
        left + right
        for left, right in zip(
            first,
            second,
        )
    ]


def compare_lists(
    first: list[Any],
    second: list[Any],
) -> list[bool]:
    """
    Compare corresponding values.

    Args:
        first:
            First list.

        second:
            Second list.

    Returns:
        Comparison results.
    """
    return [
        left == right
        for left, right in zip(
            first,
            second,
        )
    ]


def transpose_matrix(
    matrix: list[list[Any]],
) -> list[tuple[Any, ...]]:
    """
    Transpose a matrix.

    Args:
        matrix:
            Two-dimensional list.

    Returns:
        Transposed matrix.
    """
    if not matrix:
        return []

    return list(zip(*matrix))


__all__ = [
    "zip_lists",
    "zip_three_lists",
    "zip_longest_lists",
    "create_dictionary",
    "unzip_pairs",
    "combine_employee_records",
    "merge_student_marks",
    "parallel_sum",
    "compare_lists",
    "transpose_matrix",
]