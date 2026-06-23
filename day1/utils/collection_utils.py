from collections import deque


class CollectionUtility:

    @staticmethod
    def merge_tags(
        tags_a,
        tags_b
    ):
        set_a = {
            tag.lower()
            for tag in tags_a
        }

        set_b = {
            tag.lower()
            for tag in tags_b
        }

        return {
            "all_tags": sorted(
                set_a | set_b
            ),
            "common_tags": sorted(
                set_a & set_b
            ),
            "unique_tags": sorted(
                set_a - set_b
            )
        }


class SimpleQueue:

    def __init__(self):
        self.items = deque()

    def enqueue(
        self,
        item
    ):
        self.items.append(item)

    def dequeue(self):

        if self.items:
            return self.items.popleft()

        return None

    def size(self):
        return len(self.items)