"""Examples that demonstrate zip()."""

from __future__ import annotations


def zip_lists(left: list[int], right: list[str]) -> list[tuple[int, str]]:
    """Zip two lists into paired tuples.

    Args:
        left: The first list.
        right: The second list.

    Returns:
        A list of pairs.
    """
    return list(zip(left, right))
