"""
dictionary_safety.py

Demonstrates safe dictionary access.
"""

from collections import defaultdict


class DictionarySafetyExamples:
    """Utility class demonstrating dictionary safety."""

    @staticmethod
    def safe_get(
        data: dict,
        key: str
    ):
        """Returns value using get()."""

        return data.get(key, "Key Not Found")

    @staticmethod
    def default_dictionary() -> dict:
        """Returns defaultdict example."""

        scores = defaultdict(int)

        scores["Python"] += 10

        return dict(scores)

    @staticmethod
    def check_key(
        data: dict,
        key: str
    ) -> bool:
        """Checks whether key exists."""

        return key in data