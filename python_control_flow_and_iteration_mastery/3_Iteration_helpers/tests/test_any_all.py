"""
Tests for any_all_examples.py
"""

from iterations import AnyAllExamples


def test_any_positive():
    assert AnyAllExamples.any_positive(
        [-1, 2, -3]
    )


def test_all_positive():
    assert AnyAllExamples.all_positive(
        [1, 2, 3]
    )


def test_any_true():
    assert AnyAllExamples.any_true(
        [False, False, True]
    )


def test_all_true():
    assert AnyAllExamples.all_true(
        [True, True, True]
    )