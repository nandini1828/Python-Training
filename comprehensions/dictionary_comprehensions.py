"""
dictionary_comprehensions.py

Topic:
    - Dictionary comprehensions for compact key/value mapping

Real World Application:
    Turning numeric ranges into lookup tables
"""

from typing import Dict


def dictionary_comprehension_example(limit: int = 5) -> Dict[int, int]:
    """Create a mapping of numbers to their squares."""
    return {value: value**2 for value in range(limit)}


def run() -> None:
    """Run the dictionary comprehension example."""
    squares = dictionary_comprehension_example(5)
    print("\n--- Dictionary Comprehensions ---")
    print(f"  Squares: {squares}")


if __name__ == "__main__":
    run()
