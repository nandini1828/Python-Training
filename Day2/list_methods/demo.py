from __future__ import annotations

from list_methods.list_utils import (
    add_destination,
    add_multiple_destinations,
    average_values,
    chunk_list,
    clear_list,
    copy_list,
    count_items,
    find_duplicates,
    insert_destination,
    remove_destination,
    remove_last_destination,
    reverse_destinations,
    sort_destinations,
)


def run_list_demo() -> None:
    """Show simple list operations for beginners."""

    destinations = ["Paris", "London"]
    add_destination(destinations, "Rome")
    add_multiple_destinations(destinations, ["Berlin", "Tokyo"])
    insert_destination(destinations, 1, "Oslo")

    print("List after adding:", destinations)
    print("Removed last city:", remove_last_destination(destinations))
    print("List after removing last:", destinations)
    remove_destination(destinations, "Oslo")
    reverse_destinations(destinations)
    print("List after reversing:", destinations)
    sort_destinations(destinations)
    print("List after sorting:", destinations)
    print("Copied list:", copy_list(destinations))
    print("Count of Paris:", count_items(destinations, "Paris"))
    clear_list(destinations)
    print("List after clearing:", destinations)

    numbers = [3, 1, 2, 2, 4]
    print("Duplicates:", find_duplicates(numbers))
    print("Chunks:", chunk_list(numbers, 2))
    print("Average:", average_values(numbers))
