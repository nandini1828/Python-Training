"""
Type Casting Utilities
"""


class TypeCastingUtility:

    @staticmethod
    def string_to_float(
        value: str
    ) -> float:
        return float(value)

    @staticmethod
    def integer_to_string(
        value: int
    ) -> str:
        return str(value)

    @staticmethod
    def float_to_integer(
        value: float
    ) -> int:
        return int(value)

    @staticmethod
    def safe_cast(
        value,
        target_type,
        default=None
    ):
        try:
            return target_type(value)

        except (
            ValueError,
            TypeError
        ):
            return default