"""
Practical demonstrations of list iteration helpers.
"""

from .utils import (
    enumerate_list,
    filter_positive,
    find_index,
    flatten_list,
    iterate_list,
    list_summary,
    sum_items,
    unique_items,
    uppercase_items,
)


def main():
    print("\n===== List Iteration Demo =====")
    data = [1, -2, 3, 4]
    print("Iterate:", iterate_list(data))
    print("Enumerate:", enumerate_list(["a", "b"]))
    print("Indexes:", find_index(["a", "b", "a"], "a"))
    print("Positive:", filter_positive(data))
    print("Uppercase:", uppercase_items(["one", "two"]))
    print("Sum:", sum_items([1, 2, 3]))
    print("Flatten:", flatten_list([[1, 2], [3]]))
    print("Unique:", unique_items([1, 1, 2]))
    print("Summary:", list_summary(data))


if __name__ == "__main__":
    main()
