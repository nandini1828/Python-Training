"""
Tests for while_loop.py
"""

from loops import WhileLoopExamples


def test_count_numbers():
    assert WhileLoopExamples.count_numbers(5) == [1, 2, 3, 4, 5]


def test_countdown():
    assert WhileLoopExamples.countdown(3) == [3, 2, 1]


def test_calculate_sum():
    assert WhileLoopExamples.calculate_sum(5) == 15