"""Examples that demonstrate enumerate()."""

from __future__ import annotations


def enumerate_with_index(values: list[str], start: int = 0) -> list[tuple[int, str]]:
    """Pair each value with an index.

    Args:
        values: The values to enumerate.
        start: The starting index.

    Returns:
        A list of index/value pairs.
    """
    return list(enumerate(values, start=start))
