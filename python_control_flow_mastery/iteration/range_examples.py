"""Examples that demonstrate the built-in range function."""

from __future__ import annotations


def describe_range(stop: int) -> str:
    """Create a simple description of range(stop).

    Args:
        stop: The stop value for range.

    Returns:
        A string representation of the range.
    """
    return f"range(0, {stop})"


def reverse_range(stop: int) -> list[int]:
    """Return a reversed sequence created from range."""
    return list(range(stop - 1, -1, -1))
