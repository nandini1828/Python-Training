"""
Examples of Python for loops.
"""


def print_numbers(limit: int) -> list:
    """Return numbers from 1 to limit."""
    numbers = []

    for i in range(1, limit + 1):
        numbers.append(i)

    return numbers


def even_numbers(limit: int) -> list:
    """Return all even numbers."""
    evens = []

    for number in range(2, limit + 1, 2):
        evens.append(number)

    return evens


def square_numbers(limit: int) -> list:
    """Return squares of numbers."""
    squares = []

    for number in range(1, limit + 1):
        squares.append(number ** 2)

    return squares


def character_count(text: str) -> int:
    """Count characters using a for loop."""
    count = 0

    for _ in text:
        count += 1

    return count


def find_max(numbers: list[int]) -> int:
    """Return largest number."""

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


def multiplication_table(number: int) -> list[str]:
    """Return multiplication table."""

    table = []

    for i in range(1, 11):
        table.append(f"{number} x {i} = {number*i}")

    return table


def dictionary_keys(student: dict) -> list:
    """Return dictionary keys."""

    keys = []

    for key in student:
        keys.append(key)

    return keys


def zip_names_scores(names: list, scores: list) -> list:
    """Combine two lists."""

    result = []

    for name, score in zip(names, scores):
        result.append((name, score))

    return result


def enumerate_subjects(subjects: list) -> list:
    """Enumerate subjects."""

    result = []

    for index, subject in enumerate(subjects, start=1):
        result.append((index, subject))

    return result