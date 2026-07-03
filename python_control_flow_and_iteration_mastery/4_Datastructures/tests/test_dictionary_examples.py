"""
Tests for dictionary_examples.py
"""

from datastructures import DictionaryExamples


sample = {
    "name": "Bhavya",
    "age": 22
}


def test_iterate_keys():
    assert DictionaryExamples.iterate_keys(sample) == [
        "name",
        "age"
    ]


def test_iterate_values():
    assert DictionaryExamples.iterate_values(sample) == [
        "Bhavya",
        22
    ]


def test_iterate_items():
    assert DictionaryExamples.iterate_items(sample) == [
        ("name", "Bhavya"),
        ("age", 22)
    ]