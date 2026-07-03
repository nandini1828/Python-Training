"""Examples showing list comprehensions."""

from __future__ import annotations


def square_numbers(values: list[int]) -> list[int]:
    """Square each number in a list.

    Args:
        values: The source values.

    Returns:
        A list of squared values.
    """
    return [value * value for value in values]
