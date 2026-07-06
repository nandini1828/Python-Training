"""
Examples demonstrating Python dictionary comprehensions.

Topics covered:

- Basic dictionary comprehensions
- Filtering
- Transformations
- Dynamic mappings

Author: Python Training
"""

from __future__ import annotations


def number_squares(limit: int) -> dict[int, int]:
    """
    Map numbers to their squares.

    Args:
        limit:
            Upper limit.

    Returns:
        Dictionary of squares.
    """
    return {
        number: number**2
        for number in range(limit)
    }


def word_lengths(
    words: list[str],
) -> dict[str, int]:
    """
    Map words to their lengths.

    Args:
        words:
            Input words.

    Returns:
        Word lengths.
    """
    return {
        word: len(word)
        for word in words
    }


def employee_salary_map(
    employees: list[str],
    salaries: list[int],
) -> dict[str, int]:
    """
    Create employee salary mapping.

    Args:
        employees:
            Employee names.

        salaries:
            Salaries.

    Returns:
        Employee salary dictionary.
    """
    return {
        employee: salary
        for employee, salary in zip(
            employees,
            salaries,
        )
    }


def even_square_map(
    limit: int,
) -> dict[int, int]:
    """
    Map even numbers to their squares.

    Args:
        limit:
            Upper limit.

    Returns:
        Dictionary of squares.
    """
    return {
        number: number**2
        for number in range(limit)
        if number % 2 == 0
    }


def uppercase_keys(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Convert dictionary keys to uppercase.

    Args:
        data:
            Input dictionary.

    Returns:
        Updated dictionary.
    """
    return {
        key.upper(): value
        for key, value in data.items()
    }


def lowercase_values(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Convert dictionary values to lowercase.

    Args:
        data:
            Input dictionary.

    Returns:
        Updated dictionary.
    """
    return {
        key: value.lower()
        for key, value in data.items()
    }


def invert_dictionary(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Swap keys and values.

    Args:
        data:
            Input dictionary.

    Returns:
        Inverted dictionary.
    """
    return {
        value: key
        for key, value in data.items()
    }


def filter_positive(
    data: dict[str, int],
) -> dict[str, int]:
    """
    Keep only positive values.

    Args:
        data:
            Input dictionary.

    Returns:
        Filtered dictionary.
    """
    return {
        key: value
        for key, value in data.items()
        if value > 0
    }


def grade_book(
    students: dict[str, int],
) -> dict[str, str]:
    """
    Convert marks into grades.

    Args:
        students:
            Student marks.

    Returns:
        Student grades.
    """
    return {
        student: (
            "Pass"
            if marks >= 35
            else "Fail"
        )
        for student, marks in students.items()
    }


__all__ = [
    "number_squares",
    "word_lengths",
    "employee_salary_map",
    "even_square_map",
    "uppercase_keys",
    "lowercase_values",
    "invert_dictionary",
    "filter_positive",
    "grade_book",
]