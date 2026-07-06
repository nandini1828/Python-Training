"""
Unit tests for generators.py

Run:

    pytest tests/test_generators.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from comprehensions_generators.generators import (
    alphabet_generator,
    batch_generator,
    chunk_generator,
    consume_generator,
    countdown,
    employee_name_stream,
    even_numbers,
    fibonacci,
    filter_even_numbers,
    generator_expression,
    infinite_counter,
    lazy_range,
    odd_numbers,
    pipeline,
    read_lines,
    reverse_generator,
    running_total,
    square_generator,
)


def test_countdown() -> None:
    """Countdown generator."""
    assert list(countdown(3)) == [
        3,
        2,
        1,
        0,
    ]


def test_countdown_negative() -> None:
    """Negative countdown."""
    with pytest.raises(ValueError):
        list(countdown(-1))


def test_fibonacci() -> None:
    """Fibonacci sequence."""
    assert list(fibonacci(7)) == [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
    ]


def test_square_generator() -> None:
    """Square generator."""
    assert list(
        square_generator([1, 2, 3])
    ) == [
        1,
        4,
        9,
    ]


def test_reverse_generator() -> None:
    """Reverse generator."""
    assert list(
        reverse_generator([1, 2, 3])
    ) == [
        3,
        2,
        1,
    ]


def test_alphabet_generator() -> None:
    """Alphabet generator."""
    letters = list(alphabet_generator())

    assert len(letters) == 26
    assert letters[0] == "A"
    assert letters[-1] == "Z"


def test_even_numbers() -> None:
    """Even numbers."""
    assert list(even_numbers(10)) == [
        0,
        2,
        4,
        6,
        8,
    ]


def test_odd_numbers() -> None:
    """Odd numbers."""
    assert list(odd_numbers(10)) == [
        1,
        3,
        5,
        7,
        9,
    ]


def test_batch_generator() -> None:
    """Batch generation."""
    result = list(
        batch_generator(
            list(range(7)),
            3,
        )
    )

    assert result == [
        [0, 1, 2],
        [3, 4, 5],
        [6],
    ]


def test_batch_generator_invalid() -> None:
    """Invalid batch size."""
    with pytest.raises(ValueError):
        list(
            batch_generator(
                [1, 2],
                0,
            )
        )


def test_chunk_generator() -> None:
    """Chunk generator."""
    result = list(
        chunk_generator(
            [1, 2, 3, 4],
            2,
        )
    )

    assert result == [
        [1, 2],
        [3, 4],
    ]


def test_filter_even_numbers() -> None:
    """Even filter."""
    assert list(
        filter_even_numbers(
            [1, 2, 3, 4]
        )
    ) == [
        2,
        4,
    ]


def test_running_total() -> None:
    """Running totals."""
    assert list(
        running_total(
            [10, 20, 30]
        )
    ) == [
        10,
        30,
        60,
    ]


def test_consume_generator() -> None:
    """Consume generator."""
    generator = square_generator(
        [1, 2, 3]
    )

    assert consume_generator(generator) == [
        1,
        4,
        9,
    ]


def test_generator_expression() -> None:
    """Generator expression."""
    result = list(
        generator_expression(
            [1, 2, 3]
        )
    )

    assert result == [
        1,
        4,
        9,
    ]


def test_pipeline() -> None:
    """Pipeline."""
    assert list(
        pipeline(
            [1, 2, 3, 4]
        )
    ) == [
        4,
        16,
    ]


def test_employee_name_stream() -> None:
    """Employee names."""
    employees = [
        {"name": "Alice"},
        {"name": "Bob"},
    ]

    assert list(
        employee_name_stream(
            employees
        )
    ) == [
        "Alice",
        "Bob",
    ]


def test_lazy_range() -> None:
    """Lazy range."""
    assert list(
        lazy_range(3, 7)
    ) == [
        3,
        4,
        5,
        6,
    ]


def test_infinite_counter() -> None:
    """Infinite generator."""
    counter = infinite_counter()

    values = [
        next(counter)
        for _ in range(5)
    ]

    assert values == [
        0,
        1,
        2,
        3,
        4,
    ]


def test_read_lines(tmp_path) -> None:
    """File generator."""
    file_path = tmp_path / "sample.txt"

    file_path.write_text(
        "Python\nDjango\nFastAPI\n",
        encoding="utf-8",
    )

    assert list(
        read_lines(str(file_path))
    ) == [
        "Python",
        "Django",
        "FastAPI",
    ]