"""Examples that explain why modifying a list during iteration is risky."""

from __future__ import annotations


def remove_even_numbers(values: list[int]) -> list[int]:
    """Remove even numbers using a copy of the list.

    Args:
        values: The input values.

    Returns:
        A list containing only odd values.
    """
    return [value for value in values if value % 2 != 0]
