"""
Main demo for the Python Iteration Helpers Mastery project.

This script imports and exercises helper modules
related to Python iteration helper functions.
"""

from iteration_helpers.range_helper import generate_range
from iteration_helpers.enumerate_helper import enumerate_items
from iteration_helpers.zip_helper import zip_items, zip_longest_items
from iteration_helpers.reverse_sort_helper import reverse_items, sort_numbers, sort_records_by_key
from iteration_helpers.any_all_helper import check_any, check_all


def main() -> None:
    """
    Runs demo operations for all iteration helper modules.
    """
    print("Python Iteration Helpers Mastery Demo")
    print("=" * 72)

    print("\n1. RANGE")
    print("   generate_range(1, 10, 2):", generate_range(1, 10, 2))

    print("\n2. ENUMERATE")
    print("   enumerate_items(['Python', 'Java', 'C']):", enumerate_items(["Python", "Java", "C"]))

    print("\n3. ZIP / ZIP_LONGEST")
    print(
        "   zip_items(['A', 'B'], [1, 2]):",
        zip_items(["A", "B"], [1, 2]),
    )
    print(
        "   zip_longest_items(['A', 'B', 'C'], [1, 2], 'Missing'):",
        zip_longest_items(["A", "B", "C"], [1, 2], "Missing"),
    )

    print("\n4. REVERSED / SORTED")
    print("   reverse_items([1, 2, 3, 4]):", reverse_items([1, 2, 3, 4]))
    print("   sort_numbers([5, 1, 4, 2]):", sort_numbers([5, 1, 4, 2]))

    records = [
        {"name": "Karthik", "age": 21},
        {"name": "Rahul", "age": 19},
        {"name": "Anil", "age": 23},
    ]
    print(
        "   sort_records_by_key(records, 'age'):",
        sort_records_by_key(records, "age"),
    )

    print("\n5. ANY / ALL")
    print("   check_any([False, False, True]):", check_any([False, False, True]))
    print("   check_all([True, True, True]):", check_all([True, True, True]))


if __name__ == "__main__":
    main()