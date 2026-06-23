class SimpleQueue:
    """A simple FIFO queue implemented using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if not self.items:
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def size(self):
        """Return the current number of items in the queue."""
        return len(self.items)
