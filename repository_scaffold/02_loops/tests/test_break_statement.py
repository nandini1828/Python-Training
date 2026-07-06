"""
test_break_statements.py

Pytest test cases for break_statement utilities.
Run:
    pytest
"""

import pytest

from break_statement import (
    stop_at,
    find_first_even,
    search_item,
    stop_on_negative,
    first_prime,
    login_success,
    process_until_cancel,
)


def test_stop_at():
    assert stop_at(10, 5) == [1, 2, 3, 4]


def test_find_first_even():
    assert find_first_even([1, 3, 5, 8, 9]) == 8
    assert find_first_even([1, 3, 5]) is None


def test_search_item():
    assert search_item([10, 20, 30], 20) is True
    assert search_item([10, 20, 30], 99) is False


def test_stop_on_negative():
    assert stop_on_negative([5, 8, 12, -1, 20]) == [5, 8, 12]
    assert stop_on_negative([1, 2, 3]) == [1, 2, 3]


def test_first_prime():
    assert first_prime([8, 10, 15, 17, 20]) == 17
    assert first_prime([1, 4, 6, 8]) is None


def test_login_success():
    assert login_success(3, 2) is True
    assert login_success(3, 5) is False


def test_process_until_cancel():
    assert process_until_cancel(["A", "B", "Cancelled", "C"]) == ["A", "B"]
    assert process_until_cancel(["A", "B", "C"]) == ["A", "B", "C"]