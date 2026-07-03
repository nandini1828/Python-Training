"""
list_modification.py

Demonstrates safe list modification.
"""


class ListModificationExamples:
    """Utility class demonstrating list modification."""

    @staticmethod
    def remove_even_wrong(numbers: list[int]) -> list[int]:
        """
        Wrong approach.
        Elements may be skipped.
        """

        values = numbers.copy()

        for number in values:

            if number % 2 == 0:
                values.remove(number)

        return values

    @staticmethod
    def remove_even_correct(numbers: list[int]) -> list[int]:
        """
        Correct approach.
        """

        return [
            number
            for number in numbers
            if number % 2 != 0
        ]