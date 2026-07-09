"""
Unit tests for loop_foundations.break_continue.

Run:

    pytest tests/test_break_continue.py

Author: Python Training
"""

from __future__ import annotations

from loop_foundations.break_continue import (
    find_first_even,
    first_duplicate,
    first_positive_number,
    placeholder_example,
    process_orders,
    process_valid_scores,
    remove_invalid_entries,
    search_student,
    skip_empty_strings,
    skip_negative_numbers,
    stop_at_value,
    validate_usernames,
)


# ============================================================================
# find_first_even()
# ============================================================================


def test_find_first_even_found() -> None:
    """Return first even number."""
    assert find_first_even([1, 3, 8, 10]) == 8


def test_find_first_even_not_found() -> None:
    """Return None when no even numbers exist."""
    assert find_first_even([1, 3, 5]) is None


# ============================================================================
# stop_at_value()
# ============================================================================


def test_stop_at_value_found() -> None:
    """Stop before target value."""
    assert stop_at_value([1, 2, 3, 4, 5], 4) == [1, 2, 3]


def test_stop_at_value_missing() -> None:
    """Return all values if target is missing."""
    assert stop_at_value([1, 2, 3], 10) == [1, 2, 3]


# ============================================================================
# skip_negative_numbers()
# ============================================================================


def test_skip_negative_numbers() -> None:
    """Remove negative numbers."""
    assert skip_negative_numbers([5, -1, 7, -3, 8]) == [5, 7, 8]


def test_skip_negative_numbers_all_negative() -> None:
    """Return empty list."""
    assert skip_negative_numbers([-1, -2, -3]) == []


# ============================================================================
# skip_empty_strings()
# ============================================================================


def test_skip_empty_strings() -> None:
    """Remove empty strings."""
    values = ["Python", "", "Django", "", "FastAPI"]

    assert skip_empty_strings(values) == [
        "Python",
        "Django",
        "FastAPI",
    ]


# ============================================================================
# search_student()
# ============================================================================


def test_search_student_found() -> None:
    """Student exists."""
    students = ["Alice", "Bob", "Charlie"]

    assert search_student(students, "Bob") is True


def test_search_student_not_found() -> None:
    """Student missing."""
    students = ["Alice", "Bob"]

    assert search_student(students, "David") is False


# ============================================================================
# process_valid_scores()
# ============================================================================


def test_process_valid_scores() -> None:
    """Keep only valid scores."""
    scores = [90, 120, 80, -5, 75]

    assert process_valid_scores(scores) == [
        90,
        80,
        75,
    ]


# ============================================================================
# process_orders()
# ============================================================================


def test_process_orders() -> None:
    """Process active orders only."""
    orders = [
        {"id": 1, "active": True},
        {"id": 2, "active": False},
        {"id": 3, "active": True},
    ]

    assert process_orders(orders) == [1, 3]


def test_process_orders_empty() -> None:
    """No orders."""
    assert process_orders([]) == []


# ============================================================================
# first_positive_number()
# ============================================================================


def test_first_positive_number_found() -> None:
    """Return first positive number."""
    assert first_positive_number([-5, -2, 4, 7]) == 4


def test_first_positive_number_missing() -> None:
    """Return None."""
    assert first_positive_number([-5, -2]) is None


# ============================================================================
# remove_invalid_entries()
# ============================================================================


def test_remove_invalid_entries() -> None:
    """Remove None and empty strings."""
    values = [
        None,
        "",
        "Python",
        10,
        False,
    ]

    assert remove_invalid_entries(values) == [
        "Python",
        10,
        False,
    ]


# ============================================================================
# placeholder_example()
# ============================================================================


def test_placeholder_example() -> None:
    """Pass statement example."""
    assert (
        placeholder_example()
        == "Loop completed successfully."
    )


# ============================================================================
# validate_usernames()
# ============================================================================


def test_validate_usernames() -> None:
    """Keep only valid usernames."""
    usernames = [
        "john",
        "python_dev",
        "hello world",
        "alice123",
    ]

    assert validate_usernames(usernames) == [
        "python_dev",
        "alice123",
    ]


def test_validate_usernames_empty() -> None:
    """Empty input."""
    assert validate_usernames([]) == []


# ============================================================================
# first_duplicate()
# ============================================================================


def test_first_duplicate_found() -> None:
    """Return first duplicate."""
    values = [1, 3, 5, 3, 8]

    assert first_duplicate(values) == 3


def test_first_duplicate_missing() -> None:
    """Return None."""
    values = [1, 2, 3]

    assert first_duplicate(values) is None