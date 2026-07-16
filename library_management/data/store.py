from typing import List

from models.book import Book
from models.member import Member
from models.transaction import Transaction

books: List[Book] = []
members: List[Member] = []
transactions: List[Transaction] = []

reserved_books: List[int] = []
