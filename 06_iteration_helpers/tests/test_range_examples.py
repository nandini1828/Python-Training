"""
Unit tests for iteration_helpers.range_examples.

Run:

    pytest tests/test_range_examples.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from iteration_helpers.range_examples import (
    batch_numbers,
    countdown,
    divisible_by,
    employee_ids,
    even_numbers,
    generate_numbers,
    generate_range,
    generate_range_step,
    multiplication_table,
    odd_numbers,
    reverse_range,
    squares_using_range,
    sum_using_range,
)


def test_generate_numbers() -> None:
    """Test generate_numbers."""
    assert generate_numbers(5) == [0, 1, 2, 3, 4]


def test_generate_numbers_negative() -> None:
    """Negative stop raises ValueError."""
    with pytest.raises(ValueError):
        generate_numbers(-1)


def test_generate_range() -> None:
    """Test generate_range."""
    assert generate_range(2, 6) == [2, 3, 4, 5]


def test_generate_range_step() -> None:
    """Test generate_range_step."""
    assert generate_range_step(0, 10, 2) == [0, 2, 4, 6, 8]


def test_generate_range_step_zero() -> None:
    """Zero step raises ValueError."""
    with pytest.raises(ValueError):
        generate_range_step(1, 10, 0)


def test_reverse_range() -> None:
    """Test reverse_range."""
    assert reverse_range(5) == [5, 4, 3, 2, 1, 0]


def test_even_numbers() -> None:
    """Test even numbers."""
    assert even_numbers(10) == [0, 2, 4, 6, 8]


def test_odd_numbers() -> None:
    """Test odd numbers."""
    assert odd_numbers(10) == [1, 3, 5, 7, 9]


def test_multiplication_table() -> None:
    """Test multiplication table."""
    table = multiplication_table(5)

    assert len(table) == 10
    assert table[0] == "5 x 1 = 5"
    assert table[-1] == "5 x 10 = 50"


def test_sum_using_range() -> None:
    """Test summation."""
    assert sum_using_range(10) == 55


def test_squares_using_range() -> None:
    """Test square generation."""
    assert squares_using_range(5) == [0, 1, 4, 9, 16]


def test_countdown() -> None:
    """Test countdown."""
    assert countdown(3) == [3, 2, 1, 0]


def test_countdown_negative() -> None:
    """Negative countdown."""
    with pytest.raises(ValueError):
        countdown(-2)


def test_divisible_by() -> None:
    """Test divisibility."""
    assert divisible_by(12, 3) == [0, 3, 6, 9]


def test_divisible_by_zero() -> None:
    """Division by zero."""
    with pytest.raises(ValueError):
        divisible_by(10, 0)


def test_employee_ids() -> None:
    """Test employee IDs."""
    assert employee_ids(1001, 3) == [
        1001,
        1002,
        1003,
    ]


def test_batch_numbers() -> None:
    """Test batch generation."""
    assert batch_numbers(20, 5) == [0, 5, 10, 15]


def test_batch_numbers_invalid() -> None:
    """Invalid batch size."""
    with pytest.raises(ValueError):
        batch_numbers(20, 0)