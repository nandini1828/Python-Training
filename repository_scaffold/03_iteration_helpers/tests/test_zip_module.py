"""
Unit tests for zip_helper utilities.
"""

from zip_module.utils import (
    compare_lists,
    create_dictionary,
    create_employee_records,
    pair_coordinates,
    student_report,
    total_prices,
    unzip_pairs,
    zip_lists,
    zip_three_lists,
    zip_to_indexed_dict,
)


def test_zip_lists():
    assert zip_lists(
        [1, 2, 3],
        ["A", "B", "C"],
    ) == [
        (1, "A"),
        (2, "B"),
        (3, "C"),
    ]


def test_zip_three_lists():
    assert zip_three_lists(
        [1, 2],
        ["A", "B"],
        [True, False],
    ) == [
        (1, "A", True),
        (2, "B", False),
    ]


def test_create_dictionary():
    assert create_dictionary(
        ["name", "age"],
        ["Ganesh", 22],
    ) == {
        "name": "Ganesh",
        "age": 22,
    }


def test_unzip_pairs():
    pairs = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
    ]

    numbers, letters = unzip_pairs(pairs)

    assert numbers == (1, 2, 3)
    assert letters == ("A", "B", "C")


def test_unzip_empty():
    assert unzip_pairs([]) == ((), ())


def test_compare_lists():
    assert compare_lists(
        [1, 2, 3],
        [1, 5, 3],
    ) == [
        True,
        False,
        True,
    ]


def test_create_employee_records():
    assert create_employee_records(
        [101, 102],
        ["Ganesh", "Rahul"],
    ) == [
        {"id": 101, "name": "Ganesh"},
        {"id": 102, "name": "Rahul"},
    ]


def test_pair_coordinates():
    assert pair_coordinates(
        [1, 2],
        [3, 4],
    ) == [
        (1, 3),
        (2, 4),
    ]


def test_student_report():
    assert student_report(
        ["Ganesh", "Rahul"],
        ["A", "B"],
    ) == [
        "Ganesh -> Grade A",
        "Rahul -> Grade B",
    ]


def test_total_prices():
    assert total_prices(
        ["Laptop", "Mouse"],
        [50000, 800],
    ) == [
        "Laptop: ₹50000",
        "Mouse: ₹800",
    ]


def test_zip_to_indexed_dict():
    assert zip_to_indexed_dict(
        ["A", "B"],
        [1, 2],
    ) == {
        0: ("A", 1),
        1: ("B", 2),
    }