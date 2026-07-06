"""Examples of nested comprehensions."""

from typing import List


def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """Flatten a 2D list into a single list."""
    return [value for row in matrix for value in row]


def make_grid(rows: int, cols: int) -> List[List[int]]:
    """Create a grid of numbers using a nested comprehension."""
    return [[col for col in range(cols)] for _ in range(rows)]
