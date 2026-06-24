from typing import Any


class JsonQuery:

    @staticmethod
    def query(
        data: dict,
        path: str,
        default: Any = None
    ) -> Any:

        current: Any = data

        for key in path.split("."):

            if isinstance(current, dict):
                current = current.get(key)
            else:
                return default

            if current is None:
                return default

        return current