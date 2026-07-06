"""
Practical demonstrations of safe list modification helpers.
"""

from .utils import (
    append_item,
    clear_list,
    extend_list,
    insert_item,
    pop_item,
    remove_item,
    replace_item,
    sorted_copy,
    unique_list,
)


def main():
    print("\n===== List Modification Demo =====")
    data = [1, 2, 3]
    print("Append:", append_item(data, 4))
    print("Remove:", remove_item(data, 2))
    print("Insert:", insert_item(data, 1, 5))
    print("Pop:", pop_item(data))
    print("Extend:", extend_list(data, [4, 5]))
    print("Replace:", replace_item(data, 2, 20))
    print("Clear:", clear_list(data))
    print("Sorted:", sorted_copy([3, 1, 2]))
    print("Unique:", unique_list([1, 1, 2]))


if __name__ == "__main__":
    main()
