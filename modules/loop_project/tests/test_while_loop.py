from modules.loop_project.loops.while_loop import *


def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]


def test_factorial():
    assert factorial(5) == 120


def test_reverse():
    assert reverse_string("Indiana") == "anaidnI"


def test_sum():
    assert sum_numbers(10) == 55


def test_vowels():
    assert count_vowels("Indiana Jones") == 6


def test_power():
    assert power(2, 5) == 32


def test_smallest():
    assert find_smallest([20, 5, 15, 1, 8]) == 1