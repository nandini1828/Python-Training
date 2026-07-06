from typing import Any, Iterable, Sequence


def matrix_transpose(matrix: Sequence[Sequence[int]]) -> list[list[int]]:
    """Transpose a rectangular matrix."""
    if not matrix:
        return []

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("matrix rows must have the same length")

    return [[row[index] for row in matrix] for index in range(len(matrix[0]))]


def pairs(numbers: Iterable[int]) -> list[tuple[int, int]]:
    """Return ordered pairs where the two values differ."""
    values = list(numbers)
    return [(x, y) for x in values for y in values if x != y]


def flatten_nested_lists(nested: Iterable[Iterable[Any]]) -> list[Any]:
    """Flatten one level of nested lists or iterables."""
    return [item for sublist in nested for item in sublist]


def filter_nested(matrix: Iterable[Iterable[int]], threshold: int) -> list[list[int]]:
    """Filter each row independently by threshold."""
    return [[item for item in row if item > threshold] for row in matrix]


def multiplication_table(size: int) -> list[list[int]]:
    """Return a square multiplication table from 1 through size."""
    if size < 1:
        return []

    return [
        [row * column for column in range(1, size + 1)]
        for row in range(1, size + 1)
    ]
