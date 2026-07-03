"""Examples showing how else blocks work with loops."""

from __future__ import annotations


def search_value(values: list[int], target: int) -> str:
    """Search for a target and explain whether the loop completed normally.

    Args:
        values: The list to search.
        target: The target value to locate.

    Returns:
        A message describing whether the value was found.
    """
    for value in values:
        if value == target:
            return f"Value {target} found."
    else:
        return f"Value {target} not found."
