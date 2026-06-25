from __future__ import annotations

from dictionary_methods.dictionary_utils import (
    add_item,
    clear_mapping,
    filter_by_value,
    get_items,
    get_keys,
    get_values,
    has_key,
    invert_mapping,
    merge_dictionaries,
    remove_item,
    update_dictionary,
)


def run_dictionary_demo() -> None:
    """Show simple dictionary operations for beginners."""

    student = {"name": "Ada", "age": 21, "city": "London"}
    print("Name:", student.get("name"))
    print("Keys:", get_keys(student))
    print("Values:", get_values(student))
    print("Items:", get_items(student))

    add_item(student, "country", "UK")
    update_dictionary(student, {"job": "Engineer"})
    print("Updated student:", student)
    print("Has key 'age':", has_key(student, "age"))
    remove_item(student, "city")
    print("After removing city:", student)
    clear_mapping(student)
    print("After clearing dictionary:", student)

    merged = merge_dictionaries({"name": "Ada"}, {"city": "London"})
    inverted = invert_mapping({"a": 1, "b": 1, "c": 2})
    filtered = filter_by_value({"x": 10, "y": 20, "z": 30}, lambda value: value >= 20)
    print("Merged:", merged)
    print("Inverted:", inverted)
    print("Filtered:", filtered)
