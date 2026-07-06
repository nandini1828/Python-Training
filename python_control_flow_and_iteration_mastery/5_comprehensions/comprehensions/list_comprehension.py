"""
list_comprehension.py

Demonstrates Python List Comprehensions.
"""


class ListComprehensionExamples:
    """Utility class demonstrating list comprehensions."""

    @staticmethod
    def create_squares(numbers: list[int]) -> list[int]:
        """Returns squares of numbers."""

        return [number ** 2 for number in numbers]

    @staticmethod
    def filter_even_numbers(numbers: list[int]) -> list[int]:
        """Returns even numbers."""

        return [
            number
            for number in numbers
            if number % 2 == 0
        ]

    @staticmethod
    def convert_to_uppercase(words: list[str]) -> list[str]:
        """Converts strings to uppercase."""

        return [
            word.upper()
            for word in words
        ]

    @staticmethod
    def string_lengths(words: list[str]) -> list[int]:
        """Returns length of each string."""

        return [
            len(word)
            for word in words
        ]