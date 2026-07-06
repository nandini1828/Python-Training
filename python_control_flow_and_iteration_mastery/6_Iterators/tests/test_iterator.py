"""
Tests for iterator_examples.py
"""

from Iterators import IteratorExamples


def test_next_element():
    assert (
        IteratorExamples.next_element(
            [10, 20, 30]
        )
        == 10
    )


def test_iterate_manually():
    assert (
        IteratorExamples.iterate_manually(
            [1, 2, 3]
        )
        == [1, 2, 3]
    )


def test_custom_iterator():
    assert (
        IteratorExamples.custom_iterator(5)
        == [1, 2, 3, 4, 5]
    )