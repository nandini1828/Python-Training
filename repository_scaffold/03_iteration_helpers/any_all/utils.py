"""
utils.py

Reusable utility functions demonstrating Python's built-in any() and all() functions.
"""

from typing import Any


def any_truthy(values: list[Any]) -> bool:
    """
    Return True if at least one value is truthy.
    """
    return any(values)


def all_truthy(values: list[Any]) -> bool:
    """
    Return True if all values are truthy.
    """
    return all(values)


def any_positive(numbers: list[int]) -> bool:
    """
    Return True if at least one number is positive.
    """
    return any(number > 0 for number in numbers)


def all_positive(numbers: list[int]) -> bool:
    """
    Return True if all numbers are positive.
    """
    return all(number > 0 for number in numbers)


def all_even(numbers: list[int]) -> bool:
    """
    Return True if all numbers are even.
    """
    return all(number % 2 == 0 for number in numbers)


def any_empty_string(strings: list[str]) -> bool:
    """
    Return True if any string is empty.
    """
    return any(not string for string in strings)


def all_passwords_valid(passwords: list[str], minimum_length: int = 8) -> bool:
    """
    Return True if all passwords meet the minimum length.
    """
    return all(len(password) >= minimum_length for password in passwords)


def any_text_file(files: list[str]) -> bool:
    """
    Return True if any filename ends with '.txt'.
    """
    return any(file.endswith(".txt") for file in files)


def has_required_fields(
    data: dict[str, Any],
    required_fields: list[str],
) -> bool:
    """
    Return True if all required fields exist in the dictionary.
    """
    return all(field in data for field in required_fields)


def has_permissions(
    user_permissions: list[str],
    required_permissions: list[str],
) -> bool:
    """
    Return True if all required permissions are available.
    """
    return all(
        permission in user_permissions
        for permission in required_permissions
    )