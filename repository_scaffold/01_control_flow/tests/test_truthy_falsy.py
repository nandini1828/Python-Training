"""
Unit tests for truthy_falsy utilities.
"""

from truthy_falsy.utils import *


def test_is_truthy():
    assert is_truthy(10) is True
    assert is_truthy("Python") is True


def test_is_falsy():
    assert is_falsy(0) is True
    assert is_falsy([]) is True


def test_empty_string():
    assert is_empty_string("")
    assert not is_empty_string("Hello")


def test_non_empty_string():
    assert is_non_empty_string("Python")
    assert not is_non_empty_string("")


def test_empty_list():
    assert is_empty_list([])
    assert not is_empty_list([1])


def test_non_empty_list():
    assert is_non_empty_list([1])
    assert not is_non_empty_list([])


def test_none():
    assert is_none(None)
    assert not is_none(10)


def test_zero():
    assert is_zero(0)
    assert not is_zero(5)


def test_cart():
    assert cart_has_items(["Laptop"])
    assert not cart_has_items([])