"""
Tests for for_else.py
"""

from loops import ForElseExamples


def test_search_number_found():
    assert (
        ForElseExamples.search_number(
            [10, 20, 30],
            20
        )
        == "Number Found"
    )


def test_search_number_not_found():
    assert (
        ForElseExamples.search_number(
            [10, 20, 30],
            50
        )
        == "Number Not Found"
    )


def test_search_name_found():
    assert (
        ForElseExamples.search_name(
            ["Alice", "Bob"],
            "Bob"
        )
        == "Name Found"
    )