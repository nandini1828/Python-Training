"""Examples for iterating over dictionaries."""

from __future__ import annotations


def summarize_inventory(items: dict[str, int]) -> str:
    """Create a readable summary of a dictionary.

    Args:
        items: A dictionary of product names to quantities.

    Returns:
        A human-readable summary string.
    """
    summary: list[str] = []
    for name, quantity in items.items():
        summary.append(f"{name}: {quantity}")
    return ", ".join(summary)
