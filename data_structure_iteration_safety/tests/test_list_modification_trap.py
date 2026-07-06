"""
Unit tests for list_modification_trap.py
"""

from model import Product
from list_modification_trap import remove_expired_products


def test_remove_expired_products():
    """
    Verify expired products are removed safely.
    """

    products = [
        Product(101, "Laptop", "Electronics", 10, False),
        Product(102, "Milk", "Groceries", 5, True),
        Product(103, "Keyboard", "Electronics", 15, False),
        Product(104, "Bread", "Groceries", 8, True),
    ]

    result = remove_expired_products(products)

    assert len(result) == 2
    assert result[0].name == "Laptop"
    assert result[1].name == "Keyboard"


def test_no_expired_products():

    products = [
        Product(101, "Laptop", "Electronics", 10, False),
        Product(102, "Mouse", "Electronics", 20, False),
    ]

    result = remove_expired_products(products)

    assert len(result) == 2


def test_all_products_expired():

    products = [
        Product(101, "Milk", "Groceries", 5, True),
        Product(102, "Bread", "Groceries", 6, True),
    ]

    result = remove_expired_products(products)

    assert result == []