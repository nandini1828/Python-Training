"""
Tests for generator_expression.py
"""

from Iterators import GeneratorExpressionExamples


def test_square_generator():
    assert (
        list(
            GeneratorExpressionExamples.square_generator(
                [1, 2, 3]
            )
        )
        == [1, 4, 9]
    )


def test_filter_even():
    assert (
        list(
            GeneratorExpressionExamples.filter_even(
                [1, 2, 3, 4, 5]
            )
        )
        == [2, 4]
    )


def test_string_lengths():
    assert (
        list(
            GeneratorExpressionExamples.string_lengths(
                ["Python", "AI"]
            )
        )
        == [6, 2]
    )