"""Generator functions using yield."""

from typing import Generator, List


def countdown(start: int) -> Generator[int, None, None]:
    """Yield values from start down to 1."""
    while start > 0:
        yield start
        start -= 1


def fibonacci_numbers(limit: int) -> Generator[int, None, None]:
    """Yield the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b
