"""
Unit tests for mutation_patterns.py

Run:

    pytest tests/test_mutation_patterns.py
"""

from __future__ import annotations

from iteration_safety.mutation_patterns import (
    filter_positive_numbers,
    increment_values,
    merge_lists,
    normalize_strings,
    remove_duplicates,
    replace_negative_numbers,
    safe_update_dictionary,
)


def test_filter_positive_numbers() -> None:
    """Positive filter."""
    assert filter_positive_numbers(
        [-2, -1, 3, 5]
    ) == [
        3,
        5,
    ]


def test_replace_negative_numbers() -> None:
    """Replacement."""
    assert replace_negative_numbers(
        [-5, 2, -3]
    ) == [
        0,
        2,
        0,
    ]


def test_increment_values() -> None:
    """Increment."""
    assert increment_values(
        [1, 2, 3]
    ) == [
        2,
        3,
        4,
    ]


def test_normalize_strings() -> None:
    """Normalize."""
    assert normalize_strings(
        [
            " Python ",
            " DJANGO ",
        ]
    ) == [
        "python",
        "django",
    ]


def test_merge_lists() -> None:
    """Merge."""
    assert merge_lists(
        [1, 2],
        [3, 4],
    ) == [
        1,
        2,
        3,
        4,
    ]


def test_remove_duplicates() -> None:
    """Duplicate removal."""
    assert remove_duplicates(
        [1, 2, 2, 3, 4, 4]
    ) == [
        1,
        2,
        3,
        4,
    ]


def test_safe_update_dictionary() -> None:
    """Dictionary update."""
    result = safe_update_dictionary(
        {"A": 1},
        {"B": 2},
    )

    assert result == {
        "A": 1,
        "B": 2,
    }