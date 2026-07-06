"""Custom iterator examples."""

from __future__ import annotations


class CounterIterator:
    """Iterate over a sequence of numbers from zero upwards."""

    def __init__(self, limit: int) -> None:
        """Store the maximum number to produce."""
        self._limit = limit
        self._position = 0

    def __iter__(self) -> "CounterIterator":
        """Return the iterator instance."""
        return self

    def __next__(self) -> int:
        """Return the next value or raise StopIteration."""
        if self._position >= self._limit:
            raise StopIteration
        value = self._position
        self._position += 1
        return value
