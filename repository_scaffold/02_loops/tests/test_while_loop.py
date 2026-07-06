"""
Unit tests for while_loop utilities.
"""

import pytest

from while_loop.utils import (
    count_digits,
    count_down,
    count_up,
    countdown,
    factorial,
    find_first_even,
    is_palindrome,
    multiplication_table,
    reverse_string,
    sum_numbers,
)


def test_count_up():
    assert count_up(5) == [1, 2, 3, 4, 5]
    assert count_up(0) == []


def test_count_down():
    assert count_down(5) == [5, 4, 3, 2, 1]
    assert count_down(0) == []


def test_sum_numbers():
    assert sum_numbers([10, 20, 30]) == 60
    assert sum_numbers([]) == 0


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_multiplication_table():
    table = multiplication_table(3)

    assert len(table) == 10
    assert table[0] == "3 x 1 = 3"
    assert table[-1] == "3 x 10 = 30"


def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(0) == []


def test_find_first_even():
    assert find_first_even([1, 3, 5, 8, 9]) == 8
    assert find_first_even([1, 3, 5]) is None


def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""


def test_count_digits():
    assert count_digits(12345) == 5
    assert count_digits(0) == 1
    assert count_digits(-987) == 3


def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True