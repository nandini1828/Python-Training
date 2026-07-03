"""
Tests for reversed_examples.py
"""

from iterations import ReversedExamples


def test_reverse_list():
    assert ReversedExamples.reverse_list(
        [1, 2, 3]
    ) == [
        3, 2, 1
    ]


def test_reverse_string():
    assert ReversedExamples.reverse_string(
        "Python"
    ) == "nohtyP"