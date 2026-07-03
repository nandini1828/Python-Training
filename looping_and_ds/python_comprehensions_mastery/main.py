"""
Main demo for the Python Comprehensions Mastery project.

This script imports and exercises comprehension-related modules
in a single runnable demonstration.
"""

from looping_and_ds.python_comprehensions_mastery.comprehensions.list_comprehensions import (
    get_even_numbers,
    get_squared_numbers,
)
from looping_and_ds.python_comprehensions_mastery.comprehensions.dictionary_comprehensions import (
    build_square_dictionary,
    map_words_to_lengths,
)
from looping_and_ds.python_comprehensions_mastery.comprehensions.set_comprehensions import (
    get_unique_lowercase_words,
    get_even_number_set,
)
from looping_and_ds.python_comprehensions_mastery.comprehensions.nested_comprehensions import (
    flatten_matrix,
    build_multiplication_grid,
)


def main() -> None:
    """
    Runs demo operations for all comprehension modules.
    """
    print("Python Comprehensions Mastery Demo")
    print("=" * 72)

    numbers = [1, 2, 3, 4, 5, 6]
    words = ["Python", "JAVA", "python", "C", "java"]
    matrix = [[1, 2], [3, 4], [5, 6]]

    print("\n1. LIST COMPREHENSIONS")
    print("   get_even_numbers(numbers):", get_even_numbers(numbers))
    print("   get_squared_numbers(numbers):", get_squared_numbers(numbers))

    print("\n2. DICTIONARY COMPREHENSIONS")
    print("   build_square_dictionary(5):", build_square_dictionary(5))
    print("   map_words_to_lengths(['apple', 'banana', 'kiwi']):", map_words_to_lengths(["apple", "banana", "kiwi"]))

    print("\n3. SET COMPREHENSIONS")
    print("   get_unique_lowercase_words(words):", get_unique_lowercase_words(words))
    print("   get_even_number_set(numbers):", get_even_number_set(numbers))

    print("\n4. NESTED COMPREHENSIONS")
    print("   flatten_matrix(matrix):", flatten_matrix(matrix))
    print("   build_multiplication_grid(3):", build_multiplication_grid(3))


if __name__ == "__main__":
    main()