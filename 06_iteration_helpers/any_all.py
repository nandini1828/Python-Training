"""
Examples demonstrating Python's any() and all() functions.

Topics covered:

- any()
- all()
- Validation
- Membership checks
- Boolean evaluation

Author: Python Training
"""

from __future__ import annotations


def any_even(numbers: list[int]) -> bool:
    """
    Check whether any number is even.

    Args:
        numbers:
            Input numbers.

    Returns:
        True if an even number exists.
    """
    return any(
        number % 2 == 0
        for number in numbers
    )


def all_even(numbers: list[int]) -> bool:
    """
    Check whether all numbers are even.

    Args:
        numbers:
            Input numbers.

    Returns:
        True if all numbers are even.
    """
    return all(
        number % 2 == 0
        for number in numbers
    )


def any_negative(numbers: list[int]) -> bool:
    """
    Check whether any number is negative.

    Args:
        numbers:
            Input numbers.

    Returns:
        True if a negative number exists.
    """
    return any(
        number < 0
        for number in numbers
    )


def all_positive(numbers: list[int]) -> bool:
    """
    Check whether all numbers are positive.

    Args:
        numbers:
            Input numbers.

    Returns:
        True if all numbers are positive.
    """
    return all(
        number > 0
        for number in numbers
    )


def contains_admin(
    users: list[str],
) -> bool:
    """
    Check whether 'admin' exists.

    Args:
        users:
            Usernames.

    Returns:
        Membership result.
    """
    return any(
        user.lower() == "admin"
        for user in users
    )


def all_strings_non_empty(
    values: list[str],
) -> bool:
    """
    Check whether all strings are non-empty.

    Args:
        values:
            Input strings.

    Returns:
        Validation result.
    """
    return all(values)


def any_empty_string(
    values: list[str],
) -> bool:
    """
    Check whether any string is empty.

    Args:
        values:
            Input strings.

    Returns:
        Validation result.
    """
    return any(
        value == ""
        for value in values
    )


def all_scores_valid(
    scores: list[int],
) -> bool:
    """
    Validate score range.

    Args:
        scores:
            Student scores.

    Returns:
        True if all scores are between
        0 and 100.
    """
    return all(
        0 <= score <= 100
        for score in scores
    )


def any_failed(
    scores: list[int],
    passing_score: int = 35,
) -> bool:
    """
    Determine whether any student failed.

    Args:
        scores:
            Student scores.

        passing_score:
            Minimum passing score.

    Returns:
        True if any score is below
        the passing score.
    """
    return any(
        score < passing_score
        for score in scores
    )


def all_files_exist(
    file_status: list[bool],
) -> bool:
    """
    Check whether every file exists.

    Args:
        file_status:
            File existence flags.

    Returns:
        Validation result.
    """
    return all(file_status)


__all__ = [
    "any_even",
    "all_even",
    "any_negative",
    "all_positive",
    "contains_admin",
    "all_strings_non_empty",
    "any_empty_string",
    "all_scores_valid",
    "any_failed",
    "all_files_exist",
]