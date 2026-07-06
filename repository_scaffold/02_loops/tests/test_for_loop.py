"""
Unit tests for for_loop utilities.
"""

import pytest

from for_loop.utils import (
    count_vowels,
    create_student_dictionary,
    filter_even_numbers,
    find_max,
    find_min,
    multiplication_table,
    reverse_string,
    square_numbers,
    sum_numbers,
)


def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4]) == 10
    assert sum_numbers([]) == 0


def test_find_max():
    assert find_max([2, 5, 9, 1]) == 9


def test_find_max_empty():
    with pytest.raises(ValueError):
        find_max([])


def test_find_min():
    assert find_min([2, 5, 9, 1]) == 1


def test_find_min_empty():
    with pytest.raises(ValueError):
        find_min([])


def test_count_vowels():
    assert count_vowels("Python") == 1
    assert count_vowels("Education") == 5


def test_multiplication_table():
    table = multiplication_table(5)

    assert len(table) == 10
    assert table[0] == "5 x 1 = 5"
    assert table[-1] == "5 x 10 = 50"


def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""


def test_square_numbers():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_create_student_dictionary():
    names = ["Ganesh", "Rahul"]
    marks = [95, 90]

    expected = {
        "Ganesh": 95,
        "Rahul": 90,
    }

    assert create_student_dictionary(names, marks) == expected