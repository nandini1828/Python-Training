from __future__ import annotations

from tuple_methods.tuple_utils import (
    access_first_item,
    access_last_item,
    convert_to_list,
    count_items,
    count_occurrences,
    index_of,
    tuple_to_dict,
)


def run_tuple_demo() -> None:
    """Show simple tuple operations for beginners."""

    numbers = (1, 2, 2, 3)
    print("First item:", access_first_item(numbers))
    print("Last item:", access_last_item(numbers))
    print("Count of 2:", count_occurrences(numbers, 2))
    print("Count of 2 using count_items:", count_items(numbers, 2))
    print("Index of 3:", index_of(numbers, 3))
    print("Convert to list:", convert_to_list(numbers))
    print("Mapping:", tuple_to_dict(("name", "age"), ("Ada", 21)))
