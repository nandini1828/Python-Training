"""
list_comprehensions.py

Topic:
    - List comprehensions for compact iteration
    - Filtering and transforming values in one line

Real World Application:
    Filtering product IDs and transforming inventory data
"""

from typing import List


def list_comprehension_example(values: List[int] | None = None) -> list[int]:
    """Create a list of even numbers from the provided values."""
    if values is None:
        values = [1, 2, 3, 4, 5, 6]
    return [value for value in values if value % 2 == 0]


def run() -> None:
    """Run the list comprehension example."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    even_numbers = list_comprehension_example(numbers)
    print("\n--- List Comprehensions ---")
    print(f"  Original numbers: {numbers}")
    print(f"  Even numbers: {even_numbers}")


if __name__ == "__main__":
    run()
