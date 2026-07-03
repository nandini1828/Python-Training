"""
range_examples.py

Demonstrates Python range().
"""


class RangeExamples:
    """Utility class demonstrating range()."""

    @staticmethod
    def basic_range() -> list[int]:
        """Returns numbers from 0 to 4."""

        return list(range(5))

    @staticmethod
    def start_stop() -> list[int]:
        """Returns numbers from 2 to 5."""

        return list(range(2, 6))

    @staticmethod
    def start_stop_step() -> list[int]:
        """Returns numbers with step."""

        return list(range(2, 11, 2))

    @staticmethod
    def reverse_range() -> list[int]:
        """Returns numbers in reverse."""

        return list(range(5, 0, -1))