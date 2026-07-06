"""
Utility functions demonstrating enumerate() usage
"""

def index_items(iterable):
    """
    Return list of (index, item)
    """
    return list(enumerate(iterable))


def index_with_start(iterable, start=1):
    """
    Enumerate with custom starting index
    """
    return list(enumerate(iterable, start=start))


def find_item_positions(iterable, target):
    """
    Return all positions of a target element
    """
    return [index for index, value in enumerate(iterable) if value == target]


def create_index_mapping(iterable):
    """
    Create dictionary mapping index -> value
    """
    return {index: value for index, value in enumerate(iterable)}


def filter_with_index(iterable):
    """
    Return elements present at even index positions
    """
    return [value for index, value in enumerate(iterable) if index % 2 == 0]


def enumerate_string(text):
    """
    Return list of indexed characters
    """
    return list(enumerate(text))


def compare_lists(list1, list2):
    """
    Compare two lists element-wise with index
    """
    result = []
    for index, (a, b) in enumerate(zip(list1, list2)):
        result.append((index, a, b, a == b))
    return result