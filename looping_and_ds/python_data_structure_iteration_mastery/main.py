"""
Main demo for the Python Data Structure Iteration & Safety project.

This script imports and exercises modules related to
list iteration, dictionary iteration, key protection,
list modification safety, and set iteration.
"""

from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.list_iteration import (
    get_items_by_index,
    get_list_slices,
    iterate_list_items,
)
from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.list_modification_trap import (
    remove_even_numbers_unsafely,
    remove_even_numbers_safely,
)
from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.dictionary_iteration import (
    get_dictionary_keys,
    get_dictionary_values,
    get_dictionary_items,
)
from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.dictionary_key_protection import (
    safe_get_value,
    count_words_with_defaultdict,
)
from looping_and_ds.python_data_structure_iteration_mastery.data_structure_iteration.set_iteration import (
    check_membership_in_list,
    check_membership_in_set,
    iterate_set_items,
)


def main() -> None:
    """
    Runs demo operations for all data structure iteration modules.
    """
    print("Python Data Structure Iteration & Safety Demo")
    print("=" * 72)

    numbers = [10, 20, 30, 40, 50]
    sample_dict = {"name": "Karthik", "age": 21, "city": "Hyderabad"}
    words = ["python", "java", "python", "c", "java", "python"]
    values = [1, 2, 3, 4, 5, 6]
    set_values = {"Python", "Java", "C++"}

    print("\n1. LIST ITERATION")
    print("   get_items_by_index(numbers):", get_items_by_index(numbers))
    print("   get_list_slices(numbers):", get_list_slices(numbers))
    print("   iterate_list_items(numbers):", iterate_list_items(numbers))

    print("\n2. LIST MODIFICATION TRAP")
    print(
        "   remove_even_numbers_unsafely(values):",
        remove_even_numbers_unsafely(values.copy()),
    )
    print(
        "   remove_even_numbers_safely(values):",
        remove_even_numbers_safely(values),
    )

    print("\n3. DICTIONARY ITERATION")
    print("   get_dictionary_keys(sample_dict):", get_dictionary_keys(sample_dict))
    print("   get_dictionary_values(sample_dict):", get_dictionary_values(sample_dict))
    print("   get_dictionary_items(sample_dict):", get_dictionary_items(sample_dict))

    print("\n4. DICTIONARY KEY PROTECTION")
    print("   safe_get_value(sample_dict, 'name'):", safe_get_value(sample_dict, "name"))
    print("   safe_get_value(sample_dict, 'salary', 0):", safe_get_value(sample_dict, "salary", 0))
    print(
        "   count_words_with_defaultdict(words):",
        count_words_with_defaultdict(words),
    )

    print("\n5. SET ITERATION & MEMBERSHIP")
    print("   check_membership_in_list([1, 2, 3, 4], 3):", check_membership_in_list([1, 2, 3, 4], 3))
    print("   check_membership_in_set({1, 2, 3, 4}, 3):", check_membership_in_set({1, 2, 3, 4}, 3))
    print("   iterate_set_items(set_values):", iterate_set_items(set_values))


if __name__ == "__main__":
    main()