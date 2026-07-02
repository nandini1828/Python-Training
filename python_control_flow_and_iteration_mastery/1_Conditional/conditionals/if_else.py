"""
if_else.py

Demonstrates Python if-elif-else statements.

Topics Covered:
- if
- if-else
- if-elif-else
- Nested if
"""


class IfElseExamples:
    """
    Utility class containing examples of
    Python conditional statements.
    """

    @staticmethod
    def check_number(number: int) -> str:
        """
        Checks whether a number is positive,
        negative or zero.

        Args:
            number: Integer value

        Returns:
            Status message
        """

        if number > 0:
            return "Positive"

        elif number < 0:
            return "Negative"

        return "Zero"

    @staticmethod
    def check_age(age: int) -> str:
        """
        Determines whether a person
        is eligible to vote.

        Args:
            age: Person's age

        Returns:
            Eligibility message
        """

        if age >= 18:
            return "Eligible to Vote"

        return "Not Eligible to Vote"

    @staticmethod
    def calculate_grade(marks: int) -> str:
        """
        Calculates grade based on marks.

        Args:
            marks: Student marks

        Returns:
            Grade
        """

        if marks >= 90:
            return "A"

        elif marks >= 75:
            return "B"

        elif marks >= 60:
            return "C"

        elif marks >= 40:
            return "D"

        return "Fail"

    @staticmethod
    def find_largest(
        first: int,
        second: int
    ) -> int:
        """
        Finds the larger of two numbers.

        Args:
            first: First number
            second: Second number

        Returns:
            Larger number
        """

        if first > second:
            return first

        return second

    @staticmethod
    def check_even_or_odd(number: int) -> str:
        """
        Checks whether a number
        is even or odd.

        Args:
            number: Integer value

        Returns:
            Even or Odd
        """

        if number % 2 == 0:
            return "Even"

        return "Odd"

    @staticmethod
    def validate_password(password: str) -> str:
        """
        Simple password validation.

        Rules:
        - Minimum 8 characters

        Args:
            password: User password

        Returns:
            Validation message
        """

        if len(password) >= 8:
            return "Valid Password"

        return "Password Too Short"

    @staticmethod
    def check_discount(amount: float) -> str:
        """
        Determines discount percentage
        based on purchase amount.

        Args:
            amount: Purchase amount

        Returns:
            Discount message
        """

        if amount >= 10000:
            return "20% Discount"

        elif amount >= 5000:
            return "10% Discount"

        elif amount >= 1000:
            return "5% Discount"

        return "No Discount"

    @staticmethod
    def login_status(
        username: str,
        password: str
    ) -> str:
        """
        Simple login validation.

        Args:
            username: Username
            password: Password

        Returns:
            Login status
        """

        if username == "admin":

            if password == "admin123":
                return "Login Successful"

            return "Invalid Password"

        return "Invalid Username"