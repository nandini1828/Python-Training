"""Salary helper service for simple payroll calculations."""

from app.services.validation_service import ValidationService


class SalaryService:
    """Provide salary-related operations."""

    def __init__(self, validator: ValidationService | None = None) -> None:
        self.validator = validator or ValidationService()

    def calculate_bonus(self, salary: float, bonus_percentage: float = 0.10) -> float:
        """Return the bonus value for a salary."""
        self.validator.validate_salary(salary)
        return round(salary * bonus_percentage, 2)

    def get_net_salary(self, salary: float, bonus_percentage: float = 0.10) -> float:
        """Return salary plus bonus."""
        return round(salary + self.calculate_bonus(salary, bonus_percentage), 2)
