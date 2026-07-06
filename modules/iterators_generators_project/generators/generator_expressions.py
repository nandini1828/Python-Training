"""Generator expressions for memory-friendly iteration."""

from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def square_numbers(values: Iterable[int]) -> Generator[int, None, None]:
    """Square each value lazily."""
    return (value * value for value in values)


def even_numbers(values: Iterable[int]) -> Generator[int, None, None]:
    """Yield even values lazily."""
    return (value for value in values if value % 2 == 0)
