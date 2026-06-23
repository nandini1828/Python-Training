class SimpleQueue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self._items:
            return self._items.pop(0)

        return None

    def size(self):
        return len(self._items)