"""
Unit tests for iterators.py

Run:

    pytest tests/test_iterators.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from comprehensions_generators.iterators import (
    AlphabetIterator,
    CountdownIterator,
    EmployeeIterator,
    NumberIterator,
    consume_iterator,
    iterator_max,
    iterator_sum,
    iterator_to_list,
    manual_iteration,
)


def test_number_iterator() -> None:
    """Test NumberIterator."""
    assert list(NumberIterator(5)) == [0, 1, 2, 3, 4]


def test_number_iterator_zero() -> None:
    """Zero limit."""
    assert list(NumberIterator(0)) == []


def test_number_iterator_negative() -> None:
    """Negative limit."""
    with pytest.raises(ValueError):
        NumberIterator(-1)


def test_countdown_iterator() -> None:
    """Countdown iterator."""
    assert list(CountdownIterator(5)) == [
        5,
        4,
        3,
        2,
        1,
        0,
    ]


def test_countdown_zero() -> None:
    """Countdown from zero."""
    assert list(CountdownIterator(0)) == [0]


def test_countdown_negative() -> None:
    """Negative countdown."""
    with pytest.raises(ValueError):
        CountdownIterator(-5)


def test_alphabet_iterator() -> None:
    """Alphabet iterator."""
    letters = list(AlphabetIterator())

    assert len(letters) == 26
    assert letters[0] == "A"
    assert letters[-1] == "Z"


def test_employee_iterator() -> None:
    """Employee iterator."""
    employees = [
        "Alice",
        "Bob",
        "Charlie",
    ]

    assert list(
        EmployeeIterator(employees)
    ) == employees


def test_manual_iteration() -> None:
    """Manual iter() and next()."""
    assert manual_iteration(
        [10, 20, 30]
    ) == [
        10,
        20,
        30,
    ]


def test_consume_iterator() -> None:
    """Consume iterator."""
    result = consume_iterator(
        NumberIterator(4)
    )

    assert result == [
        0,
        1,
        2,
        3,
    ]


def test_iterator_sum() -> None:
    """Iterator sum."""
    assert iterator_sum(
        NumberIterator(5)
    ) == 10


def test_iterator_max() -> None:
    """Maximum value."""
    assert iterator_max(
        NumberIterator(5)
    ) == 4


def test_iterator_max_empty() -> None:
    """Empty iterator."""
    with pytest.raises(ValueError):
        iterator_max(
            NumberIterator(0)
        )


def test_iterator_to_list() -> None:
    """Iterator conversion."""
    assert iterator_to_list(
        NumberIterator(3)
    ) == [
        0,
        1,
        2,
    ]