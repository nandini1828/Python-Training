"""
Practical demonstrations of set comprehension helpers.
"""

from .utils import (
    char_set,
    common_characters,
    even_numbers,
    filter_letters,
    square_set,
    unique_uppercase,
)


def main():
    print("\n===== Set Comprehension Demo =====")
    print("Uppercase:", unique_uppercase(["apple", "banana"]))
    print("Squares:", square_set([1, 2, 3]))
    print("Evens:", even_numbers([1, 2, 3, 4]))
    print("Chars:", char_set(["hi", "by"]))
    print("Filtered:", filter_letters(["one", "two", "three"]))
    print("Common chars:", common_characters("iteration", "generator"))


if __name__ == "__main__":
    main()
