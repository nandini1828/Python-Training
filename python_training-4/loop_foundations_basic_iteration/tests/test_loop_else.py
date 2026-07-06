"""
Unit tests for loop_else.py

This module tests the functionality of for-else
and while-else loops.
"""

from model import Product
from loop_else import search_product, complete_deliveries


def test_search_existing_product(capsys):
    """
    Verify that an existing product is found
    and the for-else loop exits using break.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", True, False),
        Product("Keyboard", True, False),
    ]

    search_product(products, "Mouse")

    captured = capsys.readouterr()

    assert "Searching Product" in captured.out
    assert "Mouse Found" in captured.out
    assert "Mouse Not Found" not in captured.out


def test_search_missing_product(capsys):
    """
    Verify that the else block executes
    when the product is not found.
    """

    products = [
        Product("Laptop", True, False),
        Product("Mouse", True, False),
        Product("Keyboard", True, False),
    ]

    search_product(products, "Monitor")

    captured = capsys.readouterr()

    assert "Searching Product" in captured.out
    assert "Monitor Not Found" in captured.out


def test_search_empty_list(capsys):
    """
    Verify searching in an empty list.
    """

    products = []

    search_product(products, "Laptop")

    captured = capsys.readouterr()

    assert "Searching Product" in captured.out
    assert "Laptop Not Found" in captured.out


def test_complete_deliveries(capsys):
    """
    Verify that while-else executes
    after all deliveries are completed.
    """

    complete_deliveries(3)

    captured = capsys.readouterr()

    assert "Completed Delivery 1" in captured.out
    assert "Completed Delivery 2" in captured.out
    assert "Completed Delivery 3" in captured.out
    assert "All Deliveries Completed Successfully" in captured.out


def test_complete_zero_deliveries(capsys):
    """
    Verify that while-else executes
    even when there are zero deliveries.
    """

    complete_deliveries(0)

    captured = capsys.readouterr()

    assert "Completing Deliveries" in captured.out
    assert "All Deliveries Completed Successfully" in captured.out