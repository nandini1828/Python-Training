"""
SimpleQueue exercise implemented using a Python list internally.
"""
from __future__ import annotations

from typing import Any, List


class SimpleQueue:
    """
    A minimal FIFO queue.

    Methods:
        enqueue: Add an item to the queue.
        dequeue: Remove and return the oldest item.
        size: Return current queue size.
    """

    def __init__(self) -> None:
        self._items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        """Add `item` to the end of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Remove and return the item at the front of the queue."""
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def size(self) -> int:
        """Return the number of items currently in the queue."""
        return len(self._items)
