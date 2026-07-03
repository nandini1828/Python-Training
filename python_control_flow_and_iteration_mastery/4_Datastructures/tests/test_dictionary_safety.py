"""
Tests for dictionary_safety.py
"""

from datastructures import DictionarySafetyExamples


sample = {
    "name": "Bhavya"
}


def test_safe_get_existing():
    assert (
        DictionarySafetyExamples.safe_get(
            sample,
            "name"
        )
        == "Bhavya"
    )


def test_safe_get_missing():
    assert (
        DictionarySafetyExamples.safe_get(
            sample,
            "city"
        )
        == "Key Not Found"
    )


def test_default_dictionary():
    assert (
        DictionarySafetyExamples.default_dictionary()
        == {"Python": 10}
    )


def test_check_key():
    assert (
        DictionarySafetyExamples.check_key(
            sample,
            "name"
        )
    )