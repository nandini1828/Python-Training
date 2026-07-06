"""
Practical demonstrations of set iteration helpers.
"""

from .utils import (
    add_item,
    difference_sets,
    intersect_sets,
    is_subset,
    iterate_set,
    pop_item,
    set_from_list,
    union_sets,
)


def main():
    print("\n===== Set Iteration Demo =====")
    a = {1, 2, 3}
    b = {2, 3, 4}
    print("Iterate:", iterate_set(a))
    print("Union:", union_sets(a, b))
    print("Intersection:", intersect_sets(a, b))
    print("Difference:", difference_sets(a, b))
    print("Subset:", is_subset({1, 2}, a))
    print("Add:", add_item(a, 5))
    print("Pop:", pop_item(a))
    print("From list:", set_from_list([1, 1, 2]))


if __name__ == "__main__":
    main()
