"""
Demonstration script for the iteration_safety package.

Run:

    python -m iteration_safety.demo

Author: Python Training
"""

from __future__ import annotations

from .copy_vs_reference import (
    copy_using_list,
    copy_using_method,
    copy_using_slice,
    create_deep_copy,
    create_shallow_copy,
    demonstrate_reference,
    object_equality,
    object_identity,
)

from .mutation_patterns import (
    filter_positive_numbers,
    increment_values,
    merge_lists,
    normalize_strings,
    remove_duplicates,
    replace_negative_numbers,
    safe_update_dictionary,
)

from .safe_dictionary_iteration import (
    filter_positive_values,
    lowercase_values,
    remove_empty_values,
    remove_keys,
    snapshot_items,
    snapshot_keys,
    uppercase_keys,
)

from .safe_list_iteration import (
    filter_even_numbers,
    remove_duplicates as list_remove_duplicates,
    remove_empty_strings,
    remove_even_in_place,
    remove_negative_numbers,
    replace_negative_with_zero,
    snapshot_iteration,
)

from .safe_set_iteration import (
    common_values,
    filter_even_set,
    positive_numbers,
    remove_small_values,
    safe_remove,
    snapshot_iteration as set_snapshot_iteration,
    unique_values,
    uppercase_words,
)

from .utils import (
    print_banner,
    print_result,
)


def demonstrate_safe_list_iteration() -> None:
    """Demonstrate safe list iteration."""

    print_banner("Safe List Iteration")

    numbers = [5, -3, 10, -1, 8, 3]

    print_result(
        "Original",
        numbers,
    )

    print_result(
        "Remove Negatives",
        remove_negative_numbers(numbers),
    )

    print_result(
        "Even Numbers",
        filter_even_numbers(numbers),
    )

    print_result(
        "Remove Duplicates",
        list_remove_duplicates(
            [1, 2, 2, 3, 4, 4]
        ),
    )

    print_result(
        "Remove Even",
        remove_even_in_place(
            [1, 2, 3, 4, 5, 6]
        ),
    )

    print_result(
        "Replace Negative",
        replace_negative_with_zero(numbers),
    )

    print_result(
        "Remove Empty",
        remove_empty_strings(
            [
                "Python",
                "",
                "Django",
            ]
        ),
    )

    print_result(
        "Snapshot",
        snapshot_iteration(numbers),
    )


def demonstrate_safe_dictionary_iteration() -> None:
    """Demonstrate dictionary iteration."""

    print_banner(
        "Safe Dictionary Iteration"
    )

    data = {
        "name": "Alice",
        "city": "",
        "age": "25",
    }

    print_result(
        "Original",
        data,
    )

    print_result(
        "Remove Empty",
        remove_empty_values(data),
    )

    print_result(
        "Remove Keys",
        remove_keys(
            {
                "A": 1,
                "B": 2,
                "C": 3,
            },
            ["B"],
        ),
    )

    print_result(
        "Uppercase Keys",
        uppercase_keys(
            {
                "name": "Alice",
            }
        ),
    )

    print_result(
        "Lowercase Values",
        lowercase_values(
            {
                "LANGUAGE": "PYTHON",
            }
        ),
    )

    print_result(
        "Positive Values",
        filter_positive_values(
            {
                "A": 10,
                "B": -5,
                "C": 20,
            }
        ),
    )

    print_result(
        "Snapshot Keys",
        snapshot_keys(
            {
                "A": 1,
                "B": 2,
            }
        ),
    )

    print_result(
        "Snapshot Items",
        snapshot_items(
            {
                "A": 1,
                "B": 2,
            }
        ),
    )


def demonstrate_safe_set_iteration() -> None:
    """Demonstrate safe set iteration."""

    print_banner("Safe Set Iteration")

    values = {1, 2, 3, 4, 5, 6}

    print_result(
        "Original",
        values,
    )

    print_result(
        "Even Set",
        filter_even_set(values),
    )

    print_result(
        "Minimum >= 4",
        remove_small_values(
            values,
            4,
        ),
    )

    print_result(
        "Uppercase",
        uppercase_words(
            {
                "python",
                "django",
            }
        ),
    )

    print_result(
        "Safe Remove",
        safe_remove(
            values,
            3,
        ),
    )

    print_result(
        "Snapshot",
        set_snapshot_iteration(values),
    )

    print_result(
        "Common Values",
        common_values(
            {1, 2, 3},
            {2, 3, 4},
        ),
    )

    print_result(
        "Unique Values",
        unique_values(
            {1, 2, 3},
            {2},
        ),
    )
from .defensive_iteration import (
    immutable_filter,
    process_if_valid,
    safe_batch_processing,
    safe_dictionary_iteration,
    safe_set_iteration,
    safe_snapshot_iteration,
    validate_numbers,
)


def demonstrate_copy_vs_reference() -> None:
    """Demonstrate copy vs reference."""

    print_banner("Copy vs Reference")

    original = [1, 2, 3]

    original_list, reference = demonstrate_reference(original)

    print_result(
        "Reference Assignment",
        reference,
    )

    print_result(
        "Shallow Copy",
        create_shallow_copy(original),
    )

    print_result(
        "Deep Copy",
        create_deep_copy(original),
    )

    print_result(
        "Slice Copy",
        copy_using_slice(original),
    )

    print_result(
        "list() Copy",
        copy_using_list(original),
    )

    print_result(
        "copy() Method",
        copy_using_method(original),
    )

    print_result(
        "Identity",
        object_identity(
            original,
            reference,
        ),
    )

    print_result(
        "Equality",
        object_equality(
            original,
            reference,
        ),
    )


def demonstrate_mutation_patterns() -> None:
    """Demonstrate mutation patterns."""

    print_banner("Mutation Patterns")

    numbers = [-5, 10, 15, -3, 20]

    print_result(
        "Positive Numbers",
        filter_positive_numbers(numbers),
    )

    print_result(
        "Replace Negatives",
        replace_negative_numbers(numbers),
    )

    print_result(
        "Increment Values",
        increment_values([1, 2, 3]),
    )

    print_result(
        "Normalize Strings",
        normalize_strings(
            [
                " Python ",
                " DJANGO ",
                " FastAPI ",
            ]
        ),
    )

    print_result(
        "Merge Lists",
        merge_lists(
            [1, 2],
            [3, 4],
        ),
    )

    print_result(
        "Remove Duplicates",
        remove_duplicates(
            [1, 2, 2, 3, 4, 4],
        ),
    )

    print_result(
        "Safe Dictionary Update",
        safe_update_dictionary(
            {"A": 1},
            {"B": 2},
        ),
    )


def demonstrate_defensive_iteration() -> None:
    """Demonstrate defensive iteration."""

    print_banner("Defensive Iteration")

    values = [10, 20, 30, 40, 50]

    print_result(
        "Snapshot",
        safe_snapshot_iteration(values),
    )

    print_result(
        "Batch Processing",
        safe_batch_processing(
            values,
            2,
        ),
    )

    print_result(
        "Validation",
        validate_numbers(values),
    )

    print_result(
        "Immutable Filter",
        immutable_filter(
            [-2, 3, 5, -1, 8],
        ),
    )

    print_result(
        "Processed Values",
        process_if_valid(
            [1, 2, 3],
        ),
    )

    print_result(
        "Dictionary Snapshot",
        safe_dictionary_iteration(
            {
                "A": 1,
                "B": 2,
            },
        ),
    )

    print_result(
        "Set Snapshot",
        safe_set_iteration(
            {
                1,
                2,
                3,
            },
        ),
    )


def main() -> None:
    """Run all demonstrations."""

    print_banner("Iteration Safety")

    demonstrate_safe_list_iteration()

    demonstrate_safe_dictionary_iteration()

    demonstrate_safe_set_iteration()

    demonstrate_copy_vs_reference()

    demonstrate_mutation_patterns()

    demonstrate_defensive_iteration()

    print_banner("Demo Completed")


if __name__ == "__main__":
    main()    