"""Examples that show break, continue, and pass statements."""

from __future__ import annotations


def process_numbers(values: list[int]) -> list[int]:
    """Filter out even numbers while skipping others.

    Args:
        values: An input list of integers.

    Returns:
        A list containing only odd numbers.
    """
    result: list[int] = []
    for value in values:
        if value % 2 == 0:
            continue
        result.append(value)
    return result
