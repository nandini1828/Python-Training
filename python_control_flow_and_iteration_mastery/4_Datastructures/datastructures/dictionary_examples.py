"""
dictionary_examples.py

Demonstrates dictionary iteration.
"""


class DictionaryExamples:
    """Utility class demonstrating dictionaries."""

    @staticmethod
    def iterate_keys(data: dict) -> list:
        """Returns all keys."""

        return list(data.keys())

    @staticmethod
    def iterate_values(data: dict) -> list:
        """Returns all values."""

        return list(data.values())

    @staticmethod
    def iterate_items(data: dict) -> list:
        """Returns key-value pairs."""

        return list(data.items())