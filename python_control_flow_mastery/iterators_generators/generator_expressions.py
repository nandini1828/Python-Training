"""Examples that demonstrate generator expressions."""

from __future__ import annotations


def even_numbers(limit: int) -> object:
    """Yield even numbers from zero up to a limit.

    Args:
        limit: The exclusive upper bound.

    Yields:
        Even integers.
    """
    return (value for value in range(limit) if value % 2 == 0)
