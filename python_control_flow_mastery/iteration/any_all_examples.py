"""Examples that demonstrate any() and all()."""

from __future__ import annotations


def check_inventory(items: list[bool]) -> bool:
    """Check whether every inventory item is available.

    Args:
        items: A list of availability flags.

    Returns:
        True when all items are available, otherwise False.
    """
    return all(items)
