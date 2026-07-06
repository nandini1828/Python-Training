from data_structures.dictionary_ops import collect_items, collect_keys, collect_values


def test_dictionary_iteration_helpers():
    mapping = {"a": 1, "b": 2}
    assert collect_keys(mapping) == ["a", "b"]
    assert collect_values(mapping) == [1, 2]
    assert collect_items(mapping) == [("a", 1), ("b", 2)]
