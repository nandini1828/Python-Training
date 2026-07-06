"""
Unit tests for list_comprehensions.py

Run:

    pytest tests/test_list_comprehensions.py

Author: Python Training
"""

from __future__ import annotations

from comprehensions_generators.list_comprehensions import (
    even_numbers,
    filter_long_words,
    flatten_matrix,
    lowercase_words,
    multiplication_table,
    odd_numbers,
    remove_none,
    square_numbers,
    uppercase_words,
    word_lengths,
)


def test_square_numbers() -> None:
    """Test square_numbers."""
    assert square_numbers([1, 2, 3]) == [1, 4, 9]


def test_even_numbers() -> None:
    """Test even_numbers."""
    assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_odd_numbers() -> None:
    """Test odd_numbers."""
    assert odd_numbers([1, 2, 3, 4]) == [1, 3]


def test_uppercase_words() -> None:
    """Test uppercase conversion."""
    assert uppercase_words(
        ["python", "django"]
    ) == [
        "PYTHON",
        "DJANGO",
    ]


def test_lowercase_words() -> None:
    """Test lowercase conversion."""
    assert lowercase_words(
        ["Python", "DJANGO"]
    ) == [
        "python",
        "django",
    ]


def test_filter_long_words() -> None:
    """Test filtering."""
    words = [
        "AI",
        "Python",
        "Development",
    ]

    assert filter_long_words(
        words,
        minimum_length=6,
    ) == [
        "Python",
        "Development",
    ]


def test_word_lengths() -> None:
    """Test word lengths."""
    assert word_lengths(
        ["Python", "AI"]
    ) == [
        6,
        2,
    ]


def test_remove_none() -> None:
    """Test None removal."""
    assert remove_none(
        [
            1,
            None,
            2,
            None,
            3,
        ]
    ) == [
        1,
        2,
        3,
    ]


def test_flatten_matrix() -> None:
    """Test matrix flattening."""
    matrix = [
        [1, 2],
        [3, 4],
    ]

    assert flatten_matrix(matrix) == [
        1,
        2,
        3,
        4,
    ]


def test_multiplication_table() -> None:
    """Test multiplication table."""
    table = multiplication_table(5)

    assert table[0] == 5
    assert table[-1] == 50
    assert len(table) == 10


def test_empty_inputs() -> None:
    """Test empty collections."""
    assert square_numbers([]) == []
    assert even_numbers([]) == []
    assert flatten_matrix([]) == []