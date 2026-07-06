"""
Unit tests for enumerate_helper utilities.
"""

from enumerate_module.utils import (
    create_index_dictionary,
    create_student_records,
    enumerate_characters,
    enumerate_items,
    enumerate_tuple,
    enumerate_with_start,
    even_index_items,
    find_item_index,
    number_lines,
    odd_index_items,
)


def test_enumerate_items():
    items = ["A", "B", "C"]
    assert enumerate_items(items) == [
        (0, "A"),
        (1, "B"),
        (2, "C"),
    ]


def test_enumerate_with_start():
    items = ["A", "B", "C"]
    assert enumerate_with_start(items, 10) == [
        (10, "A"),
        (11, "B"),
        (12, "C"),
    ]


def test_create_index_dictionary():
    items = ["Python", "Java"]
    assert create_index_dictionary(items) == {
        0: "Python",
        1: "Java",
    }


def test_find_item_index():
    items = ["Apple", "Banana", "Orange"]

    assert find_item_index(items, "Banana") == 1
    assert find_item_index(items, "Mango") == -1


def test_number_lines():
    lines = ["Line 1", "Line 2"]

    assert number_lines(lines) == [
        "1. Line 1",
        "2. Line 2",
    ]


def test_enumerate_characters():
    assert enumerate_characters("ABC") == [
        (0, "A"),
        (1, "B"),
        (2, "C"),
    ]


def test_enumerate_tuple():
    values = (10, 20, 30)

    assert enumerate_tuple(values) == [
        (0, 10),
        (1, 20),
        (2, 30),
    ]


def test_create_student_records():
    students = ["Ganesh", "Rahul"]

    assert create_student_records(students, 101) == {
        101: "Ganesh",
        102: "Rahul",
    }


def test_even_index_items():
    values = ["A", "B", "C", "D", "E"]

    assert even_index_items(values) == [
        "A",
        "C",
        "E",
    ]


def test_odd_index_items():
    values = ["A", "B", "C", "D", "E"]

    assert odd_index_items(values) == [
        "B",
        "D",
    ]