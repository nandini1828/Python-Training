"""
generator_expression.py

Demonstrates Generator Expressions.
"""


class GeneratorExpressionExamples:
    """Utility class demonstrating generator expressions."""

    @staticmethod
    def square_generator(numbers: list[int]):
        """Returns generator expression."""

        return (
            number ** 2
            for number in numbers
        )

    @staticmethod
    def filter_even(numbers: list[int]):
        """Returns even numbers generator."""

        return (
            number
            for number in numbers
            if number % 2 == 0
        )

    @staticmethod
    def string_lengths(words: list[str]):
        """Returns string lengths."""

        return (
            len(word)
            for word in words
        )