"""
Unit tests for iteration_helpers.any_all.

Run:

    pytest tests/test_any_all.py

Author: Python Training
"""

from __future__ import annotations

from iteration_helpers.any_all import (
    all_even,
    all_files_exist,
    all_positive,
    all_scores_valid,
    all_strings_non_empty,
    any_empty_string,
    any_even,
    any_failed,
    any_negative,
    contains_admin,
)


def test_any_even_true() -> None:
    """At least one even number."""
    assert any_even([1, 3, 4]) is True


def test_any_even_false() -> None:
    """No even numbers."""
    assert any_even([1, 3, 5]) is False


def test_all_even_true() -> None:
    """All numbers are even."""
    assert all_even([2, 4, 6]) is True


def test_all_even_false() -> None:
    """Mixed numbers."""
    assert all_even([2, 3, 4]) is False


def test_any_negative_true() -> None:
    """Negative number exists."""
    assert any_negative([5, -1, 10]) is True


def test_any_negative_false() -> None:
    """No negative numbers."""
    assert any_negative([5, 8, 10]) is False


def test_all_positive_true() -> None:
    """All positive."""
    assert all_positive([1, 2, 3]) is True


def test_all_positive_false() -> None:
    """Contains zero."""
    assert all_positive([1, 0, 3]) is False


def test_contains_admin_true() -> None:
    """Admin exists."""
    assert contains_admin(
        [
            "guest",
            "Admin",
            "user",
        ]
    ) is True


def test_contains_admin_false() -> None:
    """Admin missing."""
    assert contains_admin(
        [
            "guest",
            "user",
        ]
    ) is False


def test_all_strings_non_empty_true() -> None:
    """Every string has content."""
    assert all_strings_non_empty(
        [
            "Python",
            "Django",
        ]
    ) is True


def test_all_strings_non_empty_false() -> None:
    """Contains an empty string."""
    assert all_strings_non_empty(
        [
            "Python",
            "",
        ]
    ) is False


def test_any_empty_string_true() -> None:
    """Empty string exists."""
    assert any_empty_string(
        [
            "",
            "Python",
        ]
    ) is True


def test_any_empty_string_false() -> None:
    """No empty strings."""
    assert any_empty_string(
        [
            "Python",
            "Django",
        ]
    ) is False


def test_all_scores_valid_true() -> None:
    """All scores are valid."""
    assert all_scores_valid(
        [95, 82, 70]
    ) is True


def test_all_scores_valid_false() -> None:
    """Invalid score exists."""
    assert all_scores_valid(
        [95, 105, 70]
    ) is False


def test_any_failed_true() -> None:
    """Student failed."""
    assert any_failed(
        [90, 25, 80]
    ) is True


def test_any_failed_false() -> None:
    """No failures."""
    assert any_failed(
        [90, 80, 70]
    ) is False


def test_all_files_exist_true() -> None:
    """Every file exists."""
    assert all_files_exist(
        [True, True, True]
    ) is True


def test_all_files_exist_false() -> None:
    """Missing file."""
    assert all_files_exist(
        [True, False, True]
    ) is False