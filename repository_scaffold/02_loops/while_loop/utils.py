"""
utils.py

Reusable utility functions demonstrating Python while loops.
"""


def count_up(limit: int) -> list[int]:
    """
    Return numbers from 1 to limit.
    """
    numbers = []
    current = 1

    while current <= limit:
        numbers.append(current)
        current += 1

    return numbers


def count_down(start: int) -> list[int]:
    """
    Return numbers from start down to 1.
    """
    numbers = []

    while start >= 1:
        numbers.append(start)
        start -= 1

    return numbers


def sum_numbers(numbers: list[int | float]) -> int | float:
    """
    Return the sum of all numbers.
    """
    index = 0
    total = 0

    while index < len(numbers):
        total += numbers[index]
        index += 1

    return total


def factorial(number: int) -> int:
    """
    Return the factorial of a number.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1

    while number > 1:
        result *= number
        number -= 1

    return result


def multiplication_table(number: int) -> list[str]:
    """
    Return the multiplication table of a number.
    """
    table = []
    value = 1

    while value <= 10:
        table.append(f"{number} x {value} = {number * value}")
        value += 1

    return table


def countdown(seconds: int) -> list[int]:
    """
    Return a countdown sequence.
    """
    values = []

    while seconds > 0:
        values.append(seconds)
        seconds -= 1

    return values


def find_first_even(numbers: list[int]):
    """
    Return the first even number.
    """
    index = 0

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            return numbers[index]

        index += 1

    return None


def reverse_string(text: str) -> str:
    """
    Reverse a string using a while loop.
    """
    reversed_text = ""
    index = len(text) - 1

    while index >= 0:
        reversed_text += text[index]
        index -= 1

    return reversed_text


def count_digits(number: int) -> int:
    """
    Return the number of digits in an integer.
    """
    if number == 0:
        return 1

    number = abs(number)
    count = 0

    while number > 0:
        count += 1
        number //= 10

    return count


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.
    """
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True