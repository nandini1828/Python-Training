"""
Unit tests for iterator_protocol.py

This module tests the custom iterator implementation.
"""

import pytest

from model import Book
from iterator_protocol import BookIterator
from iterator_protocol import browse_books


def test_book_iterator():
    """
    Verify that the custom iterator returns books
    in the correct order.
    """

    books = [
        Book(101, "Python Basics", 599),
        Book(102, "Django Mastery", 799),
        Book(103, "FastAPI Guide", 699),
    ]

    iterator = BookIterator(books)

    assert next(iterator).title == "Python Basics"
    assert next(iterator).title == "Django Mastery"
    assert next(iterator).title == "FastAPI Guide"


def test_stop_iteration():
    """
    Verify StopIteration is raised
    after all books are returned.
    """

    books = [
        Book(101, "Python Basics", 599)
    ]

    iterator = BookIterator(books)

    next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


def test_empty_iterator():

    books = []

    iterator = BookIterator(books)

    with pytest.raises(StopIteration):
        next(iterator)


def test_browse_books(capsys):
    """
    Verify browsing displays every book.
    """

    books = [
        Book(101, "Python Basics", 599),
        Book(102, "Django Mastery", 799),
    ]

    browse_books(books)

    captured = capsys.readouterr()

    assert "Browsing Books" in captured.out
    assert "Python Basics" in captured.out
    assert "Django Mastery" in captured.out