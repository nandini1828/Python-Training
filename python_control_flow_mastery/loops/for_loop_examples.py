"""Examples that demonstrate for loops."""

from __future__ import annotations


def find_target(values: list[int], target: int) -> int:
    """Search a list for a target value using a for loop.

    Args:
        values: The list to inspect.
        target: The value to find.

    Returns:
        The index of the target or -1 if missing.
    """
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def fibonacci_numbers(limit: int) -> list[int]:
    """Generate Fibonacci numbers up to a limit.

    Args:
        limit: The maximum number of values to produce.

    Returns:
        A list containing the first limit Fibonacci numbers.
    """
    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(limit):
        sequence.append(a)
        a, b = b, a + b
    return sequence
