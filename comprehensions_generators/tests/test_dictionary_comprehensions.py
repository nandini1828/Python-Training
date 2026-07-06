"""
Unit tests for dictionary_comprehensions.py

Run:

    pytest tests/test_dictionary_comprehensions.py

Author: Python Training
"""

from __future__ import annotations

from comprehensions_generators.dictionary_comprehensions import (
    employee_salary_map,
    even_square_map,
    filter_positive,
    grade_book,
    invert_dictionary,
    lowercase_values,
    number_squares,
    uppercase_keys,
    word_lengths,
)


def test_number_squares() -> None:
    """Test square mapping."""
    assert number_squares(4) == {
        0: 0,
        1: 1,
        2: 4,
        3: 9,
    }


def test_word_lengths() -> None:
    """Test word lengths."""
    assert word_lengths(
        [
            "Python",
            "AI",
        ]
    ) == {
        "Python": 6,
        "AI": 2,
    }


def test_employee_salary_map() -> None:
    """Test salary mapping."""
    result = employee_salary_map(
        [
            "Alice",
            "Bob",
        ],
        [
            100,
            200,
        ],
    )

    assert result == {
        "Alice": 100,
        "Bob": 200,
    }


def test_even_square_map() -> None:
    """Test even square mapping."""
    assert even_square_map(6) == {
        0: 0,
        2: 4,
        4: 16,
    }


def test_uppercase_keys() -> None:
    """Uppercase keys."""
    result = uppercase_keys(
        {
            "name": "Alice",
        }
    )

    assert result == {
        "NAME": "Alice",
    }


def test_lowercase_values() -> None:
    """Lowercase values."""
    result = lowercase_values(
        {
            "Language": "PYTHON",
        }
    )

    assert result == {
        "Language": "python",
    }


def test_invert_dictionary() -> None:
    """Invert mapping."""
    result = invert_dictionary(
        {
            "A": "Apple",
        }
    )

    assert result == {
        "Apple": "A",
    }


def test_filter_positive() -> None:
    """Filter positives."""
    result = filter_positive(
        {
            "A": 5,
            "B": -1,
            "C": 10,
        }
    )

    assert result == {
        "A": 5,
        "C": 10,
    }


def test_grade_book() -> None:
    """Grade mapping."""
    result = grade_book(
        {
            "Alice": 90,
            "Bob": 20,
        }
    )

    assert result == {
        "Alice": "Pass",
        "Bob": "Fail",
    }


def test_empty_dictionary() -> None:
    """Empty dictionary."""
    assert word_lengths([]) == {}
    assert filter_positive({}) == {}