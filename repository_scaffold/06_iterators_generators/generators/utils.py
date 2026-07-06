from typing import Iterable, Iterator


def natural_numbers(limit: int) -> Iterator[int]:
    """Yield natural numbers from 0 up to, but not including, limit."""
    value = 0
    while value < limit:
        yield value
        value += 1


def fibonacci(limit: int) -> Iterator[int]:
    """Yield the first limit Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def filtered_numbers(values: Iterable[int], threshold: int) -> Iterator[int]:
    """Yield numbers greater than threshold."""
    for number in values:
        if number > threshold:
            yield number


def file_lines(lines: Iterable[str]) -> Iterator[str]:
    """Yield stripped lines from an iterable of strings."""
    for line in lines:
        yield line.rstrip("\n")


def batched(values: Iterable[int], size: int) -> Iterator[list[int]]:
    """Yield values in fixed-size batches."""
    if size <= 0:
        raise ValueError("size must be greater than zero")

    batch: list[int] = []
    for value in values:
        batch.append(value)
        if len(batch) == size:
            yield batch
            batch = []

    if batch:
        yield batch
