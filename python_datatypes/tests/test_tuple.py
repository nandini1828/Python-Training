from tuple_methods.tuple_utils import to_list, count_value


def test_to_list_and_count():
    t = (1, 2, 2, 3)
    assert to_list(t) == [1, 2, 2, 3]
    assert count_value(t, 2) == 2
