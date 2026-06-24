from typing import Any


class NestedJSONQueryEngine:
    """
    Provides functionality to query nested
    dictionaries using dot-separated paths.

    Example:
        user.profile.name
    """

    @staticmethod
    def query(
        data: dict,
        path: str,
        default: Any = None
    ) -> Any:
        """
        Retrieves a value from a nested dictionary.

        Args:
            data: Nested dictionary
            path: Dot-separated path
            default: Returned if path not found

        Returns:
            Value at path or default
        """

        current: Any = data

        for key in path.split("."):

            if isinstance(current, dict):
                current = current.get(key)

            else:
                return default

            if current is None:
                return default

        return current