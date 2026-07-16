"""Simple promotion rules for employee eligibility."""

from app.models.employee import Employee


class PromotionPolicy:
    """Decide if an employee should be promoted."""

    @staticmethod
    def is_eligible(employee: Employee) -> bool:
        """Promote when employee age and salary meet simple thresholds."""
        return employee.age >= 25 and employee.salary >= 60000
