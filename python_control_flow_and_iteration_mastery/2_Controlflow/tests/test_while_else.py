"""
Tests for while_else.py
"""

from loops import WhileElseExamples


def test_count():
    assert (
        WhileElseExamples.count(3)
        == [1, 2, 3, "Completed"]
    )


def test_search_number_found():
    assert (
        WhileElseExamples.search_number(
            [10, 20, 30],
            20
        )
        == "Number Found"
    )


def test_search_number_not_found():
    assert (
        WhileElseExamples.search_number(
            [10, 20, 30],
            40
        )
        == "Number Not Found"
    )