"""
Practical demonstrations of safe dictionary key access helpers.
"""

from .utils import (
    clear_dictionary,
    filter_by_key,
    get_value_safe,
    key_exists,
    merge_with_override,
    remove_key_safely,
    set_default_value,
    update_dictionary,
)


def main():
    print("\n===== Dictionary Key Protection Demo =====")
    data = {"city": "Pune", "country": "India"}
    print("Safe value:", get_value_safe(data, "city"))
    print("Default value:", get_value_safe(data, "state", "Unknown"))
    print("Set default:", set_default_value(data, "state", "Maharashtra"))
    print("Updated:", update_dictionary(data, {"country": "Bharat"}))
    print("Merged:", merge_with_override(data, {"city": "Mumbai"}))
    print("Removed:", remove_key_safely(data, "country"))
    print("Exists:", key_exists(data, "city"))
    print("Filtered:", filter_by_key(data, ["city"]))
    print("Cleared:", clear_dictionary(data))


if __name__ == "__main__":
    main()
