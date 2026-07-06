"""
Unit tests for safe_set_iteration.py

Run:

    pytest tests/test_safe_set_iteration.py
"""

from __future__ import annotations

from iteration_safety.safe_set_iteration import (
    common_values,
    filter_even_set,
    remove_small_values,
    safe_remove,
    snapshot_iteration,
    unique_values,
    uppercase_words,
)


def test_filter_even_set() -> None:
    """Even values."""
    assert filter_even_set(
        {
            1,
            2,
            3,
            4,
            5,
            6,
        }
    ) == {
        2,
        4,
        6,
    }


def test_remove_small_values() -> None:
    """Minimum filter."""
    assert remove_small_values(
        {
            1,
            2,
            3,
            4,
            5,
        },
        3,
    ) == {
        3,
        4,
        5,
    }


def test_uppercase_words() -> None:
    """Uppercase words."""
    assert uppercase_words(
        {
            "python",
            "django",
        }
    ) == {
        "PYTHON",
        "DJANGO",
    }


def test_safe_remove() -> None:
    """Safe removal."""
    assert safe_remove(
        {
            1,
            2,
            3,
        },
        2,
    ) == {
        1,
        3,
    }


def test_snapshot_iteration() -> None:
    """Snapshot copy."""
    values = {
        1,
        2,
        3,
    }

    result = snapshot_iteration(values)

    assert sorted(result) == [
        1,
        2,
        3,
    ]


def test_common_values() -> None:
    """Intersection."""
    assert common_values(
        {
            1,
            2,
            3,
        },
        {
            2,
            3,
            4,
        },
    ) == {
        2,
        3,
    }


def test_unique_values() -> None:
    """Difference."""
    assert unique_values(
        {
            1,
            2,
            3,
        },
        {
            2,
        },
    ) == {
        1,
        3,
    }