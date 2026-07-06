"""
Unit tests for break_statement.py

This module tests whether the loop correctly stops
when it encounters a damaged product.
"""

from model import Product
from break_statement import inspect_products


def test_break_on_damaged_product(capsys):
    """
    Verify that the loop stops immediately
    after finding a damaged product.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", True, False),
        Product("Monitor", True, True),
        Product("Keyboard", True, False)
    ]

    inspect_products(products)

    captured = capsys.readouterr()

    assert "Laptop passed inspection." in captured.out
    assert "Mouse passed inspection." in captured.out
    assert "Monitor is damaged." in captured.out

    # Keyboard should never be inspected
    assert "Keyboard passed inspection." not in captured.out


def test_no_damaged_products(capsys):
    """
    Verify that every product is inspected
    when no damaged products exist.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", True, False),
        Product("Keyboard", True, False)
    ]

    inspect_products(products)

    captured = capsys.readouterr()

    assert "Laptop passed inspection." in captured.out
    assert "Mouse passed inspection." in captured.out
    assert "Keyboard passed inspection." in captured.out


def test_first_product_damaged(capsys):
    """
    Verify that the loop terminates immediately
    when the first product is damaged.
    """

    products = [
        Product("Laptop", True, True),
        Product("Mouse", True, False),
        Product("Keyboard", True, False)
    ]

    inspect_products(products)

    captured = capsys.readouterr()

    assert "Laptop is damaged." in captured.out

    # Remaining products should never be inspected
    assert "Mouse passed inspection." not in captured.out
    assert "Keyboard passed inspection." not in captured.out


def test_empty_product_list(capsys):
    """
    Verify that an empty product list
    does not raise any errors.
    """

    products = []

    inspect_products(products)

    captured = capsys.readouterr()

    assert "Inspecting Products" in captured.out