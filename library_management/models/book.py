from typing import Dict


class Book:
    def __init__(self, title: str, author: str, category: str, isbn: str, total_stock: int):
        self.title = title
        self.author = author
        self.category = category
        self.isbn = isbn
        self.total_stock = total_stock
        self.available_stock = total_stock
        self.book_id = None

    def __str__(self) -> str:
        return f"Book({self.book_id}): {self.title} by {self.author}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn

    def __len__(self) -> int:
        return self.available_stock

    def __contains__(self, item: str) -> bool:
        return item.lower() in self.title.lower() or item.lower() in self.author.lower()

    def to_dict(self) -> Dict[str, object]:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "isbn": self.isbn,
            "total_stock": self.total_stock,
            "available_stock": self.available_stock,
        }

    def is_available(self) -> bool:
        return self.available_stock > 0

    def issue(self) -> None:
        if self.available_stock <= 0:
            raise ValueError("No copies available to issue.")
        self.available_stock -= 1

    def return_copy(self) -> None:
        if self.available_stock < self.total_stock:
            self.available_stock += 1


class AvailableBookIterator:
    def __init__(self, books: list["Book"]):
        self._books = books
        self._index = 0

    def __iter__(self) -> "AvailableBookIterator":
        return self

    def __next__(self) -> "Book":
        while self._index < len(self._books):
            current = self._books[self._index]
            self._index += 1
            if current.is_available():
                return current
        raise StopIteration
