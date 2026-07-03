"""
Main demo for the Python Iterators & Generators Mastery project.

This script imports and exercises iterator and generator-related modules
in a single runnable demonstration.
"""

from iterators_generators.iterator_protocol import NumberIterator
from iterators_generators.generators import generate_numbers, generate_even_numbers
from iterators_generators.generator_expressions import (
    build_square_generator,
    build_even_generator,
)


def main() -> None:
    """
    Runs demo operations for all iterator and generator modules.
    """
    print("Python Iterators & Generators Mastery Demo")
    print("=" * 72)

    print("\n1. ITERATOR PROTOCOL")
    iterator = NumberIterator(5)
    print("   list(NumberIterator(5)):", list(iterator))

    print("\n2. GENERATORS WITH YIELD")
    print("   list(generate_numbers(5)):", list(generate_numbers(5)))
    print("   list(generate_even_numbers(10)):", list(generate_even_numbers(10)))

    print("\n3. GENERATOR EXPRESSIONS")
    square_generator = build_square_generator([1, 2, 3, 4])
    print("   list(build_square_generator([1, 2, 3, 4])):", list(square_generator))

    even_generator = build_even_generator([1, 2, 3, 4, 5, 6])
    print("   list(build_even_generator([1, 2, 3, 4, 5, 6])):", list(even_generator))


if __name__ == "__main__":
    main()