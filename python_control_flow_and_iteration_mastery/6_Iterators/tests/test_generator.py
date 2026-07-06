"""
Tests for generator_examples.py
"""

from Iterators import GeneratorExamples


def test_count_numbers():
    assert (
        list(
            GeneratorExamples.count_numbers(5)
        )
        == [1, 2, 3, 4, 5]
    )


def test_square_numbers():
    assert (
        list(
            GeneratorExamples.square_numbers(
                [1, 2, 3]
            )
        )
        == [1, 4, 9]
    )


def test_even_numbers():
    assert (
        list(
            GeneratorExamples.even_numbers(6)
        )
        == [0, 2, 4, 6]
    )