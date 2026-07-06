"""
iterator_examples.py

Demonstrates Python Iterator Protocol.
"""


class NumberIterator:
    """
    Custom iterator using
    __iter__() and __next__().
    """

    def __init__(self, limit: int):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


class IteratorExamples:
    """Utility class demonstrating iterators."""

    @staticmethod
    def create_iterator(data: list[int]):
        """Creates an iterator."""

        return iter(data)

    @staticmethod
    def next_element(data: list[int]) -> int:
        """Returns first element using next()."""

        iterator = iter(data)

        return next(iterator)

    @staticmethod
    def iterate_manually(data: list[int]) -> list[int]:
        """Iterates using next()."""

        iterator = iter(data)

        result = []

        while True:

            try:
                result.append(next(iterator))

            except StopIteration:
                break

        return result

    @staticmethod
    def custom_iterator(limit: int) -> list[int]:
        """Uses custom iterator."""

        return list(NumberIterator(limit))