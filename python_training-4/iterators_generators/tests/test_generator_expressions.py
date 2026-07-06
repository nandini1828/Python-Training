"""
Unit tests for generator_expressions.py

This module tests generator expressions.
"""

from model import Book
from generator_expressions import discounted_prices


def test_discounted_prices(capsys):
    """
    Verify discounted prices are generated.
    """

    books = [
        Book(101, "Python", 100),
        Book(102, "Django", 200),
        Book(103, "FastAPI", 300),
    ]

    discounted_prices(books)

    captured = capsys.readouterr()

    assert "90.0" in captured.out
    assert "180.0" in captured.out
    assert "270.0" in captured.out


def test_generator_expression_directly():
    """
    Verify generator expression values.
    """

    books = [
        Book(101, "Python", 100),
        Book(102, "Django", 200),
    ]

    prices = (
        book.price * 0.90
        for book in books
    )

    assert list(prices) == [90.0, 180.0]


def test_empty_generator_expression(capsys):
    """
    Verify empty book list.
    """

    discounted_prices([])

    captured = capsys.readouterr()

    assert "Discounted Prices" in captured.out


def test_generator_object():
    """
    Verify generator expression creates
    a generator object.
    """

    books = [
        Book(101, "Python", 100)
    ]

    prices = (
        book.price * 0.90
        for book in books
    )

    assert hasattr(prices, "__iter__")
    assert hasattr(prices, "__next__")