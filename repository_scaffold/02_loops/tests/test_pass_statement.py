"""
test_pass.py

Tests for pass statement utilities.
"""

from pass_statement.utils import (
    process_positive_numbers,
    find_first_positive,
    placeholder_function,
)


def test_process_positive_numbers():
    assert process_positive_numbers([1, -2, 3, -4]) == [1, 3]
    assert process_positive_numbers([-1, -2]) == []
    assert process_positive_numbers([5, 6]) == [5, 6]


def test_find_first_positive():
    assert find_first_positive([-5, -2, 3, 4]) == 3
    assert find_first_positive([-5, -2, 0]) is None
    assert find_first_positive([10]) == 10


def test_placeholder_function():
    assert placeholder_function() is None