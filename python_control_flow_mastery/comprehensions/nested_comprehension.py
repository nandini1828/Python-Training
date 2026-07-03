"""Examples showing nested comprehensions."""

from __future__ import annotations


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """Flatten a matrix using a nested comprehension.

    Args:
        matrix: A list of rows.

    Returns:
        A flattened list of integers.
    """
    return [value for row in matrix for value in row]
