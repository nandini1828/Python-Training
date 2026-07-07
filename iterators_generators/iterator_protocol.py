"""
iterator_protocol.py

Topic:
    - The iterator protocol using __iter__() and __next__()

Real World Application:
    Walking through a stream of inventory events without loading everything at once
"""


class IteratorExample:
    """A simple iterator that yields values from a list one at a time."""

    def __init__(self, values):
        self._values = values
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value


def run() -> None:
    """Run the iterator protocol example."""
    items = IteratorExample([10, 20, 30])
    print("\n--- Iterator Protocol ---")
    print("  Iterating with __iter__ and __next__:")
    for value in items:
        print(f"    - {value}")


if __name__ == "__main__":
    run()
