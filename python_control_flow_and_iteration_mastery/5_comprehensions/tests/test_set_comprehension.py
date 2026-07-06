"""
Tests for set_comprehension.py
"""

from comprehensions import SetComprehensionExamples


def test_lowercase_words():
    assert (
        SetComprehensionExamples.lowercase_words(
            ["Python", "AI", "PYTHON"]
        )
        == {
            "python",
            "ai"
        }
    )


def test_unique_even_numbers():
    assert (
        SetComprehensionExamples.unique_even_numbers(
            [1, 2, 2, 4, 5, 6]
        )
        == {
            2,
            4,
            6
        }
    )


def test_square_set():
    assert (
        SetComprehensionExamples.square_set(
            [1, 2, 3]
        )
        == {
            1,
            4,
            9
        }
    )