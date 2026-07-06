"""
Examples demonstrating safe set iteration.

Topics covered:

- Safe set iteration
- Filtering
- Safe removal
- Membership testing
- Snapshot iteration

Author: Python Training
"""

from __future__ import annotations


def filter_even_set(
    values: set[int],
) -> set[int]:
    """
    Return only even numbers.

    Args:
        values:
            Input set.

    Returns:
        Set containing only even values.
    """
    return {
        value
        for value in values
        if value % 2 == 0
    }


def remove_small_values(
    values: set[int],
    minimum: int,
) -> set[int]:
    """
    Remove values smaller than the minimum.

    Args:
        values:
            Input set.

        minimum:
            Minimum allowed value.

    Returns:
        Filtered set.
    """
    return {
        value
        for value in values
        if value >= minimum
    }


def uppercase_words(
    words: set[str],
) -> set[str]:
    """
    Convert every word to uppercase.

    Args:
        words:
            Input words.

    Returns:
        Uppercase words.
    """
    return {
        word.upper()
        for word in words
    }


def snapshot_iteration(
    values: set[int],
) -> list[int]:
    """
    Create a snapshot before iteration.

    Args:
        values:
            Input set.

    Returns:
        Snapshot list.
    """
    return list(values.copy())


def safe_remove(
    values: set[int],
    target: int,
) -> set[int]:
    """
    Remove a value safely.

    Args:
        values:
            Input set.

        target:
            Value to remove.

    Returns:
        Updated set.
    """
    result = values.copy()

    result.discard(target)

    return result


def common_values(
    first: set[int],
    second: set[int],
) -> set[int]:
    """
    Return common values.

    Args:
        first:
            First set.

        second:
            Second set.

    Returns:
        Intersection.
    """
    return {
        value
        for value in first
        if value in second
    }


def unique_values(
    first: set[int],
    second: set[int],
) -> set[int]:
    """
    Return values unique to the first set.

    Args:
        first:
            First set.

        second:
            Second set.

    Returns:
        Difference.
    """
    return {
        value
        for value in first
        if value not in second
    }


__all__ = [
    "filter_even_set",
    "remove_small_values",
    "uppercase_words",
    "snapshot_iteration",
    "safe_remove",
    "common_values",
    "unique_values",
]