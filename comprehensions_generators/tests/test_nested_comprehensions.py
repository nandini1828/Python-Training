"""
Unit tests for nested_comprehensions.py

Run:

    pytest tests/test_nested_comprehensions.py

Author: Python Training
"""

from __future__ import annotations

from comprehensions_generators.nested_comprehensions import (
    cartesian_product,
    chessboard_coordinates,
    coordinate_grid,
    even_matrix,
    flatten_strings,
    identity_matrix,
    multiplication_grid,
    transpose_matrix,
)


def test_multiplication_grid() -> None:
    """Test multiplication grid."""
    result = multiplication_grid(
        3,
        3,
    )

    assert result == [
        [0, 0, 0],
        [0, 1, 2],
        [0, 2, 4],
    ]


def test_transpose_matrix() -> None:
    """Test transpose."""
    matrix = [
        [1, 2],
        [3, 4],
    ]

    assert transpose_matrix(matrix) == [
        [1, 3],
        [2, 4],
    ]


def test_transpose_empty() -> None:
    """Empty matrix."""
    assert transpose_matrix([]) == []


def test_chessboard_coordinates() -> None:
    """Chessboard."""
    board = chessboard_coordinates()

    assert len(board) == 64
    assert board[0] == "A1"
    assert board[-1] == "H8"


def test_coordinate_grid() -> None:
    """Coordinate grid."""
    result = coordinate_grid(
        2,
        2,
    )

    assert result == [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]


def test_cartesian_product() -> None:
    """Cartesian product."""
    result = cartesian_product(
        ["A"],
        ["1", "2"],
    )

    assert result == [
        ("A", "1"),
        ("A", "2"),
    ]


def test_identity_matrix() -> None:
    """Identity matrix."""
    result = identity_matrix(3)

    assert result == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]


def test_even_matrix() -> None:
    """Even matrix."""
    result = even_matrix(
        2,
        3,
    )

    assert result == [
        [0, 2, 4],
        [6, 8, 10],
    ]


def test_flatten_strings() -> None:
    """Flatten nested strings."""
    values = [
        [
            "Python",
            "Django",
        ],
        [
            "FastAPI",
            "Flask",
        ],
    ]

    assert flatten_strings(values) == [
        "Python",
        "Django",
        "FastAPI",
        "Flask",
    ]


def test_empty_flatten() -> None:
    """Empty flatten."""
    assert flatten_strings([]) == []