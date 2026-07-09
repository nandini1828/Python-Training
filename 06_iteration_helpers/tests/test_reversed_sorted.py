"""
Unit tests for iteration_helpers.reversed_sorted.

Run:

    pytest tests/test_reversed_sorted.py

Author: Python Training
"""

from __future__ import annotations

from iteration_helpers.reversed_sorted import (
    reverse_list,
    reverse_string,
    sort_by_length,
    sort_dictionary_keys,
    sort_dictionary_values,
    sort_numbers,
    sort_records_by_age,
    sort_records_by_name,
    sort_strings_case_insensitive,
)


def test_reverse_list() -> None:
    """Test reverse_list."""
    assert reverse_list([1, 2, 3]) == [3, 2, 1]


def test_reverse_list_empty() -> None:
    """Reverse empty list."""
    assert reverse_list([]) == []


def test_reverse_string() -> None:
    """Test reverse_string."""
    assert reverse_string("Python") == "nohtyP"


def test_reverse_string_empty() -> None:
    """Reverse empty string."""
    assert reverse_string("") == ""


def test_sort_numbers() -> None:
    """Ascending sort."""
    assert sort_numbers([5, 2, 8, 1]) == [1, 2, 5, 8]


def test_sort_numbers_descending() -> None:
    """Descending sort."""
    assert sort_numbers(
        [5, 2, 8, 1],
        descending=True,
    ) == [8, 5, 2, 1]


def test_sort_strings_case_insensitive() -> None:
    """Case-insensitive sorting."""
    values = [
        "banana",
        "Apple",
        "cherry",
    ]

    assert sort_strings_case_insensitive(values) == [
        "Apple",
        "banana",
        "cherry",
    ]


def test_sort_by_length() -> None:
    """Sort by string length."""
    values = [
        "Python",
        "C",
        "Java",
    ]

    assert sort_by_length(values) == [
        "C",
        "Java",
        "Python",
    ]


def test_sort_dictionary_keys() -> None:
    """Sort dictionary keys."""
    data = {
        "z": 1,
        "a": 2,
        "m": 3,
    }

    assert sort_dictionary_keys(data) == [
        "a",
        "m",
        "z",
    ]


def test_sort_dictionary_values() -> None:
    """Sort dictionary values."""
    data = {
        "x": 30,
        "y": 10,
        "z": 20,
    }

    assert sort_dictionary_values(data) == [
        10,
        20,
        30,
    ]


def test_sort_records_by_age() -> None:
    """Sort records using age."""
    employees = [
        {"name": "Bob", "age": 30},
        {"name": "Alice", "age": 25},
    ]

    result = sort_records_by_age(employees)

    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Bob"


def test_sort_records_by_name() -> None:
    """Sort records using name."""
    employees = [
        {"name": "Charlie", "age": 28},
        {"name": "alice", "age": 25},
        {"name": "Bob", "age": 30},
    ]

    result = sort_records_by_name(employees)

    assert result[0]["name"] == "alice"
    assert result[1]["name"] == "Bob"
    assert result[2]["name"] == "Charlie"