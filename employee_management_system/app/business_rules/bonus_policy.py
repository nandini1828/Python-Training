"""Bonus policy for employee compensation."""

from app.config.constants import BONUS_PERCENTAGE
from app.models.employee import Employee


class BonusPolicy:
    """Compute a simple bonus based on salary."""

    @staticmethod
    def calculate_bonus(employee: Employee) -> float:
        """Return the bonus value for an employee salary."""
        return round(employee.salary * BONUS_PERCENTAGE, 2)
