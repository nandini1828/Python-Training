"""
Exercise Solutions - Section 3
"""


class SimpleQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):

        if not self.items:
            return None

        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


def merge_tags(tags_a, tags_b):
    """
    Exercise 3.2
    """

    set_a = {tag.lower() for tag in tags_a}
    set_b = {tag.lower() for tag in tags_b}

    all_tags = sorted(set_a | set_b)

    common_tags = sorted(set_a & set_b)

    unique_to_a = sorted(set_a - set_b)

    return {
        "all_unique_tags": all_tags,
        "common_tags": common_tags,
        "unique_to_a": unique_to_a
    }