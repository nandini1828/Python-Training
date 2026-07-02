from comprehensions.nested_comprehension import (
    flatten_matrix,
    create_grid,
)


def test_flatten_matrix():

    matrix = [
        [1, 2],
        [3, 4],
    ]

    assert flatten_matrix(matrix) == [1, 2, 3, 4]


def test_create_grid():

    expected = [
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert create_grid(2, 3) == expected