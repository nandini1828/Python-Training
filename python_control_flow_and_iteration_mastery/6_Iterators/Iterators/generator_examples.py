"""
generator_examples.py

Demonstrates Python Generators.
"""


class GeneratorExamples:
    """Utility class demonstrating generators."""

    @staticmethod
    def count_numbers(limit: int):
        """Generates numbers."""

        for number in range(1, limit + 1):
            yield number

    @staticmethod
    def square_numbers(numbers: list[int]):
        """Generates square values."""

        for number in numbers:
            yield number ** 2

    @staticmethod
    def even_numbers(limit: int):
        """Generates even numbers."""

        for number in range(limit + 1):

            if number % 2 == 0:
                yield number