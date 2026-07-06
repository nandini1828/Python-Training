"""
Examples demonstrating safe dictionary iteration.

Topics covered:

- Safe deletion
- Safe updates
- Key transformation
- Dictionary filtering

Author: Python Training
"""

from __future__ import annotations


def remove_empty_values(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Remove empty values.

    Args:
        data:
            Input dictionary.

    Returns:
        Filtered dictionary.
    """
    return {
        key: value
        for key, value in data.items()
        if value
    }


def remove_keys(
    data: dict[str, int],
    keys: list[str],
) -> dict[str, int]:
    """
    Remove selected keys.

    Args:
        data:
            Input dictionary.

        keys:
            Keys to remove.

    Returns:
        Updated dictionary.
    """
    return {
        key: value
        for key, value in data.items()
        if key not in keys
    }


def uppercase_keys(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Convert keys to uppercase.

    Args:
        data:
            Input dictionary.

    Returns:
        Updated dictionary.
    """
    return {
        key.upper(): value
        for key, value in data.items()
    }


def lowercase_values(
    data: dict[str, str],
) -> dict[str, str]:
    """
    Convert values to lowercase.

    Args:
        data:
            Input dictionary.

    Returns:
        Updated dictionary.
    """
    return {
        key: value.lower()
        for key, value in data.items()
    }


def filter_positive_values(
    data: dict[str, int],
) -> dict[str, int]:
    """
    Keep only positive values.

    Args:
        data:
            Input dictionary.

    Returns:
        Filtered dictionary.
    """
    return {
        key: value
        for key, value in data.items()
        if value > 0
    }


def snapshot_keys(
    data: dict[str, int],
) -> list[str]:
    """
    Return a snapshot of dictionary keys.

    Args:
        data:
            Input dictionary.

    Returns:
        List of keys.
    """
    return list(data.keys())


def snapshot_items(
    data: dict[str, int],
) -> list[tuple[str, int]]:
    """
    Return a snapshot of dictionary items.

    Args:
        data:
            Input dictionary.

    Returns:
        List of items.
    """
    return list(data.items())


__all__ = [
    "remove_empty_values",
    "remove_keys",
    "uppercase_keys",
    "lowercase_values",
    "filter_positive_values",
    "snapshot_keys",
    "snapshot_items",
]