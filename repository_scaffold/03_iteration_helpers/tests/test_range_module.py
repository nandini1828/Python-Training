from range_module.utils import *

def test_generate_numbers():
    assert generate_numbers(5) == [0, 1, 2, 3, 4]


def test_custom_range():
    assert generate_custom_range(1, 6, 2) == [1, 3, 5]


def test_even_numbers():
    assert even_numbers(6) == [0, 2, 4]


def test_odd_numbers():
    assert odd_numbers(6) == [1, 3, 5]


def test_sum_of_range():
    assert sum_of_range(5) == 10