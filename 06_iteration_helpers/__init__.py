"""
iteration_helpers package.

This package demonstrates Python's built-in iteration helper functions
that make looping more expressive, readable, and efficient.

Topics covered:

- range()
- enumerate()
- zip()
- itertools.zip_longest()
- reversed()
- sorted()
- any()
- all()

Author: Python Training
"""

from .range_examples import (
    even_numbers,
    generate_numbers,
    multiplication_table,
    odd_numbers,
    reverse_range,
)

from .enumerate_examples import (
    enumerate_dictionary_keys,
    enumerate_list,
    enumerate_string,
    indexed_students,
)

from .zip_examples import (
    combine_employee_records,
    create_dictionary,
    unzip_pairs,
    zip_lists,
    zip_longest_lists,
)

from .reversed_sorted import (
    reverse_list,
    reverse_string,
    sort_by_length,
    sort_numbers,
    sort_strings_case_insensitive,
)

from .any_all import (
    all_even,
    all_positive,
    any_even,
    any_negative,
    contains_admin,
)

__all__ = [
    "generate_numbers",
    "even_numbers",
    "odd_numbers",
    "reverse_range",
    "multiplication_table",
    "enumerate_list",
    "enumerate_string",
    "indexed_students",
    "enumerate_dictionary_keys",
    "zip_lists",
    "zip_longest_lists",
    "combine_employee_records",
    "create_dictionary",
    "unzip_pairs",
    "reverse_list",
    "reverse_string",
    "sort_numbers",
    "sort_by_length",
    "sort_strings_case_insensitive",
    "any_even",
    "all_even",
    "any_negative",
    "all_positive",
    "contains_admin",
]