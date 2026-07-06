"""
Tests for dictionary_comprehension.py
"""

from comprehensions import DictionaryComprehensionExamples


def test_square_dictionary():
    assert (
        DictionaryComprehensionExamples.square_dictionary(
            4
        )
        == {
            0: 0,
            1: 1,
            2: 4,
            3: 9
        }
    )


def test_word_lengths():
    assert (
        DictionaryComprehensionExamples.word_lengths(
            ["Python", "AI"]
        )
        == {
            "Python": 6,
            "AI": 2
        }
    )


def test_even_square_dictionary():
    assert (
        DictionaryComprehensionExamples.even_square_dictionary(
            6
        )
        == {
            0: 0,
            2: 4,
            4: 16
        }
    )