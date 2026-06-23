import pytest

from primitives.casting import safe_cast, count_truthy_falsy


def test_safe_cast_valid_float():
    assert safe_cast("12.5", float) == 12.5


def test_safe_cast_invalid_int_returns_none():
    assert safe_cast("12.5", int) is None


def test_safe_cast_invalid_int_default():
    assert safe_cast("abc", int, default=0) == 0


def test_count_truthy_falsy():
    assert count_truthy_falsy([0, "hello", [], None, True, 3.14]) == {"truthy": 3, "falsy": 3}
