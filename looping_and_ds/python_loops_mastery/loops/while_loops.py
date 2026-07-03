"""
while loop examples.
"""


def count_with_while(limit: int) -> list[int]:
    """
    Counts from 1 to limit using a while loop.
    """
    numbers = []
    counter = 1

    while counter <= limit:
        numbers.append(counter)
        counter += 1

    return numbers


def sum_until_limit(limit: int) -> int:
    """
    Returns the sum of numbers from 1 to limit using while loop.
    """
    total = 0
    counter = 1

    while counter <= limit:
        total += counter
        counter += 1

    return total