"""Examples showing how to iterate over lists."""

from __future__ import annotations


def flatten_nested_lists(values: list[list[int]]) -> list[int]:
    """Flatten a list of lists into one list.

    Args:
        values: A nested list structure.

    Returns:
        A flattened list.
    """
    flattened: list[int] = []
    for inner in values:
        flattened.extend(inner)
    return flattened
