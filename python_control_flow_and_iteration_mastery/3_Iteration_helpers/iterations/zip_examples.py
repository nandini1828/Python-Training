"""
zip_examples.py

Demonstrates Python zip().
"""

from itertools import zip_longest


class ZipExamples:
    @staticmethod
    def zip_lists(
        names: list[str],
        marks: list[int]
    ) -> list[tuple[str, int]]:
        """Combines two lists."""

        return list(zip(names, marks))

    @staticmethod
    def zip_longest_lists(
        names: list[str],
        marks: list[int]
    ) -> list[tuple]:
        """Uses zip_longest()."""

        return list(zip_longest(names, marks, fillvalue="-"))