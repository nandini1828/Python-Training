"""
Unit tests for continue_statement.py

This module tests whether unavailable products
are skipped while shipping available products.
"""

from model import Product
from continue_statement import ship_products


def test_skip_unavailable_products(capsys):
    """
    Verify that unavailable products are skipped
    and available products are shipped.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", False, False),
        Product("Keyboard", True, False),
        Product("Monitor", False, False),
    ]

    ship_products(products)

    captured = capsys.readouterr()

    assert "Shipping Laptop" in captured.out
    assert "Shipping Keyboard" in captured.out

    # These products should be skipped
    assert "Shipping Mouse" not in captured.out
    assert "Shipping Monitor" not in captured.out


def test_all_products_available(capsys):
    """
    Verify that all products are shipped
    when every product is available.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", True, False),
        Product("Keyboard", True, False),
    ]

    ship_products(products)

    captured = capsys.readouterr()

    assert "Shipping Laptop" in captured.out
    assert "Shipping Mouse" in captured.out
    assert "Shipping Keyboard" in captured.out


def test_no_products_available(capsys):
    """
    Verify that no shipping occurs
    when all products are unavailable.
    """

    products = [
        Product("Laptop", False, False),
        Product("Mouse", False, False),
        Product("Keyboard", False, False),
    ]

    ship_products(products)

    captured = capsys.readouterr()

    assert "Shipping Products" in captured.out

    assert "Shipping Laptop" not in captured.out
    assert "Shipping Mouse" not in captured.out
    assert "Shipping Keyboard" not in captured.out


def test_empty_product_list(capsys):
    """
    Verify that an empty product list
    is handled without errors.
    """

    products = []

    ship_products(products)

    captured = capsys.readouterr()

    assert "Shipping Products" in captured.out