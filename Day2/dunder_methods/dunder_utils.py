from __future__ import annotations


class DunderDemo:
    """Showcase common dunder methods for custom objects."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"DunderDemo(name={self.name!r}, age={self.age})"

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DunderDemo):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, DunderDemo):
            return NotImplemented
        return self.age < other.age
