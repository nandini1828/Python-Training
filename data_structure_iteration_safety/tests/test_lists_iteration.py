"""
Unit tests for lists_iteration.py
"""

from model import Product
from lists_iteration import display_products
from lists_iteration import slicing_demo


def test_display_products(capsys):
    """
    Verify that all products are displayed.
    """

    products = [
        Product(101, "Laptop", "Electronics", 15, False),
        Product(102, "Mouse", "Electronics", 30, False),
        Product(103, "Keyboard", "Electronics", 20, False),
    ]

    display_products(products)

    captured = capsys.readouterr()

    assert "Products" in captured.out
    assert "Laptop" in captured.out
    assert "Mouse" in captured.out
    assert "Keyboard" in captured.out


def test_slicing_demo(capsys):
    """
    Verify that only the first three products are displayed.
    """

    products = [
        Product(101, "Laptop", "Electronics", 15, False),
        Product(102, "Mouse", "Electronics", 30, False),
        Product(103, "Keyboard", "Electronics", 20, False),
        Product(104, "Monitor", "Electronics", 10, False),
    ]

    slicing_demo(products)

    captured = capsys.readouterr()

    assert "Laptop" in captured.out
    assert "Mouse" in captured.out
    assert "Keyboard" in captured.out
    assert "Monitor" not in captured.out


def test_empty_product_list(capsys):
    """
    Verify empty product list handling.
    """

    display_products([])

    captured = capsys.readouterr()

    assert "Products" in captured.out