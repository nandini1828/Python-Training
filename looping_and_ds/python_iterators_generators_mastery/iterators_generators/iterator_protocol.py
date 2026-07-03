"""
Iterator protocol utilities.
"""


class NumberIterator:
    """
    Custom iterator that yields numbers from 1 up to a limit.

    This class demonstrates how Python's iterator protocol works
    using __iter__() and __next__().
    """

    def __init__(self, limit: int) -> None:
        """
        Initializes the iterator.

        Parameters
        ----------
        limit : int
            Maximum number to iterate to.
        """
        self.limit = limit
        self.current = 1

    def __iter__(self) -> "NumberIterator":
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self) -> int:
        """
        Returns the next value in the sequence.

        Raises
        ------
        StopIteration
            When iteration is complete.
        """
        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1
        return value