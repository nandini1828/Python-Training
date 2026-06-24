from python_datatypes.dictionary_methods import flatten_dictionary, filter_dictionary, merge_dictionary, dictionary_statistics


def test_merge_dictionary_combines_values() -> None:
    base = {"a": 1}
    override = {"b": 2}
    assert merge_dictionary(base, override) == {"a": 1, "b": 2}


def test_filter_dictionary_returns_requested_keys() -> None:
    dictionary = {"a": 1, "b": 2, "c": 3}
    assert filter_dictionary(dictionary, ["a", "c"]) == {"a": 1, "c": 3}


def test_flatten_dictionary_flattens_nested_structures() -> None:
    nested = {"x": {"y": 5}, "z": 10}
    assert flatten_dictionary(nested) == {"x.y": 5, "z": 10}


def test_dictionary_statistics_counts_items() -> None:
    stats = dictionary_statistics({"a": 1, "b": 2})
    assert stats["count"] == 2
    assert stats["keys"] == 2
    assert stats["values"] == 2
