"""
for_loop.py

Demonstrates Python for loops.
"""


class ForLoopExamples:
    """
    Utility class demonstrating
    Python for loops.
    """

    @staticmethod
    def iterate_list(numbers: list[int]) -> list[int]:
        """Returns all elements from a list."""

        result = []

        for number in numbers:
            result.append(number)

        return result

    @staticmethod
    def iterate_string(text: str) -> list[str]:
        """Returns characters from a string."""

        characters = []

        for character in text:
            characters.append(character)

        return characters

    @staticmethod
    def iterate_range(start: int, stop: int) -> list[int]:
        """Returns numbers using range()."""

        numbers = []

        for number in range(start, stop):
            numbers.append(number)

        return numbers

    @staticmethod
    def calculate_sum(numbers: list[int]) -> int:
        """Returns sum of numbers."""

        total = 0

        for number in numbers:
            total += number

        return total