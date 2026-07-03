"""
Tests for list_modification.py
"""

from datastructures import ListModificationExamples


def test_remove_even_wrong():
    assert ListModificationExamples.remove_even_wrong(
        [1, 2, 3, 4]
    ) == [1, 3]


def test_remove_even_correct():
    assert ListModificationExamples.remove_even_correct(
        [1, 2, 3, 4, 5, 6]
    ) == [1, 3, 5]