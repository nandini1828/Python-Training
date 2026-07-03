"""
Tests for sorted_examples.py
"""

from iterations import SortedExamples


def test_sort_numbers():
    assert SortedExamples.sort_numbers(
        [5, 2, 8]
    ) == [
        2, 5, 8
    ]


def test_sort_reverse():
    assert SortedExamples.sort_reverse(
        [5, 2, 8]
    ) == [
        8, 5, 2
    ]


def test_sort_by_length():
    assert SortedExamples.sort_by_length(
        ["Python", "AI", "ML"]
    ) == [
        "AI",
        "ML",
        "Python"
    ]