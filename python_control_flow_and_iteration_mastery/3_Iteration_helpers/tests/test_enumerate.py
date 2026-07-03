"""
Tests for enumerate_examples.py
"""

from iterations import EnumerateExamples


def test_enumerate_list():
    assert EnumerateExamples.enumerate_list(
        ["A", "B"]
    ) == [
        (0, "A"),
        (1, "B")
    ]


def test_enumerate_with_start():
    assert EnumerateExamples.enumerate_with_start(
        ["A", "B"]
    ) == [
        (1, "A"),
        (2, "B")
    ]