from tuples.tuple_methods import (
    tuple_count,
    tuple_index
)


def test_tuple_count():
    data = (1, 2, 2, 3, 2)
    assert tuple_count(data, 2) == 3
    assert tuple_count(data, 1) == 1
    assert tuple_count(data, 9) == 0


def test_tuple_index():
    data = ("a", "b", "c", "b")

    assert tuple_index(data, "b") == 1
    assert tuple_index(data, "c") == 2


def test_tuple_index_error_handling():
    data = (1, 2, 3)

    # assuming safe behavior (recommended design)
    assert tuple_index(data, 99, default=-1) == -1