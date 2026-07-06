"""
Unit tests for for_loops.py

This module tests the functionality of displaying products
using a for loop.
"""

from model import Product
from for_loops import display_products


def test_display_products(capsys):
    """
    Verify that all product names are displayed.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", False, False),
        Product("Keyboard", True, False),
    ]

    display_products(products)

    captured = capsys.readouterr()

    assert "Available Products" in captured.out
    assert "Laptop" in captured.out
    assert "Mouse" in captured.out
    assert "Keyboard" in captured.out


def test_display_single_product(capsys):
    """
    Verify displaying only one product.
    """

    products = [
        Product("Monitor", True, False)
    ]

    display_products(products)

    captured = capsys.readouterr()

    assert "Monitor" in captured.out


def test_display_empty_product_list(capsys):
    """
    Verify the function handles an empty list gracefully.
    """

    products = []

    display_products(products)

    captured = capsys.readouterr()

    assert "Available Products" in captured.out