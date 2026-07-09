"""
Unit tests for loop_foundations.loops.

Run:

    pytest tests/test_loops.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from loop_foundations.loops import (
    countdown,
    count_characters,
    count_occurrences,
    factorial,
    fibonacci,
    filter_even_numbers,
    find_maximum,
    find_minimum,
    generate_range,
    iterate_dictionary,
    iterate_list,
    iterate_set,
    iterate_string,
    iterate_tuple,
    multiplication_table,
    nested_loop_grid,
    product_numbers,
    repeat_text,
    reverse_string,
    search_element,
    square_numbers,
    sum_numbers,
    while_sum,
)


# ============================================================================
# iterate_list()
# ============================================================================


def test_iterate_list() -> None:
    """Test list iteration."""
    data = [1, 2, 3]

    assert iterate_list(data) == [1, 2, 3]


# ============================================================================
# iterate_tuple()
# ============================================================================


def test_iterate_tuple() -> None:
    """Test tuple iteration."""
    data = ("Python", "Django")

    assert iterate_tuple(data) == ["Python", "Django"]


# ============================================================================
# iterate_set()
# ============================================================================


def test_iterate_set() -> None:
    """Test set iteration."""
    data = {"A", "B", "C"}

    assert set(iterate_set(data)) == data


# ============================================================================
# iterate_string()
# ============================================================================


def test_iterate_string() -> None:
    """Test string iteration."""
    assert iterate_string("ABC") == ["A", "B", "C"]


# ============================================================================
# iterate_dictionary()
# ============================================================================


def test_iterate_dictionary() -> None:
    """Test dictionary iteration."""
    data = {"name": "Alice"}

    assert iterate_dictionary(data) == [("name", "Alice")]


# ============================================================================
# generate_range()
# ============================================================================


def test_generate_range() -> None:
    """Test range generation."""
    assert generate_range(1, 6) == [1, 2, 3, 4, 5]


def test_generate_range_with_step() -> None:
    """Test range generation with step."""
    assert generate_range(0, 10, 2) == [0, 2, 4, 6, 8]


# ============================================================================
# sum_numbers()
# ============================================================================


def test_sum_numbers() -> None:
    """Test summation."""
    assert sum_numbers([1, 2, 3, 4]) == 10


def test_sum_numbers_empty() -> None:
    """Empty list sum."""
    assert sum_numbers([]) == 0


# ============================================================================
# product_numbers()
# ============================================================================


def test_product_numbers() -> None:
    """Test multiplication."""
    assert product_numbers([1, 2, 3, 4]) == 24


def test_product_numbers_empty() -> None:
    """Product of empty list."""
    assert product_numbers([]) == 1


# ============================================================================
# count_characters()
# ============================================================================


def test_count_characters() -> None:
    """Test character count."""
    assert count_characters("Python") == 6


# ============================================================================
# count_occurrences()
# ============================================================================


def test_count_occurrences() -> None:
    """Test occurrence counting."""
    values = [1, 2, 2, 3, 2]

    assert count_occurrences(values, 2) == 3


# ============================================================================
# square_numbers()
# ============================================================================


def test_square_numbers() -> None:
    """Test squaring."""
    assert square_numbers([1, 2, 3]) == [1, 4, 9]


# ============================================================================
# filter_even_numbers()
# ============================================================================


def test_filter_even_numbers() -> None:
    """Test even filtering."""
    assert filter_even_numbers([1, 2, 3, 4]) == [2, 4]


# ============================================================================
# reverse_string()
# ============================================================================


def test_reverse_string() -> None:
    """Test reversing."""
    assert reverse_string("Python") == "nohtyP"


# ============================================================================
# factorial()
# ============================================================================


def test_factorial() -> None:
    """Test factorial."""
    assert factorial(5) == 120


def test_factorial_zero() -> None:
    """Factorial of zero."""
    assert factorial(0) == 1


def test_factorial_negative() -> None:
    """Negative factorial."""
    with pytest.raises(ValueError):
        factorial(-1)


# ============================================================================
# multiplication_table()
# ============================================================================


def test_multiplication_table() -> None:
    """Test multiplication table."""
    table = multiplication_table(5)

    assert table[0] == "5 x 1 = 5"
    assert table[-1] == "5 x 10 = 50"
    assert len(table) == 10


# ============================================================================
# nested_loop_grid()
# ============================================================================


def test_nested_loop_grid() -> None:
    """Test grid generation."""
    grid = nested_loop_grid(2, 2)

    assert grid == [
        ["(0,0)", "(0,1)"],
        ["(1,0)", "(1,1)"],
    ]


# ============================================================================
# find_maximum()
# ============================================================================


def test_find_maximum() -> None:
    """Test maximum."""
    assert find_maximum([3, 8, 2]) == 8


def test_find_maximum_empty() -> None:
    """Maximum of empty list."""
    with pytest.raises(ValueError):
        find_maximum([])


# ============================================================================
# find_minimum()
# ============================================================================


def test_find_minimum() -> None:
    """Test minimum."""
    assert find_minimum([3, 8, 2]) == 2


def test_find_minimum_empty() -> None:
    """Minimum of empty list."""
    with pytest.raises(ValueError):
        find_minimum([])


# ============================================================================
# search_element()
# ============================================================================


def test_search_element_found() -> None:
    """Existing element."""
    assert search_element([1, 2, 3], 2) is True


def test_search_element_missing() -> None:
    """Missing element."""
    assert search_element([1, 2, 3], 10) is False


# ============================================================================
# countdown()
# ============================================================================


def test_countdown() -> None:
    """Test countdown."""
    assert countdown(3) == [3, 2, 1, 0]


# ============================================================================
# fibonacci()
# ============================================================================


def test_fibonacci() -> None:
    """Test fibonacci."""
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_zero() -> None:
    """Zero terms."""
    assert fibonacci(0) == []


def test_fibonacci_one() -> None:
    """One term."""
    assert fibonacci(1) == [0]


def test_fibonacci_negative() -> None:
    """Negative input."""
    with pytest.raises(ValueError):
        fibonacci(-1)


# ============================================================================
# while_sum()
# ============================================================================


def test_while_sum() -> None:
    """Test while loop summation."""
    assert while_sum(10) == 55


# ============================================================================
# repeat_text()
# ============================================================================


def test_repeat_text() -> None:
    """Test text repetition."""
    assert repeat_text("Python", 3) == [
        "Python",
        "Python",
        "Python",
    ]


def test_repeat_text_zero() -> None:
    """Repeat zero times."""
    assert repeat_text("Python", 0) == []