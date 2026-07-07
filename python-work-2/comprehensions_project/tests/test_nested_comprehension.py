from nested_comprehension import (
    flatten_matrix,
    create_grid,
)


def test_flatten_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]

    assert flatten_matrix(matrix) == [
        1,
        2,
        3,
        4,
    ]


def test_flatten_empty():
    assert flatten_matrix([]) == []


def test_create_grid():
    assert create_grid(2, 3) == [
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_create_empty_grid():
    assert create_grid(0, 3) == []