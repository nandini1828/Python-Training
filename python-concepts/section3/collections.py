"""
Section 3: Lists, Tuples & Sets
"""


class ListOperations:

    @staticmethod
    def append_item(data, item):
        data.append(item)
        return data

    @staticmethod
    def extend_items(data, items):
        data.extend(items)
        return data

    @staticmethod
    def insert_item(data, index, item):
        data.insert(index, item)
        return data

    @staticmethod
    def remove_item(data, item):
        data.remove(item)
        return data

    @staticmethod
    def pop_item(data, index=-1):
        return data.pop(index)

    @staticmethod
    def clear_items(data):
        data.clear()
        return data

    @staticmethod
    def find_index(data, item):
        return data.index(item)

    @staticmethod
    def count_occurrences(data, item):
        return data.count(item)

    @staticmethod
    def sort_items(data, reverse=False):
        data.sort(reverse=reverse)
        return data

    @staticmethod
    def reverse_items(data):
        data.reverse()
        return data

    @staticmethod
    def copy_items(data):
        return data.copy()


class TupleOperations:

    @staticmethod
    def count_occurrences(data, item):
        return data.count(item)

    @staticmethod
    def find_index(data, item):
        return data.index(item)


class SetOperations:

    @staticmethod
    def add_item(data, item):
        data.add(item)
        return data

    @staticmethod
    def remove_item(data, item):
        data.remove(item)
        return data

    @staticmethod
    def discard_item(data, item):
        data.discard(item)
        return data

    @staticmethod
    def pop_item(data):
        return data.pop()

    @staticmethod
    def clear_items(data):
        data.clear()
        return data

    @staticmethod
    def union(set_a, set_b):
        return set_a.union(set_b)

    @staticmethod
    def intersection(set_a, set_b):
        return set_a.intersection(set_b)

    @staticmethod
    def difference(set_a, set_b):
        return set_a.difference(set_b)

    @staticmethod
    def symmetric_difference(set_a, set_b):
        return set_a.symmetric_difference(set_b)

    @staticmethod
    def is_subset(set_a, set_b):
        return set_a.issubset(set_b)

    @staticmethod
    def is_superset(set_a, set_b):
        return set_a.issuperset(set_b)

    @staticmethod
    def is_disjoint(set_a, set_b):
        return set_a.isdisjoint(set_b)