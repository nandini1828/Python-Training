from utilities.constants import AVAILABLE, BORROWED
from utilities.file_handler import load_books, load_members, save_books, save_members
from utilities.helpers import normalize_title
from utilities.validators import validate_book_payload, validate_member_payload


def _load_books() -> list:
    return load_books()


def _load_members() -> list:
    return load_members()


def create_book(payload: dict) -> dict:
    validate_book_payload(payload)
    books = _load_books()
    next_id = max((book["id"] for book in books), default=0) + 1
    book = {
        "id": next_id,
        "title": normalize_title(payload["title"]),
        "author": normalize_title(payload["author"]),
        "isbn": payload["isbn"],
        "status": payload.get("status", AVAILABLE),
    }
    books.append(book)
    save_books(books)
    return book


def list_books() -> list[dict]:
    # sorted() helps present the books in a predictable order.
    return sorted(_load_books(), key=lambda book: book["title"])


def get_book(book_id: int):
    for book in _load_books():
        if book["id"] == book_id:
            return book
    return None


def update_book(book_id: int, payload: dict):
    books = _load_books()
    for book in books:
        if book["id"] == book_id:
            book.update(payload)
            save_books(books)
            return book
    return None


def delete_book(book_id: int) -> bool:
    # Avoid deleting from a list while iterating over it directly because the index shifts.
    books = _load_books()
    remaining = [book for book in books if book["id"] != book_id]
    if len(remaining) == len(books):
        return False
    save_books(remaining)
    return True


def create_member(payload: dict) -> dict:
    validate_member_payload(payload)
    members = _load_members()
    next_id = max((member["id"] for member in members), default=0) + 1
    member = {
        "id": next_id,
        "name": payload["name"].strip(),
        "email": payload["email"].strip(),
        "borrowed_books": [],
    }
    members.append(member)
    save_members(members)
    return member


def list_members() -> list[dict]:
    return sorted(_load_members(), key=lambda member: member["name"])


def get_member(member_id: int):
    for member in _load_members():
        if member["id"] == member_id:
            return member
    return None


def borrow_book(book_id: int, member_id: int):
    book = get_book(book_id)
    member = get_member(member_id)
    if not book or not member:
        return None
    if book["status"] == BORROWED:
        return {"message": "Book is already borrowed"}
    book["status"] = BORROWED
    member["borrowed_books"].append(book_id)
    books = _load_books()
    for stored_book in books:
        if stored_book["id"] == book_id:
            stored_book["status"] = BORROWED
            break
    save_books(books)
    members = _load_members()
    for stored_member in members:
        if stored_member["id"] == member_id:
            stored_member["borrowed_books"] = member["borrowed_books"]
            break
    save_members(members)
    return {"message": "Book borrowed successfully", "book": book, "member": member}
