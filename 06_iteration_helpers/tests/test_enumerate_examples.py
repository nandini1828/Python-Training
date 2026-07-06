"""
Unit tests for iteration_helpers.enumerate_examples.

Run:

    pytest tests/test_enumerate_examples.py

Author: Python Training
"""

from __future__ import annotations

from iteration_helpers.enumerate_examples import (
    csv_rows,
    employee_report,
    enumerate_dictionary_items,
    enumerate_dictionary_keys,
    enumerate_dictionary_values,
    enumerate_list,
    enumerate_list_start,
    enumerate_string,
    enumerate_words,
    find_occurrences,
    indexed_students,
    inventory_report,
    ranked_scores,
)


def test_enumerate_list() -> None:
    """Test enumerate_list."""
    assert enumerate_list(["A", "B"]) == [
        (0, "A"),
        (1, "B"),
    ]


def test_enumerate_list_start() -> None:
    """Custom start."""
    assert enumerate_list_start(["A"], 5) == [
        (5, "A"),
    ]


def test_enumerate_string() -> None:
    """String enumeration."""
    assert enumerate_string("Hi") == [
        (0, "H"),
        (1, "i"),
    ]


def test_indexed_students() -> None:
    """Student numbering."""
    assert indexed_students(["Alice"]) == [
        "1. Alice",
    ]


def test_dictionary_keys() -> None:
    """Dictionary keys."""
    data = {"x": 1}

    assert enumerate_dictionary_keys(data) == [
        (0, "x"),
    ]


def test_dictionary_values() -> None:
    """Dictionary values."""
    data = {"x": 1}

    assert enumerate_dictionary_values(data) == [
        (0, 1),
    ]


def test_dictionary_items() -> None:
    """Dictionary items."""
    data = {"x": 1}

    assert enumerate_dictionary_items(data) == [
        (0, ("x", 1)),
    ]


def test_employee_report() -> None:
    """Employee report."""
    assert employee_report(["Alice"]) == [
        "Employee 1: Alice",
    ]


def test_ranked_scores() -> None:
    """Ranking."""
    assert ranked_scores([100]) == [
        (1, 100),
    ]


def test_csv_rows() -> None:
    """CSV rows."""
    assert csv_rows([["Alice"]]) == [
        "Row 1: ['Alice']",
    ]


def test_find_occurrences() -> None:
    """Occurrences."""
    assert find_occurrences(
        [1, 2, 2, 3],
        2,
    ) == [1, 2]


def test_enumerate_words() -> None:
    """Words."""
    assert enumerate_words(
        "Python Django"
    ) == [
        (1, "Python"),
        (2, "Django"),
    ]


def test_inventory_report() -> None:
    """Inventory report."""
    report = inventory_report(
        {"Mouse": 5},
    )

    assert report == [
        "1. Mouse (5)",
    ]