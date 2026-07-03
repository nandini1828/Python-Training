from comprehensions.nested_comprehensions import (
    flatten_matrix,
    build_multiplication_grid,
)


def test_flatten_matrix():
    matrix = [[1, 2], [3, 4], [5, 6]]
    assert flatten_matrix(matrix) == [1, 2, 3, 4, 5, 6]


def test_build_multiplication_grid():
    assert build_multiplication_grid(3) == [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9],
    ]