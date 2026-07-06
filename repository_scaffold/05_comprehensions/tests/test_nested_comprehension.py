from nested_comprehension.utils import (
    filter_nested,
    flatten_nested_lists,
    matrix_transpose,
    multiplication_table,
    pairs,
)


def test_nested_comprehension_helpers():
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert pairs([1, 2]) == [(1, 2), (2, 1)]
    assert flatten_nested_lists([[1], [2]]) == [1, 2]
    assert filter_nested([[1, 3], [4]], 2) == [[3], [4]]
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert multiplication_table(0) == []

    try:
        matrix_transpose([[1, 2], [3]])
    except ValueError as error:
        assert str(error) == 'matrix rows must have the same length'
    else:
        raise AssertionError('matrix_transpose should reject ragged matrices')
