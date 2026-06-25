from __future__ import annotations

from dictionary_methods.dictionary_utils import (
    DictionaryMethods,
    filter_by_value,
    invert_mapping,
    merge_dictionaries,
)


def test_merge_dictionaries() -> None:
    result = merge_dictionaries({"a": 1}, {"b": 2})
    assert result == {"a": 1, "b": 2}


def test_invert_mapping() -> None:
    result = invert_mapping({"a": 1, "b": 1, "c": 2})
    assert result == {1: ["a", "b"], 2: ["c"]}


def test_filter_by_value() -> None:
    result = filter_by_value({"a": 1, "b": 2, "c": 3}, lambda value: value > 1)
    assert result == {"b": 2, "c": 3}


def test_dictionary_methods_helper() -> None:
    helper = DictionaryMethods({"name": "Ada", "age": 21})
    assert helper.get_value("name") == "Ada"
    assert helper.get_value("city", "Unknown") == "Unknown"
    assert set(helper.keys()) == {"name", "age"}
