"""
Unit tests for safe_list_iteration.py

Run:

    pytest tests/test_safe_list_iteration.py
"""

from __future__ import annotations

from iteration_safety.safe_list_iteration import (
    filter_even_numbers,
    remove_duplicates,
    remove_empty_strings,
    remove_even_in_place,
    remove_negative_numbers,
    replace_negative_with_zero,
    snapshot_iteration,
)


def test_remove_negative_numbers() -> None:
    """Remove negatives."""
    assert remove_negative_numbers(
        [-2, -1, 0, 1, 2]
    ) == [
        0,
        1,
        2,
    ]


def test_filter_even_numbers() -> None:
    """Even numbers."""
    assert filter_even_numbers(
        [1, 2, 3, 4, 5, 6]
    ) == [
        2,
        4,
        6,
    ]


def test_remove_duplicates() -> None:
    """Duplicate removal."""
    assert remove_duplicates(
        [1, 2, 2, 3, 3, 4]
    ) == [
        1,
        2,
        3,
        4,
    ]


def test_remove_even_in_place() -> None:
    """Safe removal."""
    assert remove_even_in_place(
        [1, 2, 3, 4, 5, 6]
    ) == [
        1,
        3,
        5,
    ]


def test_remove_empty_strings() -> None:
    """Empty strings."""
    assert remove_empty_strings(
        [
            "Python",
            "",
            "Django",
            "",
        ]
    ) == [
        "Python",
        "Django",
    ]


def test_replace_negative_with_zero() -> None:
    """Replacement."""
    assert replace_negative_with_zero(
        [-5, 2, -3]
    ) == [
        0,
        2,
        0,
    ]


def test_snapshot_iteration() -> None:
    """Snapshot copy."""
    values = [1, 2, 3]

    assert snapshot_iteration(values) == values
    assert snapshot_iteration(values) is not values


def test_empty_lists() -> None:
    """Empty inputs."""
    assert remove_negative_numbers([]) == []
    assert remove_duplicates([]) == []