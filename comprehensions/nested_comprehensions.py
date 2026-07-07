"""
nested_comprehensions.py

Topic:
    - Nested comprehensions for flattening and grid creation

Real World Application:
    Flattening tabular inventory data and generating grids
"""

from typing import List


def nested_comprehension_example() -> tuple[list[int], list[list[int]]]:
    """Flatten a 2D list and create a 3x3 multiplication grid."""
    matrix = [[1, 2, 3], [4, 5, 6]]
    flattened = [value for row in matrix for value in row]
    grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]
    return flattened, grid


def run() -> None:
    """Run the nested comprehension example."""
    flattened, grid = nested_comprehension_example()
    print("\n--- Nested Comprehensions ---")
    print(f"  Flattened matrix: {flattened}")
    print(f"  Grid: {grid}")


if __name__ == "__main__":
    run()
