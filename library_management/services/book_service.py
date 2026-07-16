from typing import List, Optional

from data.store import books
from models.book import Book
from utils.id_generator import generate_book_id


def get_all_books() -> List[dict]:
    return [book.to_dict() for book in books]


def find_book_by_id(book_id: int) -> Optional[Book]:
    return next((book for book in books if book.book_id == book_id), None)


def find_books_by_title(title: str) -> List[dict]:
    return [book.to_dict() for book in books if title.lower() in book.title.lower()]


def find_books_by_author(author: str) -> List[dict]:
    return [book.to_dict() for book in books if author.lower() in book.author.lower()]


def find_books_by_category(category: str) -> List[dict]:
    return [book.to_dict() for book in books if category.lower() == book.category.lower()]


def get_available_books() -> List[dict]:
    return [book.to_dict() for book in books if book.is_available()]


def create_book(title: str, author: str, category: str, isbn: str, total_stock: int) -> dict:
    if any(book.isbn == isbn for book in books):
        raise ValueError("ISBN already exists.")

    book = Book(title=title, author=author, category=category, isbn=isbn, total_stock=total_stock)
    book.book_id = generate_book_id()
    books.append(book)
    return book.to_dict()


def update_book(book_id: int, title: str, author: str, category: str, isbn: str, total_stock: int) -> Optional[dict]:
    book = find_book_by_id(book_id)
    if book is None:
        return None

    if isbn != book.isbn and any(existing.isbn == isbn for existing in books):
        raise ValueError("ISBN already exists.")

    book.title = title
    book.author = author
    book.category = category
    book.isbn = isbn
    book.total_stock = total_stock
    book.available_stock = min(book.available_stock, total_stock)
    return book.to_dict()


def patch_book(book_id: int, title: str | None, author: str | None, category: str | None, isbn: str | None, total_stock: int | None) -> Optional[dict]:
    book = find_book_by_id(book_id)
    if book is None:
        return None

    if isbn and isbn != book.isbn and any(existing.isbn == isbn for existing in books):
        raise ValueError("ISBN already exists.")

    if title:
        book.title = title
    if author:
        book.author = author
    if category:
        book.category = category
    if isbn:
        book.isbn = isbn
    if total_stock is not None:
        book.total_stock = total_stock
        book.available_stock = min(book.available_stock, total_stock)

    return book.to_dict()


def delete_book(book_id: int) -> bool:
    book = find_book_by_id(book_id)
    if book is None:
        return False

    if book.total_stock != book.available_stock:
        raise ValueError("Cannot delete a book with active issues.")

    books.remove(book)
    return True
