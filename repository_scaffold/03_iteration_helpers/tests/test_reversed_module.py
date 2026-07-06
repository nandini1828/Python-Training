"""
Unit tests for reversed_module utilities.
"""

from reversed_module.utils import (
    browser_history,
    countdown,
    is_palindrome,
    reverse_keys,
    reverse_lines,
    reverse_list,
    reverse_range,
    reverse_string,
    reverse_tuple,
    reverse_values,
)


def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []


def test_reverse_tuple():
    assert reverse_tuple((10, 20, 30)) == (30, 20, 10)


def test_reverse_string():
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""


def test_reverse_range():
    assert reverse_range(1, 6) == [5, 4, 3, 2, 1]


def test_reverse_lines():
    lines = ["Line 1", "Line 2", "Line 3"]

    assert reverse_lines(lines) == [
        "Line 3",
        "Line 2",
        "Line 1",
    ]


def test_reverse_keys():
    student = {
        "name": "Ganesh",
        "age": 22,
        "course": "Python",
    }

    assert reverse_keys(student) == [
        "course",
        "age",
        "name",
    ]


def test_reverse_values():
    student = {
        "name": "Ganesh",
        "age": 22,
        "course": "Python",
    }

    assert reverse_values(student) == [
        "Python",
        22,
        "Ganesh",
    ]


def test_countdown():
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(1) == [1]


def test_browser_history():
    history = [
        "google.com",
        "github.com",
        "python.org",
    ]

    assert browser_history(history) == [
        "python.org",
        "github.com",
        "google.com",
    ]


def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("Python") is False
    assert is_palindrome("Level") is True