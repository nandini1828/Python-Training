"""
generator_expressions.py

Topic:
    - Generator expressions for memory-efficient single-line generation

Real World Application:
    Processing large datasets without materializing all values at once
"""

from typing import Iterable


def generator_expression_example(data: Iterable[int]):
    """Return a generator expression that squares each value."""
    return (value * value for value in data)


def run() -> None:
    """Run the generator expression example."""
    values = [1, 2, 3, 4]
    squares = generator_expression_example(values)
    print("\n--- Generator Expressions ---")
    print("  Squares from a generator expression:")
    for value in squares:
        print(f"    - {value}")


if __name__ == "__main__":
    run()
