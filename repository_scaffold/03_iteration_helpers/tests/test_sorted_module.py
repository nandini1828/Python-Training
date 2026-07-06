"""
Unit tests for sorted_module utilities.
"""

from sorted_module.utils import (
    case_insensitive_sort,
    sort_by_length,
    sort_dictionary_items,
    sort_dictionary_keys,
    sort_numbers,
    sort_numbers_descending,
    sort_set,
    sort_strings,
    sort_students_by_marks,
    sort_tuples,
)


def test_sort_numbers():
    assert sort_numbers([5, 2, 8, 1]) == [1, 2, 5, 8]


def test_sort_numbers_descending():
    assert sort_numbers_descending([5, 2, 8, 1]) == [8, 5, 2, 1]


def test_sort_strings():
    assert sort_strings(
        ["Orange", "Apple", "Banana"]
    ) == [
        "Apple",
        "Banana",
        "Orange",
    ]


def test_sort_by_length():
    assert sort_by_length(
        ["Python", "C", "Java"]
    ) == [
        "C",
        "Java",
        "Python",
    ]


def test_sort_dictionary_keys():
    data = {
        "b": 2,
        "a": 1,
        "c": 3,
    }

    assert sort_dictionary_keys(data) == [
        "a",
        "b",
        "c",
    ]


def test_sort_dictionary_items():
    data = {
        "b": 2,
        "a": 1,
    }

    assert sort_dictionary_items(data) == [
        ("a", 1),
        ("b", 2),
    ]


def test_sort_tuples():
    items = [
        (3, 4),
        (1, 8),
        (2, 5),
    ]

    assert sort_tuples(items) == [
        (1, 8),
        (2, 5),
        (3, 4),
    ]


def test_sort_students_by_marks():
    students = [
        ("Ganesh", 95),
        ("Rahul", 88),
        ("Priya", 91),
    ]

    assert sort_students_by_marks(students) == [
        ("Ganesh", 95),
        ("Priya", 91),
        ("Rahul", 88),
    ]


def test_case_insensitive_sort():
    values = [
        "python",
        "Java",
        "c",
        "Go",
    ]

    assert case_insensitive_sort(values) == [
        "c",
        "Go",
        "Java",
        "python",
    ]


def test_sort_set():
    assert sort_set({5, 1, 3}) == [1, 3, 5]