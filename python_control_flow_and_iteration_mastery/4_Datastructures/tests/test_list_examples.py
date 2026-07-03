"""
Tests for list_examples.py
"""

from datastructures import ListExamples


def test_iterate_list():
    assert ListExamples.iterate_list([1, 2, 3]) == [1, 2, 3]


def test_access_index():
    assert ListExamples.access_index([10, 20, 30], 1) == 20


def test_slice_list():
    assert ListExamples.slice_list([1, 2, 3, 4, 5]) == [1, 2, 3]


def test_first_element():
    assert ListExamples.first_element([5, 10, 15]) == 5


def test_last_element():
    assert ListExamples.last_element([5, 10, 15]) == 15