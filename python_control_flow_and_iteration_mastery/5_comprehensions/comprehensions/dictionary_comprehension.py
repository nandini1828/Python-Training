"""
dictionary_comprehension.py

Demonstrates Python Dictionary Comprehensions.
"""


class DictionaryComprehensionExamples:
    """Utility class demonstrating dictionary comprehensions."""

    @staticmethod
    def square_dictionary(limit: int) -> dict[int, int]:
        """Creates square dictionary."""

        return {
            number: number ** 2
            for number in range(limit)
        }

    @staticmethod
    def word_lengths(words: list[str]) -> dict[str, int]:
        """Returns word lengths."""

        return {
            word: len(word)
            for word in words
        }

    @staticmethod
    def even_square_dictionary(limit: int) -> dict[int, int]:
        """Squares even numbers."""

        return {
            number: number ** 2
            for number in range(limit)
            if number % 2 == 0
        }