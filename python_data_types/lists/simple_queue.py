"""
Simple Queue implementation using Python list.
FIFO structure.
"""


class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to end of queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove item from front of queue."""
        if not self.items:
            return None
        return self.items.pop(0)

    def size(self):
        """Return queue size."""
        return len(self.items)

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0