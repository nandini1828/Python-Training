"""
Nested comprehension utilities.
"""


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """
    Flattens a 2D list into a 1D list using nested comprehension.

    Parameters
    ----------
    matrix : list[list[int]]
        Input 2D list.

    Returns
    -------
    list[int]
        Flattened list.
    """
    return [item for row in matrix for item in row]


def build_multiplication_grid(size: int) -> list[list[int]]:
    """
    Builds a multiplication grid using nested comprehensions.

    Parameters
    ----------
    size : int
        Grid size.

    Returns
    -------
    list[list[int]]
        Multiplication grid.
    """
    return [
        [row * column for column in range(1, size + 1)]
        for row in range(1, size + 1)
    ]