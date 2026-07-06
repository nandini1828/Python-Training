from comprehensions.nested_comprehension import flatten_matrix, make_grid


def test_flatten_matrix():
    assert flatten_matrix([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]


def test_make_grid():
    assert make_grid(2, 3) == [[0, 1, 2], [0, 1, 2]]
