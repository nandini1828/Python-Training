"""A custom iterator class implementing the iterator protocol."""

from typing import Iterator


class CountDownIterator:
    """Iterate backwards from a starting number to zero."""

    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
