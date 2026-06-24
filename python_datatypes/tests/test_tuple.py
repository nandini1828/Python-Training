from python_datatypes.tuple_methods import tuple_slice, tuple_statistics, tuple_to_list


def test_tuple_to_list_converts_tuple() -> None:
    assert tuple_to_list((1, 2, 3)) == [1, 2, 3]


def test_tuple_slice_returns_slice() -> None:
    assert tuple_slice((10, 20, 30, 40), 1, 3) == (20, 30)


def test_tuple_statistics_counts_uniques() -> None:
    stats = tuple_statistics((1, 2, 2, 3))
    assert stats["length"] == 4
    assert stats["unique"] == 3
