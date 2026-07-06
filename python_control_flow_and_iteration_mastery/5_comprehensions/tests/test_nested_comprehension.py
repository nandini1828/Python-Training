"""
Tests for nested_comprehension.py
"""

from comprehensions import NestedComprehensionExamples


def test_flatten_matrix():
    assert (
        NestedComprehensionExamples.flatten_matrix(
            [
                [1, 2],
                [3, 4]
            ]
        )
        == [1, 2, 3, 4]
    )


def test_create_matrix():
    assert (
        NestedComprehensionExamples.create_matrix(
            2,
            3
        )
        == [
            [0, 0, 0],
            [0, 0, 0]
        ]
    )


def test_multiplication_table():
    assert (
        NestedComprehensionExamples.multiplication_table(
            3
        )
        == [
            [1, 2, 3],
            [2, 4, 6],
            [3, 6, 9]
        ]
    )