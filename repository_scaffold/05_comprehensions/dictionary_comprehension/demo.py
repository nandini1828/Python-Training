"""
Practical demonstrations of dictionary comprehension helpers.
"""

from .utils import (
    dict_from_lists,
    filter_dict,
    invert_unique,
    normalize_scores,
    square_dict,
    uppercase_keys,
    value_length_dict,
)


def main():
    print("\n===== Dictionary Comprehension Demo =====")
    print("Squares:", square_dict([1, 2, 3]))
    print("From lists:", dict_from_lists(["a", "b"], [1, 2]))
    print("Upper keys:", uppercase_keys({"a": 1, "b": 2}))
    print("Lengths:", value_length_dict(["one", "two"]))
    print("Filtered:", filter_dict({"a": 1, "b": 3, "c": 2}, 2))
    print("Inverted:", invert_unique({"low": 1, "high": 10}))
    print("Normalized:", normalize_scores({"Asha": 42, "Ravi": 36}, 50))


if __name__ == "__main__":
    main()
