from typing import Dict, List

from models.book import Book
from models.member import Member
from models.transaction import Transaction


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.transactions: List[Transaction] = []

    def __str__(self) -> str:
        return f"Library: {self.name}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "books": [book.to_dict() for book in self.books],
            "members": [member.to_dict() for member in self.members],
            "transactions": [transaction.to_dict() for transaction in self.transactions],
        }

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_member(self, member: Member) -> None:
        self.members.append(member)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
