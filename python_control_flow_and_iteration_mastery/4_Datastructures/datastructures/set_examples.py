"""
set_examples.py

Demonstrates Python sets.
"""


class SetExamples:
    """Utility class demonstrating sets."""

    @staticmethod
    def iterate_set(values: set[int]) -> list[int]:
        """Returns all elements."""

        result = []

        for value in values:
            result.append(value)

        return result

    @staticmethod
    def check_membership(
        values: set[int],
        target: int
    ) -> bool:
        """Checks membership."""

        return target in values

    @staticmethod
    def remove_duplicates(
        numbers: list[int]
    ) -> list[int]:
        """Removes duplicates."""

        return list(set(numbers))

    @staticmethod
    def add_element(
        values: set[int],
        element: int
    ) -> set[int]:
        """Adds an element."""

        values.add(element)

        return values