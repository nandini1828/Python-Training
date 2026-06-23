"""Tests for safe_cast function."""
from python_datatypes_mastery.primitives.casting import safe_cast


def test_safe_cast_valid_int():
    assert safe_cast("123", int, default=0) == 123


def test_safe_cast_invalid_int_returns_default():
    assert safe_cast("abc", int, default=-1) == -1


def test_safe_cast_list_from_string():
    assert safe_cast("a b c", list, default=[]) == ["a", "b", "c"]


def test_safe_cast_bool_from_string():
    assert safe_cast("True", bool, default=False) is True
    assert safe_cast("no", bool, default=True) is False
