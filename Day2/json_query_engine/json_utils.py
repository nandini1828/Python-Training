"""
==================================================
Module: JSON Query Engine
Topic: Nested JSON Querying

Description:
A beginner-friendly class for reading values from
nested dictionaries.
==================================================
"""

from __future__ import annotations

from typing import Any


class JsonQueryEngine:
    """A simple class to read values from nested JSON-like data."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    def get_value(self, path: str) -> Any:
        """Return a value from a dot-separated path."""
        current: Any = self.payload
        for part in path.split("."):
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        return current
