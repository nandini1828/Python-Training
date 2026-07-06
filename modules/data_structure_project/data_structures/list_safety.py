"""Safe ways to remove items from a list while iterating."""

from typing import List


def remove_even_numbers_bug(values: List[int]) -> List[int]:
    """Demonstrate the list-modification trap by removing while looping."""
    result = values.copy()
    for index in range(len(result)):
        if index < len(result) and result[index] % 2 == 0:
            del result[index]
    return result


def remove_even_numbers_safe(values: List[int]) -> List[int]:
    """Remove even numbers safely by iterating over a copy."""
    return [value for value in values if value % 2 != 0]
