from typing import Dict


class Member:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.member_id = None
        self.borrowed_books = []

    def __str__(self) -> str:
        return f"Member({self.member_id}): {self.name}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Member):
            return False
        return self.email.lower() == other.email.lower()

    def __len__(self) -> int:
        return len(self.borrowed_books)

    def to_dict(self) -> Dict[str, object]:
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": list(self.borrowed_books),
        }

    def can_borrow(self) -> bool:
        return len(self.borrowed_books) < 3

    def borrow_book(self, book_id: int) -> None:
        if not self.can_borrow():
            raise ValueError("Member cannot borrow more than 3 books.")
        self.borrowed_books.append(book_id)

    def return_book(self, book_id: int) -> None:
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
