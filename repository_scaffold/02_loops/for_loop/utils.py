"""
utils.py

Reusable utility functions demonstrating Python for loops.
"""

from typing import Any


def print_list(items: list[Any]) -> None:
    """Print each item in a list."""
    for item in items:
        print(item)


def sum_numbers(numbers: list[int | float]) -> int | float:
    """Return the sum of all numbers."""
    total = 0

    for number in numbers:
        total += number

    return total


def find_max(numbers: list[int | float]) -> int | float:
    """Return the largest number."""
    if not numbers:
        raise ValueError("List cannot be empty.")

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def find_min(numbers: list[int | float]) -> int | float:
    """Return the smallest number."""
    if not numbers:
        raise ValueError("List cannot be empty.")

    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


def count_vowels(text: str) -> int:
    """Count the vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count


def multiplication_table(number: int) -> list[str]:
    """Return the multiplication table of a number."""
    table = []

    for value in range(1, 11):
        table.append(f"{number} x {value} = {number * value}")

    return table


def reverse_string(text: str) -> str:
    """Reverse a string using a for loop."""
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


def square_numbers(numbers: list[int]) -> list[int]:
    """Return the square of every number."""
    squares = []

    for number in numbers:
        squares.append(number ** 2)

    return squares


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Return all even numbers."""
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def create_student_dictionary(names: list[str], marks: list[int]) -> dict[str, int]:
    """Create a dictionary from names and marks."""
    students = {}

    for name, mark in zip(names, marks):
        students[name] = mark

    return students