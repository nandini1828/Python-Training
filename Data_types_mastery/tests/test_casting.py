import pytest

from primitives.casting import safe_cast, count_truthy_falsy


def test_safe_cast_valid_float():
    assert safe_cast("12.5", float) == 12.5


def test_safe_cast_valid_int():
    assert safe_cast("123", int) == 123


def test_safe_cast_invalid_int_returns_none():
    assert safe_cast("12.5", int) is None


def test_safe_cast_invalid_int_default():
    assert safe_cast("abc", int, default=0) == 0


def test_safe_cast_empty_string():
    assert safe_cast("", int) is None


def test_safe_cast_none_input():
    assert safe_cast(None, int) is None


def test_safe_cast_boolean():
    assert safe_cast("1", bool) is True


def test_count_truthy_falsy():
    assert count_truthy_falsy([0, "hello", [], None, True, 3.14]) == {
        "truthy": 3,
        "falsy": 3,
    }


def test_count_truthy_all_truthy():
    assert count_truthy_falsy([1, "a", [1], True]) == {
        "truthy": 4,
        "falsy": 0,
    }


def test_count_truthy_all_falsy():
    assert count_truthy_falsy([0, "", [], None, False]) == {
        "truthy": 0,
        "falsy": 5,
    }


def test_count_truthy_empty_list():
    assert count_truthy_falsy([]) == {
        "truthy": 0,
        "falsy": 0,
    }