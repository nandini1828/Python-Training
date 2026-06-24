from typing import Any


class SimpleQueue:

    def __init__(self) -> None:
        self.items: list[Any] = []

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:

        if not self.items:
            return None

        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)