from collections.abc import Iterable, Iterator
from typing import Any


class CountDown:
    """An iterator that counts down from start to zero."""

    def __init__(self, start: int):
        if start < 0:
            raise ValueError("start must be zero or greater")

        self.current = start

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def is_iterable(value: Any) -> bool:
    """Return True when value can be passed to iter."""
    try:
        iter(value)
    except TypeError:
        return False

    return True


def get_first(iterator: Iterable[Any]) -> Any:
    """Return the first item from an iterable, or None when empty."""
    return next(iter(iterator), None)


def collect_iterator(iterator: Iterable[Any]) -> list[Any]:
    """Collect every remaining value from an iterable into a list."""
    return list(iterator)


def manual_next(iterator: Iterator[Any], default: Any = None) -> Any:
    """Call next with a default for exhausted iterators."""
    return next(iterator, default)
