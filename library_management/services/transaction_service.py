from collections import Counter
from typing import List, Optional

from data.store import books, members, reserved_books, transactions
from models.transaction import Transaction
from utils.id_generator import generate_transaction_id


def get_all_transactions() -> List[dict]:
    return [transaction.to_dict() for transaction in transactions]


def find_transaction_by_id(transaction_id: int) -> Optional[Transaction]:
    return next((tx for tx in transactions if tx.transaction_id == transaction_id), None)


def get_issued_books() -> List[dict]:
    return [tx.to_dict() for tx in transactions if tx.action == "issue"]


def get_available_books() -> List[dict]:
    return [book.to_dict() for book in books if book.is_available()]


def issue_book(member_id: int, book_id: int) -> dict:
    member = next((m for m in members if m.member_id == member_id), None)
    if member is None:
        raise ValueError("Member not found.")

    book = next((b for b in books if b.book_id == book_id), None)
    if book is None:
        raise ValueError("Book not found.")

    if not book.is_available():
        raise ValueError("Book is not available for issue.")

    if not member.can_borrow():
        raise ValueError("Member has reached the maximum borrowed books.")

    if book_id in reserved_books and member_id not in [tx.member_id for tx in transactions if tx.book_id == book_id and tx.action == "reserve"]:
        raise ValueError("Book is reserved by another member.")

    book.issue()
    member.borrow_book(book_id)
    transaction = Transaction(member_id=member_id, book_id=book_id, action="issue")
    transaction.transaction_id = generate_transaction_id()
    transactions.append(transaction)
    return transaction.to_dict()


def return_book(member_id: int, book_id: int) -> dict:
    member = next((m for m in members if m.member_id == member_id), None)
    if member is None:
        raise ValueError("Member not found.")

    book = next((b for b in books if b.book_id == book_id), None)
    if book is None:
        raise ValueError("Book not found.")

    if book_id not in member.borrowed_books:
        raise ValueError("This book was not borrowed by the member.")

    book.return_copy()
    member.return_book(book_id)
    transaction = Transaction(member_id=member_id, book_id=book_id, action="return")
    transaction.transaction_id = generate_transaction_id()
    transactions.append(transaction)
    return transaction.to_dict()


def renew_book(member_id: int, book_id: int) -> dict:
    member = next((m for m in members if m.member_id == member_id), None)
    if member is None:
        raise ValueError("Member not found.")

    if book_id not in member.borrowed_books:
        raise ValueError("Book is not currently borrowed by this member.")

    transaction = Transaction(member_id=member_id, book_id=book_id, action="renew")
    transaction.transaction_id = generate_transaction_id()
    transactions.append(transaction)
    return transaction.to_dict()


def reserve_book(member_id: int, book_id: int) -> dict:
    member = next((m for m in members if m.member_id == member_id), None)
    if member is None:
        raise ValueError("Member not found.")

    book = next((b for b in books if b.book_id == book_id), None)
    if book is None:
        raise ValueError("Book not found.")

    if not book.is_available():
        raise ValueError("Cannot reserve an unavailable book.")

    if book_id in reserved_books:
        raise ValueError("Book is already reserved.")

    reserved_books.append(book_id)
    transaction = Transaction(member_id=member_id, book_id=book_id, action="reserve")
    transaction.transaction_id = generate_transaction_id()
    transactions.append(transaction)
    return transaction.to_dict()


def cancel_reservation(member_id: int, book_id: int) -> dict:
    if book_id not in reserved_books:
        raise ValueError("This book is not reserved.")

    transaction = Transaction(member_id=member_id, book_id=book_id, action="cancel_reservation")
    transaction.transaction_id = generate_transaction_id()
    transactions.append(transaction)
    reserved_books.remove(book_id)
    return transaction.to_dict()


def create_transaction(member_id: int, book_id: int, action: str) -> dict:
    action_name = action.strip().lower()
    if action_name == "issue":
        return issue_book(member_id=member_id, book_id=book_id)
    if action_name == "return":
        return return_book(member_id=member_id, book_id=book_id)
    if action_name == "renew":
        return renew_book(member_id=member_id, book_id=book_id)
    if action_name == "reserve":
        return reserve_book(member_id=member_id, book_id=book_id)
    if action_name == "cancel":
        return cancel_reservation(member_id=member_id, book_id=book_id)

    raise ValueError("Unsupported transaction action. Use issue, return, renew, reserve, or cancel.")


def most_borrowed_books() -> dict:
    borrow_counts = Counter(tx.book_id for tx in transactions if tx.action == "issue")
    return {"most_borrowed": borrow_counts.most_common(3)}
