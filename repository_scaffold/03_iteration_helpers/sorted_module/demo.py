from .utils import *

def run_demo():
    print("=== sorted() DEMO ===\n")

    print("1. Sort list:")
    print(sort_list([5, 2, 9, 1]))

    print("\n2. Sort descending:")
    print(sort_descending([5, 2, 9, 1]))

    print("\n3. Sort strings:")
    print(sort_strings(["banana", "apple", "cherry"]))

    print("\n4. Sort by length:")
    print(sort_by_length(["a", "abcd", "abc"]))

    print("\n5. Sort dict by keys:")
    print(sort_dict_by_keys({"b": 2, "a": 1, "c": 3}))

    print("\n6. Sort dict by values:")
    print(sort_dict_by_values({"b": 2, "a": 1, "c": 3}))

    print("\n7. Sort tuples by second value:")
    print(sort_tuples_by_second([(1, 3), (2, 1), (4, 2)]))

    print("\n8. Case insensitive sort:")
    print(custom_sort_case_insensitive(["Banana", "apple", "Cherry"]))

    print("\n9. Sort numbers as strings:")
    print(sort_numbers_as_strings([10, 2, 1]))

    print("\n10. Stable sort example:")
    data = [(1, "b"), (1, "a"), (2, "c")]
    print(stable_sort_example(data))


if __name__ == "__main__":
    run_demo()