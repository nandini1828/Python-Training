from data_structures.set_ops import contains_value, create_unique_collection


def test_set_ops():
    values = create_unique_collection([1, 2, 2, 3])
    assert values == {1, 2, 3}
    assert contains_value(values, 2) is True
    assert contains_value(values, 4) is False
