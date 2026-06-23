"""
List Methods Module
Demonstrates core Python list operations.
"""


def append_item(lst, item):
    """Add item at end of list."""
    lst.append(item)
    return lst


def extend_list(lst, items):
    """Extend list with multiple items."""
    lst.extend(items)
    return lst


def insert_item(lst, index, item):
    """Insert item at a specific index."""
    lst.insert(index, item)
    return lst


def remove_item(lst, item):
    """Remove first occurrence of item."""
    lst.remove(item)
    return lst


def pop_item(lst, index=-1):
    """Pop item from list."""
    return lst.pop(index)


def sort_list(lst):
    """Sort list in ascending order."""
    lst.sort()
    return lst


def reverse_list(lst):
    """Reverse the list."""
    lst.reverse()
    return lst