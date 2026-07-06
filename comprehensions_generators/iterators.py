"""
Examples demonstrating Python's Iterator Protocol.

Topics covered:

- iter()
- next()
- __iter__()
- __next__()
- StopIteration
- Custom iterators

Author: Python Training
"""

from __future__ import annotations

from collections.abc import Iterator


class NumberIterator:
    """
    Iterator that produces numbers from 0 to limit.

    Example:
        iterator = NumberIterator(5)

        for value in iterator:
            print(value)
    """

    def __init__(
        self,
        limit: int,
    ) -> None:
        """
        Initialize the iterator.

        Args:
            limit:
                Upper limit (exclusive).

        Raises:
            ValueError:
                If limit is negative.
        """
        if limit < 0:
            raise ValueError(
                "limit cannot be negative."
            )

        self._limit = limit
        self._current = 0

    def __iter__(self) -> Iterator[int]:
        """
        Return the iterator object.

        Returns:
            Iterator instance.
        """
        self._current = 0
        return self

    def __next__(self) -> int:
        """
        Return the next value.

        Raises:
            StopIteration:
                When iteration finishes.
        """
        if self._current >= self._limit:
            raise StopIteration

        value = self._current
        self._current += 1

        return value


class CountdownIterator:
    """
    Countdown iterator.

    Example:

        CountdownIterator(5)

    Produces:

        5 4 3 2 1 0
    """

    def __init__(
        self,
        start: int,
    ) -> None:
        """
        Initialize countdown.

        Args:
            start:
                Starting value.

        Raises:
            ValueError:
                If start is negative.
        """
        if start < 0:
            raise ValueError(
                "start cannot be negative."
            )

        self._start = start
        self._current = start

    def __iter__(self) -> Iterator[int]:
        """
        Return iterator.

        Returns:
            Iterator instance.
        """
        self._current = self._start
        return self

    def __next__(self) -> int:
        """
        Return next countdown value.
        """
        if self._current < 0:
            raise StopIteration

        value = self._current
        self._current -= 1

        return value


class AlphabetIterator:
    """
    Iterate through uppercase English letters.
    """

    def __init__(self) -> None:
        """Initialize iterator."""
        self._letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._index = 0

    def __iter__(self) -> Iterator[str]:
        """
        Return iterator.
        """
        self._index = 0
        return self

    def __next__(self) -> str:
        """
        Return next letter.
        """
        if self._index >= len(self._letters):
            raise StopIteration

        letter = self._letters[self._index]
        self._index += 1

        return letter


class EmployeeIterator:
    """
    Iterate through employee names.
    """

    def __init__(
        self,
        employees: list[str],
    ) -> None:
        """
        Initialize iterator.

        Args:
            employees:
                Employee names.
        """
        self._employees = employees
        self._index = 0

    def __iter__(self) -> Iterator[str]:
        """
        Return iterator.
        """
        self._index = 0
        return self

    def __next__(self) -> str:
        """
        Return next employee.
        """
        if self._index >= len(self._employees):
            raise StopIteration

        employee = self._employees[self._index]
        self._index += 1

        return employee


def manual_iteration(
    values: list[int],
) -> list[int]:
    """
    Demonstrate iter() and next().

    Args:
        values:
            Input values.

    Returns:
        Iterated values.
    """
    iterator = iter(values)

    result: list[int] = []

    while True:

        try:
            result.append(next(iterator))

        except StopIteration:
            break

    return result


def consume_iterator(
    iterator: Iterator[int],
) -> list[int]:
    """
    Consume an iterator.

    Args:
        iterator:
            Input iterator.

    Returns:
        Iterator values.
    """
    result: list[int] = []

    for value in iterator:
        result.append(value)

    return result


def iterator_sum(
    iterator: Iterator[int],
) -> int:
    """
    Sum iterator values.

    Args:
        iterator:
            Iterator.

    Returns:
        Sum of values.
    """
    total = 0

    for value in iterator:
        total += value

    return total


def iterator_max(
    iterator: Iterator[int],
) -> int:
    """
    Return maximum iterator value.

    Args:
        iterator:
            Input iterator.

    Returns:
        Maximum value.

    Raises:
        ValueError:
            If iterator is empty.
    """
    values = list(iterator)

    if not values:
        raise ValueError(
            "iterator is empty."
        )

    return max(values)


def iterator_to_list(
    iterator: Iterator[int],
) -> list[int]:
    """
    Convert iterator into list.

    Args:
        iterator:
            Input iterator.

    Returns:
        List.
    """
    return list(iterator)


__all__ = [
    "NumberIterator",
    "CountdownIterator",
    "AlphabetIterator",
    "EmployeeIterator",
    "manual_iteration",
    "consume_iterator",
    "iterator_sum",
    "iterator_max",
    "iterator_to_list",
]