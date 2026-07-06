"""
Demonstration script for the iteration_helpers package.

Run:

    python -m iteration_helpers.demo

Author: Python Training
"""

from __future__ import annotations

from any_all import (
    all_even,
    all_files_exist,
    all_positive,
    all_scores_valid,
    all_strings_non_empty,
    any_empty_string,
    any_even,
    any_failed,
    any_negative,
    contains_admin,
)

from enumerate_examples import (
    csv_rows,
    employee_report,
    enumerate_dictionary_items,
    enumerate_dictionary_keys,
    enumerate_dictionary_values,
    enumerate_list,
    enumerate_list_start,
    enumerate_string,
    enumerate_words,
    find_occurrences,
    indexed_students,
    inventory_report,
    ranked_scores,
)

from range_examples import (
    batch_numbers,
    countdown,
    divisible_by,
    employee_ids,
    even_numbers,
    generate_numbers,
    generate_range,
    generate_range_step,
    multiplication_table,
    odd_numbers,
    reverse_range,
    squares_using_range,
    sum_using_range,
)

from reversed_sorted import (
    reverse_list,
    reverse_string,
    sort_by_length,
    sort_dictionary_keys,
    sort_dictionary_values,
    sort_numbers,
    sort_records_by_age,
    sort_records_by_name,
    sort_strings_case_insensitive,
)

from utils import (
    print_banner,
    print_result,
)

from zip_examples import (
    combine_employee_records,
    compare_lists,
    create_dictionary,
    merge_student_marks,
    parallel_sum,
    transpose_matrix,
    unzip_pairs,
    zip_lists,
    zip_longest_lists,
    zip_three_lists,
)


def demonstrate_range() -> None:
    """Demonstrate range() examples."""

    print_banner("range()")

    print_result(
        "Generate Numbers",
        generate_numbers(5),
    )

    print_result(
        "Generate Range",
        generate_range(5, 10),
    )

    print_result(
        "Generate Range Step",
        generate_range_step(0, 20, 5),
    )

    print_result(
        "Reverse Range",
        reverse_range(5),
    )

    print_result(
        "Even Numbers",
        even_numbers(20),
    )

    print_result(
        "Odd Numbers",
        odd_numbers(20),
    )

    print_result(
        "Multiplication Table",
        multiplication_table(5),
    )

    print_result(
        "Sum Using Range",
        sum_using_range(10),
    )

    print_result(
        "Squares",
        squares_using_range(10),
    )

    print_result(
        "Countdown",
        countdown(5),
    )

    print_result(
        "Divisible By 3",
        divisible_by(20, 3),
    )

    print_result(
        "Employee IDs",
        employee_ids(1001, 5),
    )

    print_result(
        "Batch Numbers",
        batch_numbers(100, 20),
    )


def demonstrate_enumerate() -> None:
    """Demonstrate enumerate()."""

    print_banner("enumerate()")

    print_result(
        "Enumerate List",
        enumerate_list(["A", "B", "C"]),
    )

    print_result(
        "Custom Start",
        enumerate_list_start(
            ["Python", "Django"],
            1,
        ),
    )

    print_result(
        "Enumerate String",
        enumerate_string("Python"),
    )

    print_result(
        "Indexed Students",
        indexed_students(
            ["Alice", "Bob", "Charlie"],
        ),
    )

    sample = {
        "name": "Alice",
        "age": 25,
    }

    print_result(
        "Dictionary Keys",
        enumerate_dictionary_keys(sample),
    )

    print_result(
        "Dictionary Values",
        enumerate_dictionary_values(sample),
    )

    print_result(
        "Dictionary Items",
        enumerate_dictionary_items(sample),
    )

    print_result(
        "Employee Report",
        employee_report(
            ["Alice", "Bob"],
        ),
    )

    print_result(
        "Ranked Scores",
        ranked_scores([95, 88, 76]),
    )

    print_result(
        "CSV Rows",
        csv_rows(
            [
                ["Alice", "95"],
                ["Bob", "88"],
            ],
        ),
    )

    print_result(
        "Occurrences",
        find_occurrences(
            [1, 2, 2, 3, 2],
            2,
        ),
    )

    print_result(
        "Words",
        enumerate_words(
            "Python is awesome",
        ),
    )

    print_result(
        "Inventory",
        inventory_report(
            {
                "Keyboard": 5,
                "Mouse": 10,
            },
        ),
    )
def demonstrate_zip() -> None:
    """Demonstrate zip() examples."""

    print_banner("zip()")

    print_result(
        "Zip Lists",
        zip_lists(
            ["Alice", "Bob"],
            [25, 30],
        ),
    )

    print_result(
        "Zip Three Lists",
        zip_three_lists(
            ["Alice", "Bob"],
            [25, 30],
            ["HR", "IT"],
        ),
    )

    print_result(
        "Zip Longest",
        zip_longest_lists(
            ["A", "B", "C"],
            [1, 2],
            fill_value="-",
        ),
    )

    print_result(
        "Create Dictionary",
        create_dictionary(
            ["name", "age"],
            ["Alice", 25],
        ),
    )

    pairs = [
        ("Python", 95),
        ("Django", 90),
    ]

    print_result(
        "Unzip",
        unzip_pairs(pairs),
    )

    print_result(
        "Employee Records",
        combine_employee_records(
            ["Alice", "Bob"],
            ["HR", "IT"],
        ),
    )

    print_result(
        "Student Marks",
        merge_student_marks(
            ["Alice", "Bob"],
            [95, 88],
        ),
    )

    print_result(
        "Parallel Sum",
        parallel_sum(
            [1, 2, 3],
            [4, 5, 6],
        ),
    )

    print_result(
        "Compare Lists",
        compare_lists(
            [1, 2, 3],
            [1, 0, 3],
        ),
    )

    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    print_result(
        "Transpose Matrix",
        transpose_matrix(matrix),
    )


def demonstrate_reversed_sorted() -> None:
    """Demonstrate reversed() and sorted()."""

    print_banner("reversed() / sorted()")

    print_result(
        "Reverse List",
        reverse_list([1, 2, 3, 4]),
    )

    print_result(
        "Reverse String",
        reverse_string("Python"),
    )

    print_result(
        "Sort Numbers",
        sort_numbers([5, 2, 8, 1]),
    )

    print_result(
        "Sort Descending",
        sort_numbers(
            [5, 2, 8, 1],
            descending=True,
        ),
    )

    print_result(
        "Case-Insensitive Sort",
        sort_strings_case_insensitive(
            ["banana", "Apple", "cherry"],
        ),
    )

    print_result(
        "Sort by Length",
        sort_by_length(
            ["Python", "C", "Java"],
        ),
    )

    sample = {
        "z": 10,
        "a": 30,
        "m": 20,
    }

    print_result(
        "Dictionary Keys",
        sort_dictionary_keys(sample),
    )

    print_result(
        "Dictionary Values",
        sort_dictionary_values(sample),
    )

    employees = [
        {"name": "Bob", "age": 32},
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 29},
    ]

    print_result(
        "Sort by Age",
        sort_records_by_age(employees),
    )

    print_result(
        "Sort by Name",
        sort_records_by_name(employees),
    )


def demonstrate_any_all() -> None:
    """Demonstrate any() and all()."""

    print_banner("any() / all()")

    print_result(
        "Any Even",
        any_even([1, 3, 4]),
    )

    print_result(
        "All Even",
        all_even([2, 4, 6]),
    )

    print_result(
        "Any Negative",
        any_negative([5, -1, 8]),
    )

    print_result(
        "All Positive",
        all_positive([1, 2, 3]),
    )

    print_result(
        "Contains Admin",
        contains_admin(
            ["guest", "Admin", "user"],
        ),
    )

    print_result(
        "All Non Empty",
        all_strings_non_empty(
            ["Python", "Django"],
        ),
    )

    print_result(
        "Any Empty",
        any_empty_string(
            ["Python", "", "FastAPI"],
        ),
    )

    print_result(
        "Scores Valid",
        all_scores_valid(
            [95, 82, 70],
        ),
    )

    print_result(
        "Any Failed",
        any_failed(
            [90, 25, 75],
        ),
    )

    print_result(
        "Files Exist",
        all_files_exist(
            [True, True, False],
        ),
    )


def main() -> None:
    """Run every demonstration."""

    print_banner("Iteration Helpers")

    demonstrate_range()

    demonstrate_enumerate()

    demonstrate_zip()

    demonstrate_reversed_sorted()

    demonstrate_any_all()

    print_banner("Demo Completed")


if __name__ == "__main__":
    main()    