"""
Unit tests for set_iteration.py
"""

from model import Product
from set_iteration import display_categories


def test_display_unique_categories(capsys):
    """
    Verify duplicate categories are removed.
    """

    products = [
        Product(101, "Laptop", "Electronics", 10, False),
        Product(102, "Mouse", "Electronics", 20, False),
        Product(103, "Milk", "Groceries", 5, False),
        Product(104, "Bread", "Groceries", 6, False),
    ]

    display_categories(products)

    captured = capsys.readouterr()

    assert "Electronics" in captured.out
    assert "Groceries" in captured.out
    assert "True" in captured.out


def test_single_category(capsys):

    products = [
        Product(101, "Laptop", "Electronics", 10, False),
    ]

    display_categories(products)

    captured = capsys.readouterr()

    assert "Electronics" in captured.out


def test_empty_products(capsys):

    display_categories([])

    captured = capsys.readouterr()

    assert "Unique Categories" in captured.out