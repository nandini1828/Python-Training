"""
list_examples.py

Demonstrates list iteration.
"""


class ListExamples:
    """Utility class demonstrating list operations."""

    @staticmethod
    def iterate_list(numbers: list[int]) -> list[int]:
        """Iterates through a list."""

        result = []

        for number in numbers:
            result.append(number)

        return result

    @staticmethod
    def access_index(numbers: list[int], index: int) -> int:
        """Returns element at given index."""

        return numbers[index]

    @staticmethod
    def slice_list(numbers: list[int]) -> list[int]:
        """Returns first three elements."""

        return numbers[:3]

    @staticmethod
    def first_element(numbers: list[int]) -> int:
        """Returns first element."""

        return numbers[0]

    @staticmethod
    def last_element(numbers: list[int]) -> int:
        """Returns last element."""

        return numbers[-1]