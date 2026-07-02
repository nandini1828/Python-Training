"""
Tests for for_loop.py
"""

from loops import ForLoopExamples


def test_iterate_list():
    assert ForLoopExamples.iterate_list([1, 2, 3]) == [1, 2, 3]


def test_iterate_string():
    assert ForLoopExamples.iterate_string("ABC") == ["A", "B", "C"]


def test_iterate_range():
    assert ForLoopExamples.iterate_range(1, 5) == [1, 2, 3, 4]


def test_calculate_sum():
    assert ForLoopExamples.calculate_sum([10, 20, 30]) == 60