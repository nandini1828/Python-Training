"""Examples showing dictionary comprehensions."""

from __future__ import annotations


def invert_mapping(mapping: dict[str, int]) -> dict[int, str]:
    """Swap keys and values in a dictionary.

    Args:
        mapping: A mapping from string to int.

    Returns:
        A new dictionary with swapped keys and values.
    """
    return {value: key for key, value in mapping.items()}
