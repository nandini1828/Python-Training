"""
short_circuit.py

Demonstrates Python Short-Circuit Evaluation.

Topics Covered:
- and
- or
- Short-Circuit Evaluation
- Real-world examples
"""


class ShortCircuitExamples:
    """
    Utility class demonstrating
    Python short-circuit evaluation.
    """

    @staticmethod
    def using_and(age: int, has_license: bool) -> bool:
        """
        Returns True only if both
        conditions are satisfied.
        """

        return age >= 18 and has_license

    @staticmethod
    def using_or(username: str) -> str:
        """
        Returns the username if present,
        otherwise returns Guest.
        """

        return username or "Guest"

    @staticmethod
    def safe_division(number: int, divisor: int) -> bool:
        """
        Demonstrates short-circuit with AND.

        Prevents division by zero.
        """

        return divisor != 0 and number / divisor > 1

    @staticmethod
    def default_discount(discount: int) -> int:
        """
        Returns discount if available,
        otherwise returns 5.
        """

        return discount or 5

    @staticmethod
    def can_access_portal(
        is_logged_in: bool,
        is_admin: bool
    ) -> bool:
        """
        User can access if logged in
        and is an administrator.
        """

        return is_logged_in and is_admin

    @staticmethod
    def get_display_name(name: str) -> str:
        """
        Returns user name if available,
        otherwise Anonymous.
        """

        return name or "Anonymous"

    @staticmethod
    def has_data(data: list) -> bool:
        """
        Checks whether list contains data.
        """

        return bool(data) and len(data) > 0

    @staticmethod
    def get_first_item(items: list):
        """
        Returns first item if list
        contains data.
        """

        return items and items[0]