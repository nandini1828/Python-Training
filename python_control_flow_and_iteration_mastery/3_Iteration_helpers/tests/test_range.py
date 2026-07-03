"""
Tests for range_examples.py
"""

from iterations import RangeExamples


def test_basic_range():
    assert RangeExamples.basic_range() == [0, 1, 2, 3, 4]


def test_start_stop():
    assert RangeExamples.start_stop() == [2, 3, 4, 5]


def test_start_stop_step():
    assert RangeExamples.start_stop_step() == [2, 4, 6, 8, 10]


def test_reverse_range():
    assert RangeExamples.reverse_range() == [5, 4, 3, 2, 1]