"""
Practical demonstrations of list comprehension helpers.
"""

from .utils import (
    combine_words,
    even_numbers,
    filter_short_words,
    indexed_words,
    nested_flatten,
    square_numbers,
    strings_to_chars,
    uppercase_words,
    words_lengths,
)


def main():
    print("\n===== List Comprehension Demo =====")
    print("Squares:", square_numbers([1, 2, 3]))
    print("Lengths:", words_lengths(["apple", "banana"]))
    print("Evens:", even_numbers([1, 2, 3, 4]))
    print("Uppercase:", uppercase_words(["a", "b"]))
    print("Flatten:", nested_flatten([[1, 2], [3]]))
    print("Pairs:", combine_words(["x"], ["y", "z"]))
    print("Filtered:", filter_short_words(["one", "three", "four"], 3))
    print("Chars:", strings_to_chars(["ab", "cd"]))
    print("Indexed:", indexed_words(["alpha", "beta"], start=1))


if __name__ == "__main__":
    main()
