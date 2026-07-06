"""
Unit tests for range_helper utilities.
"""

import pytest

from range_module.utils import (
    cube_numbers,
    even_numbers,
    generate_range,
    generate_range_with_start,
    generate_range_with_step,
    multiplication_table,
    odd_numbers,
    reverse_range,
    squares,
    sum_first_n,
)


def test_generate_range():
    assert generate_range(5) == [0, 1, 2, 3, 4]
    assert generate_range(0) == []


def test_generate_range_with_start():
    assert generate_range_with_start(3, 7) == [3, 4, 5, 6]


def test_generate_range_with_step():
    assert generate_range_with_step(2, 11, 2) == [2, 4, 6, 8, 10]


def test_generate_range_with_step_zero():
    with pytest.raises(ValueError):
        generate_range_with_step(1, 10, 0)


def test_reverse_range():
    assert reverse_range(5, 0) == [5, 4, 3, 2, 1]


def test_reverse_range_invalid_step():
    with pytest.raises(ValueError):
        reverse_range(5, 0, 1)


def test_even_numbers():
    assert even_numbers(10) == [2, 4, 6, 8, 10]
    assert even_numbers(1) == []


def test_odd_numbers():
    assert odd_numbers(10) == [1, 3, 5, 7, 9]


def test_multiplication_table():
    table = multiplication_table(4)

    assert len(table) == 10
    assert table[0] == "4 x 1 = 4"
    assert table[-1] == "4 x 10 = 40"


def test_sum_first_n():
    assert sum_first_n(5) == 15
    assert sum_first_n(0) == 0


def test_squares():
    assert squares(5) == [1, 4, 9, 16, 25]


def test_cube_numbers():
    assert cube_numbers(4) == [1, 8, 27, 64]