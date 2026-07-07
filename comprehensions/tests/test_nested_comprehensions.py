from comprehensions.nested_comprehensions import nested_comprehension_example


def test_nested_comprehension_flattens_and_creates_grid():
    flattened, grid = nested_comprehension_example()
    assert flattened == [1, 2, 3, 4, 5, 6]
    assert grid == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
