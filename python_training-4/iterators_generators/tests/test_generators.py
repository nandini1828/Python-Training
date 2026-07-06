"""
Unit tests for generators.py

This module tests generator functions
implemented using yield.
"""

from generators import generate_coupons
from generators import display_coupons


def test_generate_coupons():
    """
    Verify generator yields all coupons.
    """

    coupons = list(generate_coupons())

    assert coupons == [
        "SAVE10",
        "SAVE20",
        "FREESHIP"
    ]


def test_generator_next():
    """
    Verify next() retrieves values sequentially.
    """

    coupons = generate_coupons()

    assert next(coupons) == "SAVE10"
    assert next(coupons) == "SAVE20"
    assert next(coupons) == "FREESHIP"


def test_display_coupons(capsys):
    """
    Verify coupons are displayed.
    """

    display_coupons()

    captured = capsys.readouterr()

    assert "SAVE10" in captured.out
    assert "SAVE20" in captured.out
    assert "FREESHIP" in captured.out


def test_generator_exhaustion():

    coupons = generate_coupons()

    list(coupons)

    import pytest

    with pytest.raises(StopIteration):
        next(coupons)