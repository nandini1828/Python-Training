"""
Examples of Python while loops.
"""


def countdown(start: int) -> list[int]:
    """Return countdown from start to 1."""
    numbers = []

    while start > 0:
        numbers.append(start)
        start -= 1

    return numbers


def factorial(number: int) -> int:
    """Calculate factorial."""

    result = 1

    while number > 1:
        result *= number
        number -= 1

    return result


def reverse_string(text: str) -> str:
    """Reverse a string."""

    index = len(text) - 1
    reversed_text = ""

    while index >= 0:
        reversed_text += text[index]
        index -= 1

    return reversed_text


def sum_numbers(limit: int) -> int:
    """Return sum from 1 to limit."""

    total = 0
    current = 1

    while current <= limit:
        total += current
        current += 1

    return total


def count_vowels(text: str) -> int:
    """Count vowels."""

    vowels = "aeiouAEIOU"
    index = 0
    count = 0

    while index < len(text):

        if text[index] in vowels:
            count += 1

        index += 1

    return count


def power(base: int, exponent: int) -> int:
    """Calculate power without **."""

    answer = 1

    while exponent > 0:
        answer *= base
        exponent -= 1

    return answer


def find_smallest(numbers: list[int]) -> int:
    """Return smallest number."""

    smallest = numbers[0]
    index = 1

    while index < len(numbers):

        if numbers[index] < smallest:
            smallest = numbers[index]

        index += 1

    return smallest