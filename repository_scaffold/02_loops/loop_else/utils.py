"""
utils.py

Utility functions demonstrating loop with else usage.
"""


def find_prime(n: int) -> bool:
    """
    Check if a number is prime using for-else.

    else runs only if loop is NOT broken.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def search_element_with_else(numbers: list[int], target: int) -> int:
    """
    Search element using for-else.

    Returns index if found, else -1.
    """
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    else:
        return -1


def find_first_even_with_else(numbers: list[int]) -> int | None:
    """
    Find first even number.

    Uses loop-else to return None if not found.
    """
    for num in numbers:
        if num % 2 == 0:
            return num
    else:
        return None


def validate_all_positive(numbers: list[int]) -> bool:
    """
    Check if all numbers are positive.

    Returns False immediately if any negative found,
    else returns True using loop-else.
    """
    for num in numbers:
        if num <= 0:
            return False
    else:
        return True


def find_divisor(n: int) -> int | None:
    """
    Return first divisor of n (other than 1).

    If no divisor found, return None (means prime).
    """
    if n < 2:
        return None

    for i in range(2, n):
        if n % i == 0:
            return i
    else:
        return None


def process_until_zero(numbers: list[int]) -> list[int]:
    """
    Process numbers until zero appears.

    If zero appears → break
    else → process full list

    Demonstrates break vs else behavior.
    """
    result = []

    for num in numbers:
        if num == 0:
            break
        result.append(num)
    else:
        # runs only if no break happened
        result.append("completed")

    return result


def find_with_while_else(numbers: list[int], target: int) -> int:
    """
    Demonstrate while-else.

    Return index if found, else -1.
    """
    i = 0

    while i < len(numbers):
        if numbers[i] == target:
            return i
        i += 1
    else:
        return -1