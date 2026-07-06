"""
Tests for list_comprehension.py
"""

from comprehensions import ListComprehensionExamples


def test_create_squares():
    assert (
        ListComprehensionExamples.create_squares(
            [1, 2, 3]
        )
        == [1, 4, 9]
    )


def test_filter_even_numbers():
    assert (
        ListComprehensionExamples.filter_even_numbers(
            [1, 2, 3, 4, 5, 6]
        )
        == [2, 4, 6]
    )


def test_convert_to_uppercase():
    assert (
        ListComprehensionExamples.convert_to_uppercase(
            ["python", "ai"]
        )
        == ["PYTHON", "AI"]
    )


def test_string_lengths():
    assert (
        ListComprehensionExamples.string_lengths(
            ["Python", "AI"]
        )
        == [6, 2]
    )