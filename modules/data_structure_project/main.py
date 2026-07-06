"""Entry point for the data structure project."""

from data_structures.dictionary_ops import collect_items, collect_keys, collect_values
from data_structures.dictionary_safety import count_words, safe_lookup
from data_structures.list_ops import first_and_last, iterate_with_index, middle_slice
from data_structures.list_safety import remove_even_numbers_bug, remove_even_numbers_safe
from data_structures.set_ops import contains_value, create_unique_collection


def main() -> None:
    print("first and last:", first_and_last([10, 20, 30]))
    print("middle slice:", middle_slice([1, 2, 3, 4, 5], 1, 4))
    print("indexed loop:", iterate_with_index(["a", "b", "c"]))
    print("buggy removal:", remove_even_numbers_bug([1, 2, 2, 3]))
    print("safe removal:", remove_even_numbers_safe([1, 2, 2, 3]))
    print("dictionary keys:", collect_keys({"a": 1, "b": 2}))
    print("dictionary values:", collect_values({"a": 1, "b": 2}))
    print("dictionary items:", collect_items({"a": 1, "b": 2}))
    print("safe lookup:", safe_lookup({"name": "Ada"}, "age", "unknown"))
    print("word counts:", count_words(["one", "two", "one"]))
    print("set contains:", contains_value(create_unique_collection([1, 2, 3]), 2))


if __name__ == "__main__":
    main()
