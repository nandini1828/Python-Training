"""
enumerate_examples.py

Demonstrates Python enumerate().
"""


class EnumerateExamples:
    """Utility class demonstrating enumerate()."""

    @staticmethod
    def enumerate_list(names: list[str]) -> list[tuple[int, str]]:
        """Returns index and value."""

        return list(enumerate(names))

    @staticmethod
    def enumerate_with_start(
        names: list[str]
    ) -> list[tuple[int, str]]:
        """Starts index from 1."""

        return list(enumerate(names, start=1))