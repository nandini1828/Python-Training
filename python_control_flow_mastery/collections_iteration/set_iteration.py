"""Examples for iterating over sets."""

from __future__ import annotations


def unique_names(names: list[str]) -> list[str]:
    """Return unique names while preserving insertion order.

    Args:
        names: A list that may contain duplicates.

    Returns:
        A list of unique names.
    """
    return list(dict.fromkeys(names))
