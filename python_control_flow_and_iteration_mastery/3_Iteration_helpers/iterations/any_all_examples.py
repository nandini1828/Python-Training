"""
any_all_examples.py

Demonstrates Python any() and all().
"""


class AnyAllExamples:
    """Utility class demonstrating any() and all()."""

    @staticmethod
    def any_positive(numbers: list[int]) -> bool:
        """Returns True if any number is positive."""

        return any(number > 0 for number in numbers)

    @staticmethod
    def all_positive(numbers: list[int]) -> bool:
        """Returns True if all numbers are positive."""

        return all(number > 0 for number in numbers)

    @staticmethod
    def any_true(values: list[bool]) -> bool:
        """Checks if any value is True."""

        return any(values)

    @staticmethod
    def all_true(values: list[bool]) -> bool:
        """Checks if all values are True."""

        return all(values)