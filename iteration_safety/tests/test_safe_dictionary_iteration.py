"""
Unit tests for safe_dictionary_iteration.py

Run:

    pytest tests/test_safe_dictionary_iteration.py
"""

from __future__ import annotations

from iteration_safety.safe_dictionary_iteration import (
    filter_positive_values,
    lowercase_values,
    remove_empty_values,
    remove_keys,
    snapshot_items,
    snapshot_keys,
    uppercase_keys,
)


def test_remove_empty_values() -> None:
    """Remove empty values."""
    data = {
        "A": "Python",
        "B": "",
        "C": "Django",
    }

    assert remove_empty_values(data) == {
        "A": "Python",
        "C": "Django",
    }


def test_remove_keys() -> None:
    """Remove selected keys."""
    assert remove_keys(
        {
            "A": 1,
            "B": 2,
            "C": 3,
        },
        ["B"],
    ) == {
        "A": 1,
        "C": 3,
    }


def test_uppercase_keys() -> None:
    """Uppercase keys."""
    assert uppercase_keys(
        {
            "name": "Alice",
        }
    ) == {
        "NAME": "Alice",
    }


def test_lowercase_values() -> None:
    """Lowercase values."""
    assert lowercase_values(
        {
            "Language": "PYTHON",
        }
    ) == {
        "Language": "python",
    }


def test_filter_positive_values() -> None:
    """Positive filtering."""
    assert filter_positive_values(
        {
            "A": 5,
            "B": -1,
            "C": 10,
        }
    ) == {
        "A": 5,
        "C": 10,
    }


def test_snapshot_keys() -> None:
    """Snapshot keys."""
    result = snapshot_keys(
        {
            "A": 1,
            "B": 2,
        }
    )

    assert result == [
        "A",
        "B",
    ]


def test_snapshot_items() -> None:
    """Snapshot items."""
    result = snapshot_items(
        {
            "A": 1,
            "B": 2,
        }
    )

    assert result == [
        ("A", 1),
        ("B", 2),
    ]


def test_empty_dictionary() -> None:
    """Empty dictionary."""
    assert remove_empty_values({}) == {}