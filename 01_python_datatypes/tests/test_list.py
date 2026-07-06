from list_methods.list_utils import unique, chunk


def test_unique_preserves_order():
    assert unique([1, 2, 1, 3]) == [1, 2, 3]


def test_chunk_small():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
