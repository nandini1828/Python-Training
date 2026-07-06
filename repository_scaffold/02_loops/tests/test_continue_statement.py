"""
test_continue_statement.py

Pytest test cases for continue_statement utilities.
Run:
    pytest
"""

from continue_statement import (
    skip_even,
    skip_negatives,
    skip_empty,
    skip_multiples_of_three,
    valid_emails,
    safe_division,
    valid_students,
)


def test_skip_even():
    assert skip_even([1, 2, 3, 4, 5]) == [1, 3, 5]


def test_skip_negatives():
    assert skip_negatives([10, -5, 20, -1]) == [10, 20]


def test_skip_empty():
    assert skip_empty(["A", "", "B"]) == ["A", "B"]


def test_skip_multiples_of_three():
    assert skip_multiples_of_three([1, 3, 4, 6, 7]) == [1, 4, 7]


def test_valid_emails():
    assert valid_emails(["a@gmail.com", "invalid", "b@yahoo.com"]) == [
        "a@gmail.com",
        "b@yahoo.com",
    ]


def test_safe_division():
    result = safe_division([10, 0, 5])
    assert result == [1.0, 2.0]


def test_valid_students():
    students = [
        {"name": "A", "marks": 90},
        {"name": "B", "marks": -1},
        {"name": "C", "marks": 80},
    ]

    assert valid_students(students) == [
        {"name": "A", "marks": 90},
        {"name": "C", "marks": 80},
    ]