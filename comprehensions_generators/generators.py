"""
Examples demonstrating Python generators.

Topics covered:

- yield
- Lazy evaluation
- Infinite generators
- File generators
- Fibonacci generator
- Countdown generator

Author: Python Training
"""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path


def countdown(
    start: int,
) -> Generator[int, None, None]:
    """
    Generate a countdown.

    Args:
        start:
            Starting number.

    Yields:
        Countdown values.

    Raises:
        ValueError:
            If start is negative.
    """
    if start < 0:
        raise ValueError(
            "start cannot be negative."
        )

    current = start

    while current >= 0:
        yield current
        current -= 1


def fibonacci(
    count: int,
) -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers.

    Args:
        count:
            Number of values.

    Yields:
        Fibonacci sequence.

    Raises:
        ValueError:
            If count is negative.
    """
    if count < 0:
        raise ValueError(
            "count cannot be negative."
        )

    previous = 0
    current = 1

    for _ in range(count):
        yield previous
        previous, current = (
            current,
            previous + current,
        )


def square_generator(
    numbers: list[int],
) -> Generator[int, None, None]:
    """
    Yield squares lazily.

    Args:
        numbers:
            Input numbers.

    Yields:
        Squared values.
    """
    for number in numbers:
        yield number**2


def read_lines(
    file_path: str,
) -> Generator[str, None, None]:
    """
    Lazily read a text file.

    Args:
        file_path:
            Path to the file.

    Yields:
        Lines without trailing newlines.
    """
    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:

        for line in file:
            yield line.rstrip("\n")


def infinite_counter(
    start: int = 0,
) -> Generator[int, None, None]:
    """
    Generate an infinite sequence.

    Args:
        start:
            Starting value.

    Yields:
        Consecutive integers.
    """
    current = start

    while True:
        yield current
        current += 1


def reverse_generator(
    values: list[int],
) -> Generator[int, None, None]:
    """
    Yield values in reverse order.

    Args:
        values:
            Input values.

    Yields:
        Reversed values.
    """
    for value in reversed(values):
        yield value


def alphabet_generator() -> Generator[str, None, None]:
    """
    Yield uppercase alphabet letters.

    Yields:
        Letters A through Z.
    """
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        yield letter


def even_numbers(
    limit: int,
) -> Generator[int, None, None]:
    """
    Yield even numbers.

    Args:
        limit:
            Upper limit.

    Yields:
        Even numbers.
    """
    for number in range(limit):
        if number % 2 == 0:
            yield number


def odd_numbers(
    limit: int,
) -> Generator[int, None, None]:
    """
    Yield odd numbers.

    Args:
        limit:
            Upper limit.

    Yields:
        Odd numbers.
    """
    for number in range(limit):
        if number % 2 != 0:
            yield number

def batch_generator(
    values: list[int],
    batch_size: int,
) -> Generator[list[int], None, None]:
    """
    Yield values in fixed-size batches.

    Args:
        values:
            Input values.

        batch_size:
            Number of items per batch.

    Yields:
        Lists containing batched values.

    Raises:
        ValueError:
            If batch_size is not positive.
    """
    if batch_size <= 0:
        raise ValueError(
            "batch_size must be greater than zero."
        )

    for index in range(0, len(values), batch_size):
        yield values[index:index + batch_size]


def chunk_generator(
    values: list[int],
    chunk_size: int,
) -> Generator[list[int], None, None]:
    """
    Yield chunks from a list.

    Args:
        values:
            Input values.

        chunk_size:
            Chunk size.

    Yields:
        Chunks of values.
    """
    yield from batch_generator(
        values,
        chunk_size,
    )


def filter_even_numbers(
    values: list[int],
) -> Generator[int, None, None]:
    """
    Yield only even numbers.

    Args:
        values:
            Input values.

    Yields:
        Even numbers.
    """
    for value in values:
        if value % 2 == 0:
            yield value


def running_total(
    values: list[int],
) -> Generator[int, None, None]:
    """
    Yield running totals.

    Example:
        Input:
            [10, 20, 30]

        Output:
            10
            30
            60

    Args:
        values:
            Input values.

    Yields:
        Running totals.
    """
    total = 0

    for value in values:
        total += value
        yield total


def consume_generator(
    generator: Generator[int, None, None],
) -> list[int]:
    """
    Consume a generator.

    Args:
        generator:
            Input generator.

    Returns:
        List of generated values.
    """
    return list(generator)


def generator_expression(
    values: list[int],
) -> Generator[int, None, None]:
    """
    Demonstrate a generator expression.

    Args:
        values:
            Input values.

    Returns:
        Generator expression.
    """
    return (
        value**2
        for value in values
    )


def pipeline(
    values: list[int],
) -> Generator[int, None, None]:
    """
    Demonstrate a simple generator pipeline.

    Pipeline:
        values
            ↓
        square
            ↓
        keep even

    Args:
        values:
            Input values.

    Yields:
        Even squares.
    """
    squares = (
        value**2
        for value in values
    )

    yield from (
        square
        for square in squares
        if square % 2 == 0
    )


def employee_name_stream(
    employees: list[dict[str, str]],
) -> Generator[str, None, None]:
    """
    Stream employee names.

    Args:
        employees:
            Employee records.

    Yields:
        Employee names.
    """
    for employee in employees:
        yield employee["name"]


def lazy_range(
    start: int,
    stop: int,
) -> Generator[int, None, None]:
    """
    Lazily generate numbers.

    Args:
        start:
            Starting value.

        stop:
            Ending value.

    Yields:
        Consecutive numbers.
    """
    current = start

    while current < stop:
        yield current
        current += 1


__all__ = [
    "countdown",
    "fibonacci",
    "square_generator",
    "read_lines",
    "infinite_counter",
    "reverse_generator",
    "alphabet_generator",
    "even_numbers",
    "odd_numbers",
    "batch_generator",
    "chunk_generator",
    "filter_even_numbers",
    "running_total",
    "consume_generator",
    "generator_expression",
    "pipeline",
    "employee_name_stream",
    "lazy_range",
]