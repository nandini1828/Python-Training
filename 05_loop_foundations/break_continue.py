"""
Examples demonstrating Python loop control statements.

This module covers:
- break
- continue
- pass

These statements control loop execution and are commonly used in
searching, validation, filtering, and processing collections.

Author: Python Training
"""

from __future__ import annotations

from typing import Any


def find_first_even(numbers: list[int]) -> int | None:
    """
    Return the first even number.

    Args:
        numbers:
            List of integers.

    Returns:
        First even number if found, otherwise None.
    """
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


def stop_at_value(
    values: list[Any],
    target: Any,
) -> list[Any]:
    """
    Stop iterating once the target value is found.

    Args:
        values:
            Input list.

        target:
            Value that stops iteration.

    Returns:
        Elements visited before the target.
    """
    result: list[Any] = []

    for value in values:
        if value == target:
            break

        result.append(value)

    return result


def skip_negative_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Skip negative numbers.

    Args:
        numbers:
            Input numbers.

    Returns:
        Non-negative numbers.
    """
    result: list[int] = []

    for number in numbers:
        if number < 0:
            continue

        result.append(number)

    return result


def skip_empty_strings(
    values: list[str],
) -> list[str]:
    """
    Skip empty strings.

    Args:
        values:
            Input strings.

    Returns:
        Non-empty strings.
    """
    result: list[str] = []

    for value in values:
        if not value:
            continue

        result.append(value)

    return result


def search_student(
    students: list[str],
    name: str,
) -> bool:
    """
    Search for a student using break.

    Args:
        students:
            Student names.

        name:
            Student to search.

    Returns:
        True if found.
    """
    found = False

    for student in students:
        if student == name:
            found = True
            break

    return found


def process_valid_scores(
    scores: list[int],
) -> list[int]:
    """
    Ignore invalid scores.

    Valid scores are between 0 and 100.

    Args:
        scores:
            List of scores.

    Returns:
        Valid scores only.
    """
    result: list[int] = []

    for score in scores:
        if score < 0 or score > 100:
            continue

        result.append(score)

    return result


def process_orders(
    orders: list[dict[str, Any]],
) -> list[int]:
    """
    Process only valid orders.

    Args:
        orders:
            Order records.

    Returns:
        Valid order IDs.
    """
    processed: list[int] = []

    for order in orders:
        if not order.get("active", False):
            continue

        processed.append(order["id"])

    return processed


def first_positive_number(
    numbers: list[int],
) -> int | None:
    """
    Return first positive number.

    Args:
        numbers:
            Integer list.

    Returns:
        First positive number.
    """
    for number in numbers:
        if number > 0:
            return number

    return None


def remove_invalid_entries(
    values: list[Any],
) -> list[Any]:
    """
    Remove invalid values.

    Invalid values are

    - None
    - Empty string

    Args:
        values:
            Input values.

    Returns:
        Filtered values.
    """
    result: list[Any] = []

    for value in values:
        if value is None:
            continue

        if value == "":
            continue

        result.append(value)

    return result


def placeholder_example() -> str:
    """
    Demonstrate the pass statement.

    Returns:
        Placeholder message.
    """
    for _ in range(5):
        pass

    return "Loop completed successfully."


def validate_usernames(
    usernames: list[str],
) -> list[str]:
    """
    Validate usernames.

    Rules

    - Minimum length 5
    - No spaces

    Args:
        usernames:
            Input usernames.

    Returns:
        Valid usernames.
    """
    valid: list[str] = []

    for username in usernames:
        if len(username) < 5:
            continue

        if " " in username:
            continue

        valid.append(username)

    return valid


def first_duplicate(
    values: list[Any],
) -> Any | None:
    """
    Return first duplicate element.

    Args:
        values:
            Input list.

    Returns:
        Duplicate element if found.
    """
    seen: set[Any] = set()

    for value in values:
        if value in seen:
            return value

        seen.add(value)

    return None


__all__ = [
    "find_first_even",
    "stop_at_value",
    "skip_negative_numbers",
    "skip_empty_strings",
    "search_student",
    "process_valid_scores",
    "process_orders",
    "first_positive_number",
    "remove_invalid_entries",
    "placeholder_example",
    "validate_usernames",
    "first_duplicate",
]