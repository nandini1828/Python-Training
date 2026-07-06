"""
Practical demonstrations of generator expression helpers.
"""

from .utils import (
    char_generator,
    even_generator,
    running_total_generator,
    square_generator,
    word_lengths_generator,
)


def main():
    print("\n===== Generator Expressions Demo =====")
    print("Squares:", list(square_generator([1, 2, 3])))
    print("Evens:", list(even_generator([1, 2, 3, 4])))
    print("Chars:", list(char_generator(["ab", "cd"])))
    print("Lengths:", list(word_lengths_generator(["hello", "world"])))
    print("Running totals:", list(running_total_generator([2, 4, 6])))


if __name__ == "__main__":
    main()
