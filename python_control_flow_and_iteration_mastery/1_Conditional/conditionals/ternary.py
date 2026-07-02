"""
ternary.py

Demonstrates Python Ternary Operator.

Topics Covered:
- Conditional Expressions
- Single-line if-else
"""


class TernaryExamples:
    """
    Utility class demonstrating
    Python ternary operator.
    """

    @staticmethod
    def even_or_odd(number: int) -> str:
        """
        Returns Even or Odd.
        """

        return "Even" if number % 2 == 0 else "Odd"

    @staticmethod
    def pass_or_fail(marks: int) -> str:
        """
        Returns Pass or Fail.
        """

        return "Pass" if marks >= 40 else "Fail"

    @staticmethod
    def largest(first: int, second: int) -> int:
        """
        Returns larger number.
        """

        return first if first > second else second

    @staticmethod
    def voting_status(age: int) -> str:
        """
        Returns voting eligibility.
        """

        return "Eligible" if age >= 18 else "Not Eligible"

    @staticmethod
    def login_message(is_logged_in: bool) -> str:
        """
        Returns login status.
        """

        return "Welcome" if is_logged_in else "Login Required"

    @staticmethod
    def maximum(first: int, second: int, third: int) -> int:
        """
        Returns maximum among
        three numbers.
        """

        return (
            first
            if first >= second and first >= third
            else second if second >= third else third
        )

    @staticmethod
    def discount(amount: float) -> str:
        """
        Returns discount status.
        """

        return "Discount Applied" if amount >= 5000 else "No Discount"