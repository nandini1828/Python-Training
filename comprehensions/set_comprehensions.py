"""
set_comprehensions.py

Topic:
    - Set comprehensions for compact unique value creation

Real World Application:
    Building a unique collection of product labels
"""

from typing import List


def set_comprehension_example(strings: List[str] | None = None) -> set[str]:
    """Create a set of lowercase strings from the supplied input."""
    if strings is None:
        strings = ["Laptop", "Mouse", "Laptop", "Keyboard", "mouse"]
    return {value.lower() for value in strings}


def run() -> None:
    """Run the set comprehension example."""
    values = ["Laptop", "Mouse", "Laptop", "Keyboard", "mouse"]
    lowered = set_comprehension_example(values)
    print("\n--- Set Comprehensions ---")
    print(f"  Original values: {values}")
    print(f"  Lowercase unique values: {lowered}")


if __name__ == "__main__":
    run()
