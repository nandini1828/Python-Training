from __future__ import annotations

from list_methods.list_utils import average_values, chunk_list, find_duplicates


def run_list_demo() -> None:
    """Show simple list operations for beginners."""

    numbers = [3, 1, 2, 2, 4]
    numbers.append(5)
    numbers.sort()

    print("Original list:", [3, 1, 2, 2, 4])
    print("Sorted list:", numbers)
    print("Duplicates:", find_duplicates(numbers))
    print("Chunks:", chunk_list(numbers, 2))
    print("Average:", average_values(numbers))
