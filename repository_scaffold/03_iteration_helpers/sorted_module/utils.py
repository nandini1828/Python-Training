"""
Utilities for sorted() operations
"""


def sort_list(data):
    return sorted(data)


def sort_descending(data):
    return sorted(data, reverse=True)


def sort_strings(data):
    return sorted(data)


def sort_by_length(data):
    return sorted(data, key=len)


def sort_dict_by_keys(data):
    return dict(sorted(data.items()))


def sort_dict_by_values(data):
    return dict(sorted(data.items(), key=lambda x: x[1]))


def sort_tuples_by_second(data):
    return sorted(data, key=lambda x: x[1])


def custom_sort_case_insensitive(data):
    return sorted(data, key=str.lower)


def sort_numbers_as_strings(data):
    return sorted(data, key=str)


def stable_sort_example(data):
    # demonstrates stability
    return sorted(data, key=lambda x: x[0])