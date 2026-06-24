from __future__ import annotations

from dictionary_methods.dictionary_utils import filter_by_value, invert_mapping, merge_dictionaries


def run_dictionary_demo() -> None:
    """Show simple dictionary operations for beginners."""

    student = {"name": "Ada", "age": 21, "city": "London"}
    print("Name:", student.get("name"))
    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))
    print("Items:", list(student.items()))

    merged = merge_dictionaries({"name": "Ada"}, {"city": "London"})
    inverted = invert_mapping({"a": 1, "b": 1, "c": 2})
    filtered = filter_by_value({"x": 10, "y": 20, "z": 30}, lambda value: value >= 20)
    print("Merged:", merged)
    print("Inverted:", inverted)
    print("Filtered:", filtered)
