"""
Unit tests for set_comprehensions.py

Run:

    pytest tests/test_set_comprehensions.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from comprehensions_generators.set_comprehensions import (
    positive_numbers,
    unique_characters,
    unique_even_numbers,
    unique_first_letters,
    unique_lowercase_words,
    unique_remainders,
    unique_word_lengths,
    vowels,
)


def test_unique_lowercase_words() -> None:
    """Test lowercase conversion."""
    result = unique_lowercase_words(
        [
            "Python",
            "python",
            "DJANGO",
        ]
    )

    assert result == {
        "python",
        "django",
    }


def test_unique_first_letters() -> None:
    """Test first letters."""
    result = unique_first_letters(
        [
            "Python",
            "Programming",
            "Django",
        ]
    )

    assert result == {
        "p",
        "d",
    }


def test_unique_word_lengths() -> None:
    """Test unique lengths."""
    result = unique_word_lengths(
        [
            "Python",
            "Java",
            "C",
        ]
    )

    assert result == {
        6,
        4,
        1,
    }


def test_unique_even_numbers() -> None:
    """Test even numbers."""
    result = unique_even_numbers(
        [
            2,
            4,
            2,
            6,
            8,
            4,
        ]
    )

    assert result == {
        2,
        4,
        6,
        8,
    }


def test_unique_remainders() -> None:
    """Test remainders."""
    result = unique_remainders(
        [
            10,
            15,
            20,
            25,
        ],
        3,
    )

    assert result == {
        1,
        2,
    }


def test_unique_remainders_zero_division() -> None:
    """Divisor cannot be zero."""
    with pytest.raises(ValueError):
        unique_remainders(
            [1, 2, 3],
            0,
        )


def test_positive_numbers() -> None:
    """Test positives."""
    result = positive_numbers(
        [
            -5,
            0,
            10,
            15,
            -2,
        ]
    )

    assert result == {
        10,
        15,
    }


def test_unique_characters() -> None:
    """Test unique characters."""
    result = unique_characters(
        "Python"
    )

    assert result == {
        "P",
        "y",
        "t",
        "h",
        "o",
        "n",
    }


def test_vowels() -> None:
    """Test vowels."""
    result = vowels(
        "Artificial Intelligence"
    )

    assert result == {
        "a",
        "e",
        "i",
    }


def test_empty_inputs() -> None:
    """Test empty collections."""
    assert unique_lowercase_words([]) == set()
    assert unique_characters("") == set()