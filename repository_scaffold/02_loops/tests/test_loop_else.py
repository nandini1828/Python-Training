"""
test_loop_else.py

Tests for loop-else utilities.
"""

from loop_else.utils import (
    find_prime,
    search_element_with_else,
    find_first_even_with_else,
    validate_all_positive,
    find_divisor,
    process_until_zero,
    find_with_while_else,
)


# ------------------ PRIME ------------------

def test_find_prime():
    assert find_prime(2) is True
    assert find_prime(3) is True
    assert find_prime(4) is False
    assert find_prime(17) is True
    assert find_prime(1) is False
    assert find_prime(0) is False
    assert find_prime(-5) is False


# ------------------ SEARCH ------------------

def test_search_element_with_else():
    data = [10, 20, 30]

    assert search_element_with_else(data, 10) == 0
    assert search_element_with_else(data, 30) == 2
    assert search_element_with_else(data, 99) == -1
    assert search_element_with_else([], 10) == -1


# ------------------ FIRST EVEN ------------------

def test_find_first_even_with_else():
    assert find_first_even_with_else([1, 3, 5, 6]) == 6
    assert find_first_even_with_else([2, 4, 6]) == 2
    assert find_first_even_with_else([1, 3, 5]) is None
    assert find_first_even_with_else([]) is None


# ------------------ VALIDATION ------------------

def test_validate_all_positive():
    assert validate_all_positive([1, 2, 3]) is True
    assert validate_all_positive([1, -2, 3]) is False
    assert validate_all_positive([0]) is False
    assert validate_all_positive([]) is True  # important edge case


# ------------------ DIVISOR ------------------

def test_find_divisor():
    assert find_divisor(10) == 2
    assert find_divisor(15) == 3
    assert find_divisor(13) is None  # prime
    assert find_divisor(1) is None
    assert find_divisor(0) is None


# ------------------ BREAK vs ELSE ------------------

def test_process_until_zero():
    assert process_until_zero([1, 2, 0, 5]) == [1, 2]
    assert process_until_zero([1, 2, 3]) == [1, 2, 3, "completed"]
    assert process_until_zero([]) == ["completed"]


# ------------------ WHILE ELSE ------------------

def test_find_with_while_else():
    data = [5, 10, 15]

    assert find_with_while_else(data, 5) == 0
    assert find_with_while_else(data, 15) == 2
    assert find_with_while_else(data, 99) == -1
    assert find_with_while_else([], 10) == -1