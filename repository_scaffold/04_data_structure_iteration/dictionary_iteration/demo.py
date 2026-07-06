"""
Practical demonstrations of dictionary iteration helpers.
"""

from .utils import (
    count_frequency,
    dictionary_to_list,
    find_key,
    get_keys,
    get_values,
    invert_dictionary,
    iterate_dictionary,
    merge_dictionaries,
)


def main():
    print("\n===== Dictionary Iteration Demo =====")
    data = {"apple": 1, "banana": 2, "cherry": 3}
    print("Items:", iterate_dictionary(data))
    print("Keys:", get_keys(data))
    print("Values:", get_values(data))
    print("Merged:", merge_dictionaries(data, {"date": 4}))
    print("Pairs:", dictionary_to_list(data))
    print("Inverted:", invert_dictionary({"x": 10, "y": 20}))
    print("Frequency:", count_frequency(["x", "y", "x"]))
    print("Find key:", find_key(data, "banana"))


if __name__ == "__main__":
    main()
