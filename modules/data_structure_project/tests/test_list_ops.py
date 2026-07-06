from data_structures.list_ops import first_and_last, iterate_with_index, middle_slice


def test_first_and_last():
    assert first_and_last([10, 20, 30]) == (10, 30)


def test_middle_slice():
    assert middle_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_iterate_with_index():
    assert iterate_with_index(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]
