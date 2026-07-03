"""Examples that demonstrate while loops."""

from __future__ import annotations


def countdown(start: int) -> list[int]:
    """Count down from a start value to zero.

    Args:
        start: The starting number.

    Returns:
        A list of values from start down to zero.
    """
    values: list[int] = []
    current = start
    while current >= 0:
        values.append(current)
        current -= 1
    return values
