"""
JSON file handling helpers.

This module contains utility methods for reading from
and writing to JSON files.
"""

import json
from typing import Any


class FileHandler:
    """Utility class for JSON file operations."""

    @staticmethod
    def read_json(path: str) -> Any:
        """
        Read data from a JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            Any: The Python object stored in the JSON file
                 (list, dictionary, etc.).
        """
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_json(path: str, data: Any) -> None:
        """
        Write Python data to a JSON file.

        Args:
            path (str): Path to the JSON file.
            data (Any): Python object to save as JSON.
        """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
