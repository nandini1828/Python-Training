"""
Utility functions demonstrating zip() usage
"""

from itertools import zip_longest


def pair_lists(list1, list2):
    """
    Pair two lists element-wise
    """
    return list(zip(list1, list2))


def pair_multiple_lists(*lists):
    """
    Zip multiple iterables together
    """
    return list(zip(*lists))


def zip_with_index(iterable):
    """
    Combine enumerate and zip
    """
    return list(zip(range(len(iterable)), iterable))


def uneven_zip(list1, list2, fill_value=None):
    """
    Handle uneven lists using zip_longest
    """
    return list(zip_longest(list1, list2, fillvalue=fill_value))


def unzip_pairs(paired_list):
    """
    Unzip list of tuples into separate lists
    """
    if not paired_list:
        return [], []
    return map(list, zip(*paired_list))


def create_dict(keys, values):
    """
    Create dictionary using zip
    """
    return dict(zip(keys, values))


def compare_lists(list1, list2):
    """
    Compare two lists element-wise
    """
    return [(a, b, a == b) for a, b in zip(list1, list2)]


def sum_pairs(list1, list2):
    """
    Add corresponding elements of two lists
    """
    return [a + b for a, b in zip(list1, list2)]


def transpose_matrix(matrix):
    """
    Transpose a 2D matrix using zip
    """
    return [list(row) for row in zip(*matrix)]