from datetime import date
from typing import Dict


class Transaction:
    def __init__(self, member_id: int, book_id: int, action: str):
        self.member_id = member_id
        self.book_id = book_id
        self.action = action
        self.transaction_id = None
        self.date = date.today()

    def __str__(self) -> str:
        return f"Transaction({self.transaction_id}): {self.action} book {self.book_id} for member {self.member_id}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, object]:
        return {
            "transaction_id": self.transaction_id,
            "member_id": self.member_id,
            "book_id": self.book_id,
            "action": self.action,
            "date": self.date.isoformat(),
        }
