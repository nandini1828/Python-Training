"""
Examples demonstrating defensive iteration.

Topics covered:

- Snapshot iteration
- Batch processing
- Validation
- Immutable processing
- Defensive programming

Author: Python Training
"""

from __future__ import annotations


def safe_snapshot_iteration(
    values: list[int],
) -> list[int]:
    """
    Iterate over a snapshot.

    Args:
        values:
            Input list.

    Returns:
        Snapshot.
    """
    return [
        value
        for value in values.copy()
    ]


def safe_batch_processing(
    values: list[int],
    batch_size: int,
) -> list[list[int]]:
    """
    Split values into batches.

    Args:
        values:
            Input values.

        batch_size:
            Batch size.

    Returns:
        List of batches.

    Raises:
        ValueError:
            If batch_size is invalid.
    """
    if batch_size <= 0:
        raise ValueError(
            "batch_size must be positive."
        )

    return [
        values[index:index + batch_size]
        for index in range(
            0,
            len(values),
            batch_size,
        )
    ]


def validate_numbers(
    values: list[int],
) -> bool:
    """
    Validate numeric values.

    Args:
        values:
            Input values.

    Returns:
        True if every value is an integer.
    """
    return all(
        isinstance(
            value,
            int,
        )
        for value in values
    )


def immutable_filter(
    values: list[int],
) -> tuple[int, ...]:
    """
    Return immutable filtered data.

    Args:
        values:
            Input values.

    Returns:
        Tuple of positive values.
    """
    return tuple(
        value
        for value in values
        if value > 0
    )


def process_if_valid(
    values: list[int],
) -> list[int]:
    """
    Process validated values.

    Args:
        values:
            Input values.

    Returns:
        Doubled values.

    Raises:
        TypeError:
            If validation fails.
    """
    if not validate_numbers(values):
        raise TypeError(
            "All values must be integers."
        )

    return [
        value * 2
        for value in values
    ]


def safe_dictionary_iteration(
    data: dict[str, int],
) -> list[tuple[str, int]]:
    """
    Iterate safely over dictionary items.

    Args:
        data:
            Input dictionary.

    Returns:
        Snapshot of items.
    """
    return list(data.items())


def safe_set_iteration(
    values: set[int],
) -> list[int]:
    """
    Iterate safely over a set.

    Args:
        values:
            Input set.

    Returns:
        Snapshot of set values.
    """
    return list(values.copy())


__all__ = [
    "safe_snapshot_iteration",
    "safe_batch_processing",
    "validate_numbers",
    "immutable_filter",
    "process_if_valid",
    "safe_dictionary_iteration",
    "safe_set_iteration",
]