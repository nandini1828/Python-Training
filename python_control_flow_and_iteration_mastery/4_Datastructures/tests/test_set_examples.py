"""
Tests for set_examples.py
"""

from datastructures import SetExamples


def test_check_membership():
    assert (
        SetExamples.check_membership(
            {1, 2, 3},
            2
        )
    )


def test_remove_duplicates():
    result = SetExamples.remove_duplicates(
        [1, 2, 2, 3, 3]
    )

    assert set(result) == {1, 2, 3}


def test_add_element():
    assert (
        SetExamples.add_element(
            {1, 2},
            3
        )
        == {1, 2, 3}
    )


def test_iterate_set():
    result = SetExamples.iterate_set(
        {1, 2, 3}
    )

    assert set(result) == {1, 2, 3}