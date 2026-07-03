"""
reversed_examples.py

Demonstrates Python reversed().
"""


class ReversedExamples:
    """Utility class demonstrating reversed()."""

    @staticmethod
    def reverse_list(numbers: list[int]) -> list[int]:
        """Returns reversed list."""

        return list(reversed(numbers))

    @staticmethod
    def reverse_string(text: str) -> str:
        """Returns reversed string."""

        return "".join(reversed(text))