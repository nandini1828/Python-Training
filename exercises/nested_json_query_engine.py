"""
Nested JSON Query Engine

Provides functionality to retrieve values
from nested dictionaries using dot-separated paths.
"""

from typing import Any


class NestedJSONQueryEngine:
    """
    Query nested JSON-like dictionaries.
    """

    def query(
        self,
        data: dict,
        path: str,
        default: Any = None
    ) -> Any:
        """
        Retrieves a value from a nested dictionary.

        Parameters
        ----------
        data : dict
            Nested dictionary structure.

        path : str
            Dot-separated path.

        default : Any
            Value returned if path is not found.

        Returns
        -------
        Any
            Retrieved value or default.
        """

        current = data

        for key in path.split("."):

            if isinstance(current, dict):
                if key in current:
                    current = current[key]
                else:
                    return default
            elif isinstance(current, list):
                try:
                    index = int(key)
                    current = current[index]
                except (ValueError, IndexError):
                    return default
            else:
                return default

        return current


def demo_json_query():
    """Demonstrate nested JSON query functionality."""
    engine = NestedJSONQueryEngine()
    data = {"user": {"profile": {"name": "Alice"}}}
    
    result1 = engine.query(data, "user.profile.name")
    result2 = engine.query(data, "user.profile.age", 18)
    
    return (result1, result2)