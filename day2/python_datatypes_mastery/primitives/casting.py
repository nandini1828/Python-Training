from typing import Any


class SafeCaster:

    @staticmethod
    def cast(
        value: Any,
        target_type: type,
        default: Any = None
    ) -> Any:
        try:
            return target_type(value)
        except (ValueError, TypeError):
            return default