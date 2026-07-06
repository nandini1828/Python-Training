"""
set_comprehension.py

Demonstrates Python Set Comprehensions.
"""


class SetComprehensionExamples:
    """Utility class demonstrating set comprehensions."""

    @staticmethod
    def lowercase_words(words: list[str]) -> set[str]:
        """Returns lowercase words."""

        return {
            word.lower()
            for word in words
        }

    @staticmethod
    def unique_even_numbers(numbers: list[int]) -> set[int]:
        """Returns unique even numbers."""

        return {
            number
            for number in numbers
            if number % 2 == 0
        }

    @staticmethod
    def square_set(numbers: list[int]) -> set[int]:
        """Returns square values."""

        return {
            number ** 2
            for number in numbers
        }