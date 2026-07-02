"""
logical_operators.py

Demonstrates Python Logical Operators.

Topics Covered:
- and
- or
- not
- Combining multiple conditions
- Real-world validation examples
"""


class LogicalOperatorExamples:
    """
    Utility class demonstrating
    Python logical operators.
    """

    @staticmethod
    def can_vote(age: int, is_citizen: bool) -> bool:
        """
        Checks whether a person
        is eligible to vote.

        Args:
            age: Person's age
            is_citizen: Citizenship status

        Returns:
            True if eligible else False
        """

        return age >= 18 and is_citizen

    @staticmethod
    def login(username: str, password: str) -> bool:
        """
        Validates login credentials.

        Args:
            username: Username
            password: Password

        Returns:
            True if credentials are valid.
        """

        return username == "admin" and password == "admin123"

    @staticmethod
    def has_access(is_admin: bool, is_manager: bool) -> bool:
        """
        Checks whether a user
        has access to a resource.

        Args:
            is_admin: Admin role
            is_manager: Manager role

        Returns:
            True if access is allowed.
        """

        return is_admin or is_manager

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Performs simple email validation.

        Args:
            email: Email address

        Returns:
            True if email looks valid.
        """

        return "@" in email and "." in email

    @staticmethod
    def is_store_open(is_weekend: bool, is_holiday: bool) -> bool:
        """
        Determines whether
        the store is open.

        Args:
            is_weekend: Weekend status
            is_holiday: Holiday status

        Returns:
            True if open.
        """

        return not is_holiday and not is_weekend

    @staticmethod
    def is_even_positive(number: int) -> bool:
        """
        Checks whether a number
        is positive and even.

        Args:
            number: Integer value

        Returns:
            Boolean result.
        """

        return number > 0 and number % 2 == 0

    @staticmethod
    def can_apply_for_loan(
        salary: float,
        credit_score: int
    ) -> bool:
        """
        Checks loan eligibility.

        Rules:
        - Salary >= 50000
        - Credit score >= 700

        Args:
            salary: Monthly salary
            credit_score: Credit score

        Returns:
            Loan eligibility.
        """

        return salary >= 50000 and credit_score >= 700

    @staticmethod
    def student_passed(
        theory_marks: int,
        practical_marks: int
    ) -> bool:
        """
        Checks whether a student
        passed both exams.

        Args:
            theory_marks: Theory marks
            practical_marks: Practical marks

        Returns:
            True if student passed.
        """

        return theory_marks >= 35 and practical_marks >= 35

    @staticmethod
    def can_watch_movie(age: int, with_parent: bool) -> bool:
        """
        Determines movie eligibility.

        Rules:
        - Age >= 18
        OR
        - Parent accompanies.

        Args:
            age: Person's age
            with_parent: Parent present

        Returns:
            Eligibility status.
        """

        return age >= 18 or with_parent

    @staticmethod
    def account_active(is_blocked: bool) -> bool:
        """
        Checks whether an account
        is active.

        Args:
            is_blocked: Account status

        Returns:
            True if active.
        """

        return not is_blocked