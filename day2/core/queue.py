from collections import deque


class SimpleQueue:

    def __init__(self) -> None:
        self.items = deque()

    def enqueue(
        self,
        item
    ) -> None:
        self.items.append(item)

    def dequeue(self):

        if self.items:
            return self.items.popleft()

        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0