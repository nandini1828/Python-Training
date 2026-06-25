from __future__ import annotations

from introspection.introspection_utils import extract_documentation, inspect_object


class Book:
    """A small class used to show introspection."""

    def __init__(self, title: str) -> None:
        self.title = title

    def read(self) -> str:
        return f"Reading {self.title}"


def run_introspection_demo() -> None:
    """Show simple introspection examples for beginners."""

    book = Book("Python Basics")
    summary = inspect_object(book)
    documentation = extract_documentation(Book.read)

    print("Object kind:", summary["kind"])
    print("Attributes:", summary["attributes"])
    print("Methods:", summary["methods"])
    print("Docstring:", documentation["docstring"])
