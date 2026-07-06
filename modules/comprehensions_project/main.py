"""Entry point for the comprehensions project."""

from comprehensions.dictionary_comprehension import square_mapping, vowel_count
from comprehensions.list_comprehension import even_numbers, uppercase_words
from comprehensions.nested_comprehension import flatten_matrix, make_grid
from comprehensions.set_comprehension import unique_lowercase_words


def main() -> None:
    print("even numbers:", even_numbers([1, 2, 3, 4, 5]))
    print("upper words:", uppercase_words(["apple", "banana"]))
    print("square mapping:", square_mapping(5))
    print("vowel count:", vowel_count("hello world"))
    print("unique lowercase words:", unique_lowercase_words(["Apple", "apple", "BANANA", "banana"]))
    print("flattened matrix:", flatten_matrix([[1, 2], [3, 4], [5]]))
    print("grid:", make_grid(2, 3))


if __name__ == "__main__":
    main()
