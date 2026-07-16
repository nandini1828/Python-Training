"""Validation helpers for employee data."""

import re

from app.config.constants import MAX_LEAVE_DAYS, MINIMUM_AGE, MINIMUM_SALARY


class ValidationService:
    """Simple validation class for employee rules."""

    @staticmethod
    def validate_age(age: int) -> bool:
        """Age must be at least the minimum age."""
        return age >= MINIMUM_AGE

    @staticmethod
    def validate_salary(salary: float) -> bool:
        """Salary must be at least the minimum salary."""
        return salary >= MINIMUM_SALARY

    @staticmethod
    def validate_email(email: str) -> bool:
        """Check if email follows a basic email format."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_leave_days(days: int) -> bool:
        """Leave days cannot exceed the company policy maximum."""
        return 0 <= days <= MAX_LEAVE_DAYS

    def validate_employee(self, age: int, salary: float, email: str) -> dict[str, bool]:
        """Run all employee validations together."""
        return {
            "age_ok": self.validate_age(age),
            "salary_ok": self.validate_salary(salary),
            "email_ok": self.validate_email(email),
        }
