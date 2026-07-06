"""
Examples demonstrating Python loop foundations.

This module introduces Python's looping constructs and common iteration
patterns used in day-to-day programming.

Topics covered:
- for loops
- while loops
- Iterating over strings
- Lists
- Tuples
- Sets
- Dictionaries
- range()
- Basic aggregations

Author: Python Training
"""

from __future__ import annotations

from typing import Any


def iterate_list(items: list[Any]) -> list[Any]:
    """
    Iterate over a list.

    Args:
        items:
            Input list.

    Returns:
        Copy of the input list.
    """
    result: list[Any] = []

    for item in items:
        result.append(item)

    return result


def iterate_tuple(items: tuple[Any, ...]) -> list[Any]:
    """
    Iterate over a tuple.

    Args:
        items:
            Input tuple.

    Returns:
        List containing tuple elements.
    """
    result: list[Any] = []

    for item in items:
        result.append(item)

    return result


def iterate_set(items: set[Any]) -> list[Any]:
    """
    Iterate over a set.

    Args:
        items:
            Input set.

    Returns:
        List containing set elements.

    Note:
        Sets are unordered.
    """
    result: list[Any] = []

    for item in items:
        result.append(item)

    return result


def iterate_string(text: str) -> list[str]:
    """
    Iterate through characters of a string.

    Args:
        text:
            Input string.

    Returns:
        List of characters.
    """
    characters: list[str] = []

    for character in text:
        characters.append(character)

    return characters


def iterate_dictionary(
    data: dict[str, Any],
) -> list[tuple[str, Any]]:
    """
    Iterate through dictionary key-value pairs.

    Args:
        data:
            Input dictionary.

    Returns:
        List of key-value tuples.
    """
    result: list[tuple[str, Any]] = []

    for key, value in data.items():
        result.append((key, value))

    return result


def generate_range(
    start: int,
    stop: int,
    step: int = 1,
) -> list[int]:
    """
    Generate a list using range().

    Args:
        start:
            Starting value.

        stop:
            Ending value (exclusive).

        step:
            Step size.

    Returns:
        List generated using range().
    """
    numbers: list[int] = []

    for value in range(start, stop, step):
        numbers.append(value)

    return numbers


def sum_numbers(numbers: list[int]) -> int:
    """
    Calculate the sum of numbers.

    Args:
        numbers:
            Integer list.

    Returns:
        Sum of all numbers.
    """
    total = 0

    for number in numbers:
        total += number

    return total


def product_numbers(numbers: list[int]) -> int:
    """
    Calculate the product of numbers.

    Args:
        numbers:
            Integer list.

    Returns:
        Product of numbers.
    """
    product = 1

    for number in numbers:
        product *= number

    return product


def count_characters(text: str) -> int:
    """
    Count characters without using len().

    Args:
        text:
            Input string.

    Returns:
        Character count.
    """
    count = 0

    for _ in text:
        count += 1

    return count


def count_occurrences(
    values: list[Any],
    target: Any,
) -> int:
    """
    Count occurrences of a value.

    Args:
        values:
            Input list.

        target:
            Target value.

    Returns:
        Number of occurrences.
    """
    count = 0

    for value in values:
        if value == target:
            count += 1

    return count


def square_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Square every number.

    Args:
        numbers:
            Integer list.

    Returns:
        Squared numbers.
    """
    result: list[int] = []

    for number in numbers:
        result.append(number * number)

    return result


def filter_even_numbers(
    numbers: list[int],
) -> list[int]:
    """
    Return only even numbers.

    Args:
        numbers:
            Integer list.

    Returns:
        Even numbers.
    """
    result: list[int] = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def reverse_string(text: str) -> str:
    """
    Reverse a string using iteration.

    Args:
        text:
            Input string.

    Returns:
        Reversed string.
    """
    result = ""

    for character in text:
        result = character + result

    return result
def factorial(number: int) -> int:
    """
    Calculate the factorial of a number using a for loop.

    Args:
        number:
            Non-negative integer.

    Returns:
        Factorial of the given number.

    Raises:
        ValueError:
            If number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def multiplication_table(number: int) -> list[str]:
    """
    Generate a multiplication table.

    Args:
        number:
            Input number.

    Returns:
        Multiplication table from 1 to 10.
    """
    table: list[str] = []

    for multiplier in range(1, 11):
        table.append(
            f"{number} x {multiplier} = {number * multiplier}"
        )

    return table


def nested_loop_grid(rows: int, columns: int) -> list[list[str]]:
    """
    Create a grid using nested loops.

    Args:
        rows:
            Number of rows.

        columns:
            Number of columns.

    Returns:
        Two-dimensional grid.
    """
    grid: list[list[str]] = []

    for row in range(rows):
        current_row: list[str] = []

        for column in range(columns):
            current_row.append(f"({row},{column})")

        grid.append(current_row)

    return grid


def find_maximum(numbers: list[int]) -> int:
    """
    Find the largest number.

    Args:
        numbers:
            List of integers.

    Returns:
        Largest value.

    Raises:
        ValueError:
            If list is empty.
    """
    if not numbers:
        raise ValueError("numbers cannot be empty.")

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def find_minimum(numbers: list[int]) -> int:
    """
    Find the smallest number.

    Args:
        numbers:
            List of integers.

    Returns:
        Smallest value.

    Raises:
        ValueError:
            If list is empty.
    """
    if not numbers:
        raise ValueError("numbers cannot be empty.")

    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


def search_element(
    values: list[Any],
    target: Any,
) -> bool:
    """
    Search for an element.

    Args:
        values:
            Input list.

        target:
            Value to search.

    Returns:
        True if found, otherwise False.
    """
    for value in values:
        if value == target:
            return True

    return False


def countdown(start: int) -> list[int]:
    """
    Countdown using a while loop.

    Args:
        start:
            Starting number.

    Returns:
        Countdown sequence.
    """
    result: list[int] = []

    current = start

    while current >= 0:
        result.append(current)
        current -= 1

    return result


def fibonacci(limit: int) -> list[int]:
    """
    Generate Fibonacci numbers.

    Args:
        limit:
            Number of terms.

    Returns:
        Fibonacci sequence.

    Raises:
        ValueError:
            If limit is negative.
    """
    if limit < 0:
        raise ValueError("limit cannot be negative.")

    if limit == 0:
        return []

    if limit == 1:
        return [0]

    sequence = [0, 1]

    while len(sequence) < limit:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def while_sum(limit: int) -> int:
    """
    Sum numbers using a while loop.

    Args:
        limit:
            Upper limit (inclusive).

    Returns:
        Sum of numbers from 1 to limit.
    """
    total = 0
    current = 1

    while current <= limit:
        total += current
        current += 1

    return total


def repeat_text(
    text: str,
    times: int,
) -> list[str]:
    """
    Repeat text using a while loop.

    Args:
        text:
            Text to repeat.

        times:
            Number of repetitions.

    Returns:
        List containing repeated text.
    """
    result: list[str] = []

    count = 0

    while count < times:
        result.append(text)
        count += 1

    return result


__all__ = [
    "iterate_list",
    "iterate_tuple",
    "iterate_set",
    "iterate_string",
    "iterate_dictionary",
    "generate_range",
    "sum_numbers",
    "product_numbers",
    "count_characters",
    "count_occurrences",
    "square_numbers",
    "filter_even_numbers",
    "reverse_string",
    "factorial",
    "multiplication_table",
    "nested_loop_grid",
    "find_maximum",
    "find_minimum",
    "search_element",
    "countdown",
    "fibonacci",
    "while_sum",
    "repeat_text",
]