"""Examples that explain reversed() and sorted()."""

from __future__ import annotations


def sort_names(names: list[str]) -> list[str]:
    """Sort names case-insensitively.

    Args:
        names: The names to sort.

    Returns:
        A sorted copy of the input names.
    """
    return sorted(names, key=str.lower)
