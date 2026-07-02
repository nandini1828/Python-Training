"""
while_loop.py

Demonstrates Python while loops.
"""


class WhileLoopExamples:
    """
    Utility class demonstrating
    Python while loops.
    """

    @staticmethod
    def count_numbers(limit: int) -> list[int]:
        """Counts from 1 to limit."""

        result = []

        count = 1

        while count <= limit:
            result.append(count)
            count += 1

        return result

    @staticmethod
    def countdown(start: int) -> list[int]:
        """Counts backwards."""

        result = []

        while start > 0:
            result.append(start)
            start -= 1

        return result

    @staticmethod
    def calculate_sum(limit: int) -> int:
        """Returns sum from 1 to limit."""

        total = 0
        number = 1

        while number <= limit:
            total += number
            number += 1

        return total