"""
sorted_examples.py

Demonstrates Python sorted().
"""


class SortedExamples:
    """Utility class demonstrating sorted()."""

    @staticmethod
    def sort_numbers(numbers: list[int]) -> list[int]:
        """Sorts numbers."""

        return sorted(numbers)

    @staticmethod
    def sort_reverse(numbers: list[int]) -> list[int]:
        """Sorts in descending order."""

        return sorted(numbers, reverse=True)

    @staticmethod
    def sort_by_length(words: list[str]) -> list[str]:
        """Sorts strings by length."""

        return sorted(words, key=len)