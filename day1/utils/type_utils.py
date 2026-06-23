"""
Type Utilities
"""


class TypeUtility:

    @staticmethod
    def safe_cast(
        value,
        target_type,
        default=None
    ):
        try:
            return target_type(value)

        except (
            TypeError,
            ValueError
        ):
            return default

    @staticmethod
    def is_instance(
        obj,
        expected_type
    ) -> bool:
        return isinstance(
            obj,
            expected_type
        )