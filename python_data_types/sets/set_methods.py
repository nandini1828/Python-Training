"""
Basic set operations module.
"""


def add_item(s, item):
    s.add(item)
    return s


def remove_item(s, item):
    if item in s:
        s.remove(item)
    return s


def union_sets(a, b):
    return a.union(b)


def intersection_sets(a, b):
    return a.intersection(b)


def difference_sets(a, b):
    return a.difference(b)