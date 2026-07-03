from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.dictionary_iteration import (
    get_dictionary_keys,
    get_dictionary_values,
    get_dictionary_items,
)


def test_get_dictionary_keys():
    assert get_dictionary_keys({"a": 1, "b": 2}) == ["a", "b"]


def test_get_dictionary_values():
    assert get_dictionary_values({"a": 1, "b": 2}) == [1, 2]


def test_get_dictionary_items():
    assert get_dictionary_items({"a": 1, "b": 2}) == [("a", 1), ("b", 2)]