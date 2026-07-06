"""
Examples demonstrating nested comprehensions.

Topics covered:

- Matrix flattening
- Matrix transpose
- Cartesian products
- Coordinate generation
- Multiplication grids

Author: Python Training
"""

from __future__ import annotations


def multiplication_grid(
    rows: int,
    columns: int,
) -> list[list[int]]:
    """
    Build a multiplication grid.

    Args:
        rows:
            Number of rows.

        columns:
            Number of columns.

    Returns:
        Multiplication grid.
    """
    return [
        [
            row * column
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def transpose_matrix(
    matrix: list[list[int]],
) -> list[list[int]]:
    """
    Transpose a matrix.

    Args:
        matrix:
            Input matrix.

    Returns:
        Transposed matrix.
    """
    if not matrix:
        return []

    return [
        [
            row[column]
            for row in matrix
        ]
        for column in range(len(matrix[0]))
    ]


def chessboard_coordinates() -> list[str]:
    """
    Generate chessboard coordinates.

    Returns:
        Chessboard positions.
    """
    return [
        f"{column}{row}"
        for row in range(1, 9)
        for column in "ABCDEFGH"
    ]


def coordinate_grid(
    rows: int,
    columns: int,
) -> list[tuple[int, int]]:
    """
    Generate coordinate pairs.

    Args:
        rows:
            Number of rows.

        columns:
            Number of columns.

    Returns:
        Coordinate pairs.
    """
    return [
        (row, column)
        for row in range(rows)
        for column in range(columns)
    ]


def cartesian_product(
    first: list[str],
    second: list[str],
) -> list[tuple[str, str]]:
    """
    Build a Cartesian product.

    Args:
        first:
            First collection.

        second:
            Second collection.

    Returns:
        Cartesian product.
    """
    return [
        (left, right)
        for left in first
        for right in second
    ]


def identity_matrix(
    size: int,
) -> list[list[int]]:
    """
    Build an identity matrix.

    Args:
        size:
            Matrix size.

    Returns:
        Identity matrix.
    """
    return [
        [
            1 if row == column else 0
            for column in range(size)
        ]
        for row in range(size)
    ]


def even_matrix(
    rows: int,
    columns: int,
) -> list[list[int]]:
    """
    Build a matrix of even numbers.

    Args:
        rows:
            Number of rows.

        columns:
            Number of columns.

    Returns:
        Matrix of even values.
    """
    return [
        [
            (row * columns + column) * 2
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def flatten_strings(
    values: list[list[str]],
) -> list[str]:
    """
    Flatten nested string lists.

    Args:
        values:
            Nested list.

    Returns:
        Flat list.
    """
    return [
        item
        for group in values
        for item in group
    ]


__all__ = [
    "multiplication_grid",
    "transpose_matrix",
    "chessboard_coordinates",
    "coordinate_grid",
    "cartesian_product",
    "identity_matrix",
    "even_matrix",
    "flatten_strings",
]