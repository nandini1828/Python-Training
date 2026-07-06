"""Examples showing the iterator protocol."""

from typing import Iterator, List, TypeVar

T = TypeVar("T")


class IterableCounter:
    """A simple iterable that implements __iter__."""

    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __iter__(self) -> Iterator[int]:
        return self._generate_values()

    def _generate_values(self) -> Iterator[int]:
        for value in range(self.limit):
            yield value


def next_value(values: List[T]) -> T:
    """Return the first value from an iterator created from the list."""
    iterator = iter(values)
    return next(iterator)
